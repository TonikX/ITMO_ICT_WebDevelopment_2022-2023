import axios from "axios";


const apiURL = 'http://127.0.0.1:8000'

const instance = axios.create({
    baseURL: apiURL
})

instance.interceptors.request.use(function (config) {
    // Do something before request is sent
    // console.log(config)
    return config;
}, function (error) {
    // Do something with request error
    return Promise.reject(error);
});

instance.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    return response;
}, async function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    if (error.response.status === 401) {
        const originalRequest = error.config
        const refreshToken = localStorage.getItem('refreshToken')
        const response = async (refreshToken) => {
            return await instance({
                method: 'POST',
                url: `/auth/token/refresh/`,
                data: {
                    refresh: refreshToken
                }
            })
        }

        const accessToken = await response(refreshToken)
        localStorage.setItem('accessToken', accessToken.data.access)

        originalRequest.headers['Authorization'] = 'Bearer ' + accessToken.data.access

        return instance(originalRequest)
    }
    return Promise.reject(error);
})

export default instance
