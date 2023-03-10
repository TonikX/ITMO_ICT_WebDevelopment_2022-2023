import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Auth from './views/Auth.vue'

createApp(App)
    .use(router)
    .component('Auth', Auth)
    .mount('#app')
