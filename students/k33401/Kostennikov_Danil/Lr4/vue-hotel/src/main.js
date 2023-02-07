import { createApp } from "vue";
import App from "./App.vue";
import "./assets/main.css";
import router from "./router";
import store from "./stores";

const app = createApp(App);

app.use(store);
app.use(router);

app.mount("#app");
