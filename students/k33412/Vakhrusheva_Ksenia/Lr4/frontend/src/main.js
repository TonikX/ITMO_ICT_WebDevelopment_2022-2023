import {createApp} from 'vue'
import App from './App.vue'

import './assets/main.css'
import router from "@/router";
import vuetify from "@/plugins/vuetify";

import axios from "axios";
import {createPinia} from "pinia";

axios.defaults.baseURL = "http://localhost:8000"

const pinia = createPinia();

createApp(App)
	.use(vuetify)
	.use(router)
	.use(pinia)
	.mount('#app')
