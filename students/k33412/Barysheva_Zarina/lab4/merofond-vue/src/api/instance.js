import axios from 'axios'


const apiURL = '127.0.0.1:777'


const instance = axios.create({
 baseURL: apiURL
})


export default instance
