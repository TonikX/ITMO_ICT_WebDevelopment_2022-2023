// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};
// Скрыить форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};
// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        error: (response) => {
            console.log("False")
        }
    })
};
// Подписаться
let follow = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/profile/follow/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        error: (response) => {
            console.log("False")
        }
    })
};
// обработать форму авторизации с помощью ajax request.
$(".need_auth").submit(function (e) {
    e.preventDefault();
    var url = $(this).attr('action');
    var data = $(this).serialize();
    $.post(
        url,
        data,
        function (response) {
            window.location = response.location;
        },
    );
});
