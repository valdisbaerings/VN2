$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {

                let newHtml = resp.data.map(d => {
                    if (d.type_id === 1) {
                        return `<div class="well product">
                                <div class="card">
                                <div class="card-body">
                            <a href="/products/games/${d.id}">
                                <img class="product-img" src="${d.firstImage}"/>
                                <h6>${d.name}</h6>
                            </a>
                            <h3 class="mb-0 font-weight-semibold">${ d.price }</h3>
                            <button type="button" class="btn bg-cart" onclick="addToCart(${ d.id })"><i
                            class="fa fa-cart-plus mr-2"></i> Add to cart</button>
                            </div></div>
                        </div>`
                    }
                    else {
                        return `<div class="well product">
                                <div class="card">
                                <div class="card-body">
                            <a href="/products/consoles/${d.id}">
                                <img class="product-img" src="${d.firstImage}"/>
                                <h6>${d.name}</h6>
                            </a>
                            <h3 class="mb-0 font-weight-semibold">${ d.price }</h3>
                            <button type="button" class="btn bg-cart" onclick="addToCart(${ d.id })"><i
                            class="fa fa-cart-plus mr-2"></i> Add to cart</button>
                            </div></div>
                        </div>`
                    }
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

