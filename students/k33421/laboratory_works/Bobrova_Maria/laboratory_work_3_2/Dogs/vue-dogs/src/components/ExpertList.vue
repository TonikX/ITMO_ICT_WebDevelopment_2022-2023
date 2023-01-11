<template>
<div>
 <div  v-for="expert in experts" :key="expert.id"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div><strong>Имя:</strong> {{ expert.name }}</div>
   <div><strong>Фамилия:</strong> {{ expert.last_name }}</div>
   <div><strong>Клуб:</strong> {{ expert.club }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: { // «Props» -- это специальное ключевое слово, обозначающее свойства . Его можно зарегистрировать в компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
   experts: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>

</style>