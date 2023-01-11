import Hello from "@/components/Hello.vue";
import {createRouter, createWebHistory} from "vue-router";

const routes = [  // массив с роутами
   // отдельный роут:
   {
       path: '/hi', // конкретный url-адрес
       component: Hello // Ссылка на компонент
   },
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router // экспортируем сконфигурированный роутер
