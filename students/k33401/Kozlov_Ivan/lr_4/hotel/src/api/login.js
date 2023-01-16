class LoginApi {
    constructor(instance) {
        this.API = instance
    }

    login = async (data) => {
        return this.API({
            method: 'POST',
            url: '/auth/token/login/',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        }).catch(function (error) {
            if (error.toJSON().message){
                alert("Неверный пароль или логин")
            }
        });
    };
}

export default LoginApi
