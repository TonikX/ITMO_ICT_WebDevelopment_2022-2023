import { createApp } from 'vue'

import App from '@/App.vue'
import router from '@/router'
import store from "@/stores";
import components from '@/components/UI'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import '@/assets/main.css'
import '@/assets/dark.css'
import '@/assets/light.css'
import VueApexCharts from "vue3-apexcharts";

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app.component('apexchart', VueApexCharts)

app.use(store)
app.use(router)

app.mount('#app')
