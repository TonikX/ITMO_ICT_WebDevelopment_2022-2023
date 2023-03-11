import {createRouter, createWebHistory} from 'vue-router'
import Products from "../views/Products.vue";
import Product from "../views/Product.vue";
import Profile from "../views/Profile.vue";
import Staff from "../views/Staff.vue";
import Sells from "../views/Sells.vue";
import Register from "../views/Register.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/product',
      name: 'product',
      component: Product
    },
    {
      path: '/',
      name: 'products',
      component: Products
    },
    {
      path: '/profile/',
      name: 'profile',
      component: Profile
    },
    {
      path: '/sells/',
      name: 'sells',
      component: Sells
    },
    {
      path: '/staff/',
      name: 'staff',
      component: Staff
    },
    {
      path: '/register/',
      name: 'register',
      component: Register
    }
  ]
})

export default router
