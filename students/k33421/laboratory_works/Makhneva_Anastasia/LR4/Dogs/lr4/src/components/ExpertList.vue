<template>
<div>
      <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <v-card-text>
 <div  v-for="expert in experts" :key="expert.id"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div><strong>имя:</strong> {{ expert.name }}</div>
   <div><strong>фамилия:</strong> {{ expert.last_name }}</div>
   <div><strong>клуб:</strong> {{ expert.club }}</div><br>
 </div>
    </v-card-text>
      </v-card>
</div>
</template>

<script>
export default {
 props: { // «Props» -- это специальное ключевое слово, обозначающее свойства. Его можно зарегистрировать в компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
   experts: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>
/* eslint-disable */
</style>