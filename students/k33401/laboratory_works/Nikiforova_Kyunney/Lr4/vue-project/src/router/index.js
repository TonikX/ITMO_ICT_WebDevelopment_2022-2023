import { createRouter, createWebHistory } from "vue-router";
import Main from "../views/Main.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import description from "../views/card_description.vue";
import calender from "../views/CalendarPage.vue";
import Profile from "../views/Profile.vue";
import Not_Found from "../views/404.vue";


const routes = [
    {
       path: "/",
       name: "Main",
       component: Main,
       meta: {
           title: 'Home'
       }
    },
    {
        path: "/Login",
        name: "login",
        component: Login,
        meta: {
            title: 'Login'
        }
    },
    {
        path: "/Register",
        name: "register",
        component: Register,
        meta: {
            title: 'Register'
        }
    },
    {
        path: "/Description/:id",
        name: "description",
        component: description,
        meta: {
            title: 'description'
        }
    },
    {
        path: "/Calendar",
        name: "calendar",
        component: calender,
        meta: {
            title: 'calender'
        }
    },
    {
        path: "/Profile",
        name: "profile",
        component: Profile,
        meta: {
            title: 'Profile'
        }
    },
    {
        path: '/:pathMatch(.*)*',
        name: "Not_Found",
        component: Not_Found,
        meta:{
          title: '404'
        }
    
      }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});
router.beforeEach((to, from, next) =>
{
    document.title = `${to.meta.title} | Event`;
    next();
})

export default router;