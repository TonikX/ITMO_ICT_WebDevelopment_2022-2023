<template>
<div>
  <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <v-card-text>
 <div  v-for="participant in participants" :key="participant.id"> 
   <div><strong>кличка:</strong> {{ participant.name }}</div>
   <div><strong>порода:</strong> {{ participant.breed }}</div>
   <div><strong>возраст:</strong> {{ participant.age }}</div>
   <div><strong>родословная:</strong> {{ participant.family }}</div>
   <div><strong>данные хозяина:</strong> {{ participant.owner_data }}</div>
   <div><strong>клуб:</strong> {{ participant.club }}</div><br>
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