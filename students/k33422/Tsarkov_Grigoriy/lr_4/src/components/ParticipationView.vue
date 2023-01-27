<template>
   <div class="app">
     <h1>Участия</h1>
       <a href="/">Главная</a><br><br>
     <button v-on:click="fetchParticipations">Получить список участий</button> <!-- Кнопка вызывает функцию получения списка данных (функция fetchWarriors объявлена в блоке "methods") -->

     <participation-list
         v-bind:participations="participations"
     > <!-- Встраивание компонента вызывающего список объектов. v-bind - директива служит для так называемой data binding -- привязки данных (данные объявляются в блоке данных data() (см. код ниже)). -->
     </participation-list>
   </div>
</template>

<script>
/* eslint-disable */
import ParticipationList from "./ParticipationList.vue";
import axios from "axios";

export default {
 components: {
   ParticipationList
 },

 data() { // data - это функция, которая возвращает объект с данными
   return {
     participations: [], // Массив данных (передается в компонент WarriorList, получает данные средствами функции fetchWarriors
   }
 },
 methods: { // methods. Это объект, который содержит список Javascript функций, которые должны выполняться в зависимости от того, какие действия производит пользователь.
   async fetchParticipations () { // асинхронная функция для получения данных
     try {
       const response = await axios.get('http://127.0.0.1:8000/participation/?format=json') // Выполнение GET-запроса Backend-серверу. Запрос вернет JSON.
       console.log(response.data)
       this.participations = response.data // Массив данных warriors из блока(функции) data() получает значением результат только-что выполненного запроса
     } catch (e) {
       alert('Ошибка')
     }
   }

 },
 mounted() {
   this.fetchParticipations() // Vue вызывает хук mount(), когда компонент добавляется в DOM.  В данном примере это позволяет вызвать fetchWarriors для получения списка воинов до отрисовки страницы в браузере, благодаря этому страница загружается с уже полученными ранее данными.

 }
}
</script>