import { createApp } from 'vue'
import App from './App.vue'


//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
//import 'bootstrap/dist/css/bootstrap.css'
//import 'bootstrap-vue/dist/bootstrap-vue.css'

import './assets/main.css'
import router from "./router";

//Vue.use(BootstrapVue)

createApp(App).use(router).mount('#app')

