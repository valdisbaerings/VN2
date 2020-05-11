const filter_function = (id) => {
    console.log(id)
    $.ajax({
        url: '/products?product_filter=' + id,
        type: 'GET',
        success: function (resp) {
            console.log('hello')
            var newHtml = resp.data.map(d => {
                return `<div class="well products">
                    <a href="/products/${d.id}">
                        <img class="product-img" src="${d.firstImage}"/>
                        <h4>${d.name}</h4>
                        <p>${d.price}</p>
                        <p>${d.description}</p>
                    </a>
                </div>`
            });
            $('.products').html(newHtml.join(''));

        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error)
        }
    });
};
