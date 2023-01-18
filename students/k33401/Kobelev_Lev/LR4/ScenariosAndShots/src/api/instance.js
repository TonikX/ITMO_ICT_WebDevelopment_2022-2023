import axios from 'axios'

const apiURL = 'http://127.0.0.1:8000/'

const instance = axios.create({
    baseURL: apiURL
})

export default instance
