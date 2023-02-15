//import SignIn from "@/components/SignIn.vue";
//import SignUp from "@/components/SignUp.vue";
import FreeRoomsPage from "@/views/FreeRoomsPage.vue";
import RegisterPage from "@/views/RegisterPage.vue";
import RegisterComponent from "@/components/Register.vue";
import LoginComponent from "@/components/Login.vue";
import Navbar from "@/components/Navbar.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  // массив с роутами
  // отдельный роут:
  { path: "/freeRooms", component: FreeRoomsPage },
  { path: "/register", component: RegisterComponent },
  { path: "/login", component: LoginComponent },
  { path: "/navbar", component: Navbar },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
