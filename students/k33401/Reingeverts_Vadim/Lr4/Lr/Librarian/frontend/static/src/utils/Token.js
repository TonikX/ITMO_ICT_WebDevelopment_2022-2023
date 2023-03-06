// https://stackoverflow.com/a/43943556
export const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

export const getLocalStorageToken = () => {
    return JSON.parse(localStorage.getItem("token"));
};
export const getSessionStorageToken = () => {
    return JSON.parse(sessionStorage.getItem("token"));
};
