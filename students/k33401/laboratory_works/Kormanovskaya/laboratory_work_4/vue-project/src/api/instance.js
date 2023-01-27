import axios from 'axios'

const apiURL = 'http://localhost:4000'

const instance = axios.create({
    baseURL: apiURL
})

export default instance
