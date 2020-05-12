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
                            <a href="/products/games/${d.id}">
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                                <p>${d.price}$</p>
                            </a>
                        </div>`
                    }
                    else {
                        return `<div class="well products">
                            <a href="/products/consoles/${d.id}">
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4>
                                <p>${d.description}</p>
                                <p>${d.price}$</p>
                            </a>
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

