
$(function () {
    function insert_excuse(result) {
        console.log(result)
    }

    $('.make_excuse').click(function (e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "/get_excuse",
            contentType: 'application/json;charset=UTF-8',
            success: function (result) {
                // insert_excuse(result);
                $('#excuse').text(result)
            },
            error: function (result) {
                console.log(result)
            }
        })
    });
});