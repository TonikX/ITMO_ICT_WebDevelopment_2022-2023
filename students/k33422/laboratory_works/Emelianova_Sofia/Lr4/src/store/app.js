// Utilities
import { defineStore } from 'pinia'
import API from '@/api';
import router from '@/router';

export const useAppStore = defineStore('app', {
  state: () => ({
    user: null,
    allBooks: [],
    myBooks: [],
    notification: null
  }),
  getters: {
    getUser() {
      const username = localStorage.getItem('LIBRARY_USERNAME');
      return username;
    },
    getAllBooksSorted() {
      return this.allBooks.filter(v => !v.reader).reduce((acc, v) => {
        (acc[v.book] = acc[v.book] || []).push(v);
        return acc;
      }, {});
    }
  },
  actions: {
    async userAuth(username, password) {
      if (!username || !password) {
          this.addNotification('error', 'Вы не ввели имя пользователя и/или пароль')
          return;
      }

      const { auth_token } = await API.userAuth(username, password);
      if (!auth_token) {
          console.error('Auth error!');
          return;
      }

      localStorage.setItem('LIBRARY_AUTH_TOKEN', auth_token);
      localStorage.setItem('LIBRARY_USERNAME', username);
      this.getUserInfo();
      router.push('/')
    },
    async getUserInfo() {
      const result = await API.getUser(this.getUser || 'admin2');
      if (!result) {
        return;
      }

      this.user = result;
    },
    async userRegister(regData) {
      const result = await API.userRegister(regData);
      if (!result) {
        return;
      }

      await this.userAuth(regData.username, regData.password);
      await this.getUserInfo();
    },
    async saveUserInfo(credentials) {
      const result = await API.userChangeCredentials(credentials)
        .catch(err => {
          this.addNotification('error', err.response.data)
        });
      if (!result) {
        return;
      }

      this.user = credentials;
    },

    logOut() {
      localStorage.removeItem('LIBRARY_AUTH_TOKEN');
      localStorage.removeItem('LIBRARY_USERNAME');
      window.location.reload();
    },

    async getMyBooks() {
      const result = await API.getUserBooks(this.getUser || 'admin2');
      if (!result) {
        return;
      }

      this.myBooks = result;
    },
    
    async getAllBooks() {
      const result = await API.getAllBooks();
      if (!result) {
        return;
      }

      this.allBooks = result;
    },

    async bookTake(bookName) {
      const result = await API.userBookTake(this.getUser || 'admin2', bookName);
      if (!result) {
        return;
      }

      await this.getAllBooks();
      await this.getMyBooks();
    },

    async bookReturn(bookName) {
      const result = await API.userBookReturn(this.getUser || 'admin2', bookName);
      if (!result) {
        return;
      }

      await this.getAllBooks();
      await this.getMyBooks();
    },

    addNotification(type = 'info', msg) {
      if (msg.id) {
        return;
      }

      const timeout = setTimeout(() => {
        this.notification = null;
      }, 2000);

      if (this.notification) {
        this.notification = null;
        clearTimeout(timeout);
        this.addNotification(type, msg);
        return;
      }

      this.notification = {
        type,
        msg
      }
    }
  }
})
