import Vue from "vue";
import VueRouter from "vue-router";
import RacesList from "@/views/RacesListView";
import UserAuth from "@/views/UserAuthView";
import RidersListView from "@/views/RidersListView";
import RaceDetailsView from "@/views/RaceDetailsView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/races",
    name: "RacesList",
    component: RacesList,
  },
  {
    path: "/races/:id",
    name: "RaceDetails",
    component: RaceDetailsView,
  },
  {
    path: "/riders",
    name: "RidersList",
    component: RidersListView,
  },
  {
    path: "/auth",
    name: "UserAuth",
    component: UserAuth,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem("authToken") !== null || to.path === "/auth") {
    next();
  } else {
    next("/auth");
  }
});

export default router;
