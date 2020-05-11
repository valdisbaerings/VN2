const addToWishlist = (id) => {
    $.ajax({
        url: `/user/addToWishlist`,
        type: 'POST',
        data: JSON.stringify({product_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            $("#items_in_wishlist").html(resp.numberOfItems)
            confirm("The item has been added to your wishlist, check out your wishlist in your profile!")
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}

const deleteFromWishlist = (id) => {
    $.ajax({
        url: `/user/deleteFromWishlist`,
        type: 'POST',
        data: JSON.stringify({wishlist_id: id}),
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