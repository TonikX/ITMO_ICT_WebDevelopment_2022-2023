import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";
import Rooms from "@/views/Rooms.vue";
import Guests from "@/views/Guests.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/rooms",
    name: "Rooms",
    component: Rooms,
    meta: { requiresAuth: true },
  },
  {
    path: "/",
    redirect: "/rooms",
  },
  {
    path: "/guests",
    name: "Guests",
    component: Guests,
    meta: { requiresAuth: true },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!localStorage.getItem("auth_token")) {
      next({
        name: "Login",
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
