<template>
<div>
  <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <v-card-text>
 <div  v-for="participant in participants" :key="participant.id"> 
   <div><strong>Name:</strong> {{ participant.name }}</div>
   <div><strong>Breed:</strong> {{ participant.breed }}</div>
   <div><strong>Age:</strong> {{ participant.age }}</div>
   <div><strong>Pedigree:</strong> {{ participant.family }}</div>
   <div><strong>Owner info:</strong> {{ participant.owner_data }}</div>
   <div><strong>Club:</strong> {{ participant.club }}</div><br>
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