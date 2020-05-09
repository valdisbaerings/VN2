$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        var text = $('#search-box').val();
        console.log(text)
         $.ajax({
            url: '/products/search_history',
            type: 'POST',
             data: {
                 text: text,
                 csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
             },
            success: function() {
                return data
            } ,
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error)
            }
        });

    });

});