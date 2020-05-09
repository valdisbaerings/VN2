const addToCart = (id) => {
    $.ajax({
        url: `/cart/addToCart`,
        type: 'POST',
        data: JSON.stringify({product_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            $("#items_in_cart").html(resp.numberOfItems)
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}

