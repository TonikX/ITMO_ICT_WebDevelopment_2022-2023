<template>
<div>
 <div  v-for="participation in participations" :key="participation.id"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
   <div><strong>Медаль:</strong> {{ participation.medal }}</div>
   <div><strong>Вакцинация:</strong> {{ participation.vaccinated }}</div>
   <div><strong>Допуск:</strong> {{ participation.dismissed }}</div>
   <div><strong>Оценка:</strong> {{ participation.final_grade }}</div>
   <div><strong>Участник:</strong> {{ participation.participant }}</div>
   <div><strong>Ринг:</strong> {{ participation.rings }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: { // «Props» -- это специальное ключевое слово, обозначающее свойства . Его можно зарегистрировать в компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
   participations: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>
/* eslint-disable */
</style>