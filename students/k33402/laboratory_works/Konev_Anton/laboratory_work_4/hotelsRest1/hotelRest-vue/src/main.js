import {createApp} from 'vue'
import icons from '@/components/icons'

import App from '@/App.vue'
import router from '@/router'
import store from "@/stores";
import components from '@/components/my-components'

import './assets/main.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import '@fortawesome/fontawesome-svg-core'
import '@fortawesome/vue-fontawesome'
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {library} from "@fortawesome/fontawesome-svg-core";


const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

icons.forEach(icon => {
    library.add(icon)
})

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(store)
app.use(router)

app.mount('#app')
