import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import store from './stores'

import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

const app = createApp(App)

app.use(store)
app.use(router)

app.mount('#app')
