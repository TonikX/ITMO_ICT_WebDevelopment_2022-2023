import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

import Profile from './views/Profile'

import store from './store'
Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/my',
            name: 'my_tweets',
            component: Home,
            beforeEnter: (to, from, next) => {
                if (store.getters.get_auth) {
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/my-follow',
            name: 'my_follow_tweets',
            component: Home,
            beforeEnter: (to, from, next) => {
                if (store.getters.get_auth) {
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/exhibition',
            name: 'exhibition',
            component: Home,
            beforeEnter: (to, from, next) => {
                if (store.getters.get_auth) {
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile,
            beforeEnter: (to, from, next) => {
                if (store.getters.get_auth) {
                    next()
                } else {
                    next({name: 'home'})
                }
            }
        },
    ]
})

