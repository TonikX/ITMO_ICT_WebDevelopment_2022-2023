import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import './assets/main.css'

const vuetify = createVuetify({
    components,
    directives
})

const app = createApp(App).use(vuetify)

app.use(router)

app.mount('#app')