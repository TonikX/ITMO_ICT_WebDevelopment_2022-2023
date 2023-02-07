//import SignIn from "@/components/SignIn.vue";
//import SignUp from "@/components/SignUp.vue";
import FreeRoomsPage from "@/views/FreeRoomsPage.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  // массив с роутами
  // отдельный роут:
  { path: "/freeRooms", component: FreeRoomsPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
