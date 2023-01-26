<template>
<div>
    <v-card
      elevation="2"
      outlined
      class="my-2"
    >
  <v-card-text>  
 <div  v-for="participation in participations" :key="participation.id">
   <div><strong>Medal:</strong> {{ participation.medal }}</div>
   <div><strong>Vaccine:</strong> {{ participation.vaccinated }}</div>
   <div><strong>Verified:</strong> {{ participation.dismissed }}</div>
   <div><strong>Grade:</strong> {{ participation.final_grade }}</div>
   <div><strong>Participant:</strong> {{ participation.participant }}</div>
   <div><strong>Ring:</strong> {{ participation.rings }}</div><br>
 </div>
  </v-card-text>
    </v-card>
</div>
</template>

<script>
export default {
 props: {
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