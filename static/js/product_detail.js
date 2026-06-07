let currentScale = 1;
let currentIndex = 0;

// ================= IMAGE =================
function changeImage(element, index) {
    document.getElementById("mainImage").src = element.src;
    document.getElementById("modalImage").src = element.src;

    currentIndex = index;

    document.querySelectorAll(".gallery-thumb-wrapper")
        .forEach(item => item.classList.remove("active-thumb"));

    element.parentElement.classList.add("active-thumb");
}

function nextImage() {
    currentIndex = (currentIndex + 1) % imageList.length;
    updateModalImage();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + imageList.length) % imageList.length;
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

// ================= COMMENTS =================
$(document).ready(function () {

    const csrftoken = getCookie('csrftoken');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie) {
            document.cookie.split(';').forEach(c => {
                c = c.trim();
                if (c.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(c.split('=')[1]);
                }
            });
        }
        return cookieValue;
    }

    function resetStars() {
        $(".rating-star")
            .removeClass("bi-star-fill")
            .addClass("bi-star");

        $("#rateInput").val(5);
    }

    $(".rating-star").click(function () {
        let value = $(this).data("value");

        $("#rateInput").val(value);

        $(".rating-star").each(function () {
            $(this).toggleClass(
                "bi-star-fill",
                $(this).data("value") <= value
            ).toggleClass(
                "bi-star",
                $(this).data("value") > value
            );
        });
    });



    $("#commentForm").submit(function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: commentUrl,
            data: $(this).serialize(),
            headers: { "X-CSRFToken": csrftoken },

            success: function (response) {

                if (response.status === "success") {

                    $("#comment-message").html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    $("#commentForm")[0].reset();
                    resetStars();

                } else {

                    let html = `<div class="alert alert-danger">`;

                    if (response.errors) {
                        $.each(response.errors, function (_, value) {
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

// ================= VARIANTS =================
const variants =
    JSON.parse(document.getElementById("variant-data").textContent);

let selectedAttributes =
    JSON.parse(document.getElementById("active-attributes").textContent || "[]");

// ================= ATTRIBUTE CLICK =================
document.querySelectorAll(".attribute-btn").forEach(btn => {

    btn.addEventListener("click", function () {

        const valueId = parseInt(this.dataset.value);
        const attributeName = this.dataset.attribute;

        // 1. aynı attribute group içindeki eski value’yu sil
        const groupValues = document.querySelectorAll(
            `[data-attribute="${attributeName}"]`
        );

        groupValues.forEach(el => {
            const id = parseInt(el.dataset.value);
            selectedAttributes = selectedAttributes.filter(v => v !== id);
            el.classList.remove("active-attribute");
        });

        // 2. yeni value ekle
        selectedAttributes.push(valueId);
        this.classList.add("active-attribute");

        // 3. variant match (subset logic)
        const matched = variants.find(v =>
            selectedAttributes.every(id =>
                v.attributes.includes(id)
            )
        );

        if (matched) {
            window.location.href = matched.url;
        }
    });
});