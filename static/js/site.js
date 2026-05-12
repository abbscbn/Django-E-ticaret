$(document).ready(function () {

    $("#query").autocomplete({

        source: function (request, response) {

            $.ajax({

                url: "/search_auto/",
                dataType: "json",
                data: {
                    term: request.term
                },

                success: function (data) {
                    response(data);
                }

            });

        },

        minLength: 2

    });

});