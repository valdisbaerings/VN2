const sorter_function = (id, type) => {
    console.log(type)
    $.ajax({
        url: '/products' + type + '?product_sorter=' + id,
        type: 'GET',
        success: function (resp) {

            var newHtml = resp.data.map(d => {
                if (d.type_id == 1 && (type == '/games/' || type == '')) {
                    console.log('hello')
                    return `<div class="well products">
                        <a href="/products/games/${d.id}">
                            <img class="product-img" src="${d.firstImage}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            <p>${d.price}$</p>
                        </a>
                    </div>`
                }
                else {
                    console.log('hello')
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

        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
};