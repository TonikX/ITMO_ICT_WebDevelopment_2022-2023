<template>
<div>
  <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <v-card-text>
 <div  v-for="participant in participants" :key="participant.id"> 
   <div><strong>Кличка:</strong> {{ participant.name }}</div>
   <div><strong>Порода:</strong> {{ participant.breed }}</div>
   <div><strong>Возраст:</strong> {{ participant.age }}</div>
   <div><strong>Родословная:</strong> {{ participant.family }}</div>
   <div><strong>Данные хозяина:</strong> {{ participant.owner_data }}</div>
   <div><strong>Клуб:</strong> {{ participant.club }}</div><br>
 </div>
    </v-card-text>
  </v-card>
</div>
</template>

<script>
export default {
 props: { 
   participants: {
     type: Array,
     required: true
   }
 }
}
</script>

<style scoped>

</style>