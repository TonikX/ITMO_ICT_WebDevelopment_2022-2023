<template>
<div>
 <div  v-for="worker in workers" :key="worker.worker_id">
   <div><strong>Имя:</strong> {{ worker.name }}</div>
   <div><strong>Возраст:</strong> {{ worker.age }}</div>
   <div><strong>Образование:</strong> {{ worker.education }}</div>
   <div><strong>Опыт работы:</strong> {{ worker.work_exp }}</div>
   <div><strong>Серия и номер паспорта:</strong> {{ worker.passport }}</div>
   <div><strong>Должность:</strong> {{ worker.occupation }}</div>
   <div><strong>Доступ к рейсам:</strong> {{ worker.access }}</div>
   <div><strong>Работодатель:</strong> {{ worker.employer }}</div>
   <div><strong>Статус:</strong> {{ worker.status }}</div>
 </div>
</div>
</template>

<script>
export default {
 props: { 
   workers: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>

</style>