let currentScale = 1;


let currentIndex = 0;

function changeImage(element, index) {

    document.getElementById("mainImage").src = element.src;

    document.getElementById("modalImage").src = element.src;

    currentIndex = index;

    document.querySelectorAll(".gallery-thumb-wrapper").forEach(item => {
        item.classList.remove("active-thumb");
    });

    element.parentElement.classList.add("active-thumb");

}

function nextImage() {

    currentIndex++;

    if (currentIndex >= imageList.length) {
        currentIndex = 0;
    }

    updateModalImage();

}

function prevImage() {

    currentIndex--;

    if (currentIndex < 0) {
        currentIndex = imageList.length - 1;
    }

    updateModalImage();

}

function updateModalImage() {

    document.getElementById("modalImage").src = imageList[currentIndex];

    resetZoom();

}

function zoomIn() {

    currentScale += 0.2;

    applyZoom();

}

function zoomOut() {

    if (currentScale > 1) {

        currentScale -= 0.2;

        applyZoom();

    }

}

function resetZoom() {

    currentScale = 1;

    applyZoom();

}

function applyZoom() {

    document.getElementById("modalImage").style.transform =
        `scale(${currentScale})`;

}

$(document).ready(function () {

    // CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    // ⭐ STAR RATING
    function resetStars() {
        $(".rating-star")
            .removeClass("bi-star-fill")
            .addClass("bi-star");

        $("#rateInput").val(5); // default 5
    }

    $(".rating-star").on("click", function () {

        let value = $(this).data("value");

        $("#rateInput").val(value);

        $(".rating-star").each(function () {

            if ($(this).data("value") <= value) {
                $(this).removeClass("bi-star").addClass("bi-star-fill");
            } else {
                $(this).removeClass("bi-star-fill").addClass("bi-star");
            }

        });

    });

    // FORM SUBMIT
    $("#commentForm").submit(function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: commentUrl,
            data: $(this).serialize(),
            headers: {
                "X-CSRFToken": csrftoken
            },

            success: function (response) {

                if (response.status === "success") {

                    $("#comment-message").html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    // 🔥 FORM RESET
                    $("#commentForm")[0].reset();

                    // ⭐ STAR RESET
                    resetStars();

                } else {

                    let html = `<div class="alert alert-danger">`;

                    if (response.errors) {
                        $.each(response.errors, function (key, value) {
                            html += `<div>${value[0]}</div>`;
                        });
                    } else {
                        html += response.message;
                    }

                    html += `</div>`;

                    $("#comment-message").html(html);
                }
            },

            error: function () {
                $("#comment-message").html(`
                    <div class="alert alert-danger">
                        Sunucu hatası oluştu
                    </div>
                `);
            }
        });

    });

});
