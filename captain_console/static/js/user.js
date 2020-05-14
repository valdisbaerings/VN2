const change_password_message = (id) => {
    $.ajax({
        success: function () {
            alert("Password successfully changed!")
        },
        error: function (xhr, status, error) {
            console.error(error)
        }
    });
}

