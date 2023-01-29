<template>
<div>
  <v-card
      elevation="2"
      outlined
      class="my-2"
    >
    <v-card-text>
 <div  v-for="participant in participants" :key="participant.id"> 
   <div><strong>nickname:</strong> {{ participant.name }}</div>
   <div><strong>breed:</strong> {{ participant.breed }}</div>
   <div><strong>age:</strong> {{ participant.age }}</div>
   <div><strong>family:</strong> {{ participant.family }}</div>
   <div><strong>owner data:</strong> {{ participant.owner_data }}</div>
   <div><strong>club:</strong> {{ participant.club }}</div><br>
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