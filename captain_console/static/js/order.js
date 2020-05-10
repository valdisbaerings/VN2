const saveOrder = (id) => {
    $.ajax({
        url: `/order`,
        type: 'POST',
        data: JSON.stringify({order_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            $("#order_items").html(resp.order_items)
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}