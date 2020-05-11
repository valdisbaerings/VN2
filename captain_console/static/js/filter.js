const filter_function = (id) => {
    console.log(id)
    $.ajax({
        url: '/products?product_filter=' + id,
        type: 'GET',
        success: function (resp) {

            var newHtml = resp.data.map(d => {
                if (d.type_id === 1) {

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
                    console.log(d.price)
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
