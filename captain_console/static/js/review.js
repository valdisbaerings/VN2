const addReview = (id) => {
    var text = $('#review-box').val();
    $.ajax({
        url: '/user/review/'+ id + '/add_review',
        type: 'POST',
        data: JSON.stringify({product_id: id, review: text}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            $("#items_in_reviewlist").html(resp.numberOfItems)
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}