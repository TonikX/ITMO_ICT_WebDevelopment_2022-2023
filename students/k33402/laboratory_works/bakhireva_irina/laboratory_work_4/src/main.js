import {createApp} from 'vue'
import {createPinia} from 'pinia'

import App from './App.vue'
import router from './router'

import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import {createVuetify} from "vuetify";
import {VDataTable} from 'vuetify/labs/VDataTable'
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000"

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(createVuetify({
	components: {
		VDataTable,
	}
}))
app.component('DatepickerComponent', Datepicker);
app.mount('#app')
