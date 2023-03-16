<template>
<div>
 <div  v-for="flight in flights" :key="flight.id">
   <div><strong>Номер рейса:</strong> {{ flight.number }}</div>
   <div><strong>Расстояние полета:</strong> {{ flight.distance }}</div>
   <div><strong>Пункт вылета:</strong> {{ flight.departure }}</div>
   <div><strong>Пункт назначения:</strong> {{ flight.arrival }}</div>
   <div><strong>Количество совершенных рейсов:</strong> {{ flight.completed }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: { // «Props» -- это специальное ключевое слово, обозначающее свойства . Его можно зарегистрировать в компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
   flights: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>

</style>