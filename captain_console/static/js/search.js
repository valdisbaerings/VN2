$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        var data = {
        name: "helloworld",
        age: 123
    };

    var json = JSON.stringify(data);
    console.log("HHIIII")
    console.log(json)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/products/");
    xhr.setRequestHeader("name", "json");
    xhr.send(json);
    console.log(xhr)


    });

});