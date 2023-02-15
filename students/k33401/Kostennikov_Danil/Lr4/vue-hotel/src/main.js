import { createApp } from "vue";
import App from "./App.vue";
import "./assets/main.css";
import router from "./router";
import store from "./stores";
// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App).use(vuetify);

app.use(store);
app.use(router);

app.mount("#app");
