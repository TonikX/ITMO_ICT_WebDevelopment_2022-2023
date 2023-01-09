import axios from "axios";
import { useAppStore } from '@/store/app';

const BASE_URL = 'http://127.0.0.1:8000'

class API {
    constructor() {
        const client = axios.create({
            baseURL: BASE_URL
        });

        client.interceptors.request.use((config) => {
            const token = localStorage.getItem('LIBRARY_AUTH_TOKEN');
            if (token) {
                config.headers['Authorization'] = `Token ${token}`;
            }

            return config;
        })

        client.interceptors.response.use((response) => {
            const store = useAppStore();
            if (response.data) {
                if (response.data.detail) {
                    store.addNotification('info', response.data.detail);
                    return response.data.detail;
                }
                return response.data;
            }

            return response;

        })

        this.client = client;
    }

    async userAuth (username, password) {
        return await this.client.post('/auth/token/login', {
            username,
            password
        });
    }

    async userChangeCredentials(credentials) {
        return await this.client.put(`/api/v1/user-edit/${credentials.username}/`, credentials);
    }

    async getUser(username) {
        return await this.client.get(`/api/v1/get-user-info/${username}/`);
    }

    async userRegister(registerData) {
        return await this.client.post('/api/v1/reader-register/', registerData);
    }

    async getUserBooks(readerName) {
        return await this.client.get(`/api/v1/books/?reader=${readerName}`);
    }

    async getAllBooks() {
        return await this.client.get(`/api/v1/books-copies/`);
    }

    async userBookTake(userName, bookName) {
        return await this.client.post(`/api/v1/get-book/${userName}/`, {
            book: bookName
        });
    }

    async userBookReturn(userName, bookName) {
        return await this.client.post(`/api/v1/return-book/${userName}/`, {
            book: bookName
        });
    }
}

export default new API;
