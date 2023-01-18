import { createPinia } from 'pinia'
import App from './App.vue'
import "bootstrap"
import 'jquery/src/jquery.js';
import 'popper.js/dist/popper.min.js';
import 'bootstrap/dist/js/bootstrap.min.js';
import "bootstrap/dist/css/bootstrap.css";
import { createApp } from "vue";

import router from "./router";
// import store from "./store";
// import firebase from 'firebase/compat/app'
// import "firebase/compat/auth"
import "bootstrap/dist/js/bootstrap.js";



createApp(App).use(router).use(createPinia()).mount("#app");

