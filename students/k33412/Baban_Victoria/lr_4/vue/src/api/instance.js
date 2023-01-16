import axios from 'axios'

const apiURL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')

const instance = axios.create({
 baseURL: apiURL,
})

if (token){
    instance.defaults.headers.common['Authorization'] = "Token " + token;
}

export default instance