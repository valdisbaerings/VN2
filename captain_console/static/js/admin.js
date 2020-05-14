const deleteProduct = (id) => {
    $.ajax({
        url: `/admin/delete_product`,
        type: 'POST',
        data: JSON.stringify({product_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function (resp) {
            console.log('delete success')
            location.reload();
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
    console.log('deleted')
}

const deleteImage = (id) => {
    $.ajax({
        url: `/admin/delete_image`,
        type: 'POST',
        data: JSON.stringify({image_id: id}),
        headers: {'Content-Type': 'application/json'},
        success: function () {
            console.log('delete success')
            location.reload();
        },
        error: function (xhr, status, error) {
            console.error(error)
        }
    });
}

const back_function = (id) => {
    $.ajax({
        success: function () {
            window.history.back()
            location.reload();
        },
        error: function (xhr, status, error) {
            console.error(error)
        }
    });
}

