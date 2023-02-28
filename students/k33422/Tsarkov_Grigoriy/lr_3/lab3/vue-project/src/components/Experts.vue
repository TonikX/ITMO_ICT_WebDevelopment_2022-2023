<template>
   <div class="app">
     <h1>Эксперты</h1>
       <a href="/">Главная</a> |
       <a href="/participation">Участия</a> |
       <a href="/experts">Эксперты</a> |
       <a href="/auth"> Личный кабинет </a> <!--/auth --><br><br>
     <button v-on:click="fetchExperts">Получить список экспертов</button> <!-- Кнопка вызывает функцию получения списка данных (функция fetchWarriors объявлена в блоке "methods") -->

     <expert-list
         v-bind:experts="experts"
     > <!-- Встраивание компонента вызывающего список объектов. v-bind - директива служит для так называемой data binding -- привязки данных (данные объявляются в блоке данных data() (см. код ниже)). -->
     </expert-list>
   </div>
</template>

<script>

import ExpertList from "./ExpertList.vue";
import axios from "axios";

export default {
 components: {
   ExpertList
 },

 data() { // data - это функция, которая возвращает объект с данными
   return {
     experts: [], // Массив данных (передается в компонент WarriorList, получает данные средствами функции fetchWarriors
   }
 },
 methods: { // methods. Это объект, который содержит список Javascript функций, которые должны выполняться в зависимости от того, какие действия производит пользователь.
   async fetchExperts () { // асинхронная функция для получения данных
     try {
       for (let i = 1; i < 3; i++) {
          const response = await axios.get('http://127.0.0.1:8000/experts/' + String(i) + '?format=json') // Выполнение GET-запроса Backend-серверу. Запрос вернет JSON.
          console.log(response.data)
          this.experts.push(response.data)
       }
        // Массив данных warriors из блока(функции) data() получает значением результат только-что выполненного запроса
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchExperts() // Vue вызывает хук mount(), когда компонент добавляется в DOM.  В данном примере это позволяет вызвать fetchWarriors для получения списка воинов до отрисовки страницы в браузере, благодаря этому страница загружается с уже полученными ранее данными.

 }
}
</script>