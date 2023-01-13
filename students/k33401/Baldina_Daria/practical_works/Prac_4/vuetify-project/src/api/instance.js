import axios from 'axios'

const apiURL = 'https://api.nasa.gov/EPIC'

const instance = axios.create({
  baseURL: apiURL
})

export default instance