$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {

                var newHtml = resp.data.map(d => {
                    return `<div class="well product">
                        <a href="/products/${d.id}">
                            <img class="product-img" src="${d.firstImage}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                        </a>
                    </div>`
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val('');

            },
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error)
            }
        });


    });

});

const addToCart = (id) => {
    $.ajax({
        url: '/cart/addToCart',
        type: 'POST',
        json: {product_id: id},
        success: function (resp) {
            console.log(resp);
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
}