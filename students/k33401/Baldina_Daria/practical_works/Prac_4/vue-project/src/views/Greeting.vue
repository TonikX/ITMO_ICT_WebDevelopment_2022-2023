<template>
    <section>
      <GreetingCard :username="savedUsername" />
      <h2>Это простой проект на Vue.</h2>
    </section>

    <form @submit.prevent="submitUsername">
     <label for="username">
       Введите своё имя:
     </label>
 
     <input
       v-model="username"
       id="username"
       name="username"
       type="text"
       placeholder="Иван Иванов"
     />

     <h3>Варианты приветствий:</h3>
 
    <div class="greeting-list-wrapper">
    <GreetingList :greetings="greetings" />
 </div>

   </form>

</template>

<script>
import GreetingCard from '../components/GreetingCard.vue'
import GreetingList from '../components/GreetingList.vue'
 
export default {
    name: 'GreetingView',
 
    components: {
        GreetingCard,
        GreetingList
    },

    data: () => ({
        username: '',
        savedUsername: '',
        greetings: [
                    { id: 1, text: 'Привет' },
                    { id: 2, text: 'Hello' },
                    { id: 3, text: 'Hola' }
        ]

 }),

    methods: {
        submitUsername () {
     // сохраним username в localStorage
        localStorage.setItem('username', this.username)
 
     // сохраним его в отдельную переменную,
     // для дальнейшей передачи в компоненту
     // GreetingCard
        this.savedUsername = this.username
 
     // очистим форму
        this.$refs.form.reset()
    }
 },
 
    created () {
   // если localStorage содержит значение по ключу
   // username, то запишем его в наши переменные
        if (localStorage.getItem('username')) {
            this.savedUsername = localStorage.getItem('username')
 
             this.username = this.savedUsername
        }
    }
}

</script>
 
<style>
.greeting-list-wrapper {
 display: flex;
}
 
.greeting-list-wrapper .greeting-list {
 margin: auto
}
</style>
