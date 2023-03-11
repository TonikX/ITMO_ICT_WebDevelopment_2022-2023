# Лабораторная работа №4 Галиновский Роман Web-программирование

## Задание

`Сделать клиентскую часть приложение на основе серверного приложения в ЛР3:`

  1. Реализовать утвержденные с преподавателем интерфейсы для взаимодействияи с серверной частью в соответствии с предметной областью.

  2. Реализовать интерфейсы регистрации и авторизации.
    
  3. Реализовать профиль пользователя с возможностью изменения данных в нем.

  4. Реализовать клиентские интерфейсы и настроить взаимодействиее с серверной частью.

## Реализованные интерфейсы
### Начальная страница
#### в случае если не авторизованы, будет такая Home-page
![alt text](https://sun9-66.userapi.com/impg/hQwa6QZwxCkdTYsbK1qaWAgcPrTsCGVyALNkbg/8mnsYLYhdzk.jpg?size=2560x1663&quality=96&sign=5d0ba9cd8d72ba0214177e91b070d280&type=album)
#### Это уже для авторизованных
![alt text](https://sun9-32.userapi.com/impg/7mvpQpUX8QwFGqmHq0K1QXmKNvjOyKiAs2Usbw/qaU8XzYs_Ls.jpg?size=2560x1663&quality=96&sign=14c5a9f3ad92b5315a72a8c1cc9d5857&type=album)
### Авторизация
![alt text](https://sun9-65.userapi.com/impg/qT-yN9ccdB9L4xl_gliel-TaNjjTIzUtHJZdGA/rapYMi4Yn2M.jpg?size=2560x1663&quality=96&sign=7722ccc6bd7858c81927b1e83cf965be&type=album)
### Регистрация
![alt text](https://sun9-8.userapi.com/impg/3QFW_rHfn5xMzIHsSGiCD6muVt8vWCyDCjJWMA/29a9HOjrdt0.jpg?size=2560x1663&quality=96&sign=188c807654a8e56969b303bc6f61b7c1&type=album)
### Профиль
![alt text](https://sun9-57.userapi.com/impg/kp6rtsrGI6M1LQb8QdkVm5bDSmh7NTDzwviXMg/QuWDl2hzBFQ.jpg?size=2560x1663&quality=96&sign=1ec050693aa3b2deb7ae02d5a0603534&type=album)
### Список собак
![alt text](https://sun9-79.userapi.com/impg/y4g2EJFEpXjwodRrSACYUknpw0_8I04Fn-TQzw/24X3VEl0lXY.jpg?size=2560x1663&quality=96&sign=eefb3a6414b121fe5b2dcde8249163c4&type=album)
### Изменение данных о собаке
![alt text](https://sun9-72.userapi.com/impg/WCdi-EDYtgXI1rM2kgDED-sGxtMcjS3IG_sa9w/vqLZjUDWjTk.jpg?size=2560x1663&quality=96&sign=a0216e237388fa1c1ee50d1c1e66091f&type=album)
### Добавление собаки
![alt text](https://sun9-36.userapi.com/impg/_Qi1Uo_fE4t72v_l3I6DID2sk03qjsyKVui4CQ/_ow5O4t8xwc.jpg?size=2560x1663&quality=96&sign=5f3c66be23e7dae225e74b7f7e15af2c&type=album)

`router/index.jsz`
Маршрутизация:
```javascript
import Index from "@/views/Index.vue"
import Login from "@/views/Login.vue"
import Dog from "@/views/Dogs.vue"
import Register from "@/views/Register.vue"
import Profile from "@/views/Profile.vue"
import Registration from "@/views/Registration.vue"
import CreateDog from "@/views/CreateDog.vue"
import ChangeDog from "@/views/ChangeDog.vue"
import CreateRegister from "@/views/CreateRegister.vue"
import ChangeRegister from "@/views/ChangeRegister.vue"
import ProfileChange from "@/views/ProfileChange.vue"
import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter)
const routes = [
  {
    path: "/",
    name: "Index",
    component: Index
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Registration",
    component: Registration
  },
  {
    path: "/dog",
    name: "dogs",
    component: Dog
  },
  {
    path: "/dog_reg",
    name: "Register",
    component: Register
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile
  },
  {
    path: "/dog/create/",
    name: "CreateDog",
    component: CreateDog
  },
  {
    path: "/dog/:id/",
    name: "ChangeDog",
    component: ChangeDog
  },
  {
    path: "/dog_reg/create/",
    name: "CreateRegister",
    component: CreateRegister
  },
  {
    path: "/dog_reg/:id/",
    name: "ChangeRegister",
    component: ChangeRegister
  },
  {
    path: "/profile/change",
    name: "ProfileChange",
    component: ProfileChange
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router


```