const addToCart = (id) => {
    $.ajax({
        url: `/cart/addToCart`,
        type: 'POST',
        data: JSON.stringify({product_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            $("#items_in_cart").html(resp.numberOfItems)
            confirm("The item has been added to the cart")
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            alert("You are not logged in, please log in before adding to cart!")
            console.error(error)
        }
    });
}


const deleteFromCart = (id) => {
    $.ajax({
        url: `/cart/deleteFromCart`,
        type: 'POST',
        data: JSON.stringify({cart_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            location.reload();
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}