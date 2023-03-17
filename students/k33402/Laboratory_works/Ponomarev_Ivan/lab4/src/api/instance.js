import axios from 'axios'

const defaultURL = "http://localhost:8000"

const instance = axios.create({
    baseURL: defaultURL
})
export default instance