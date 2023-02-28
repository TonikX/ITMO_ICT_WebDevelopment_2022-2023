<template>
    <section>
      <v-row>
        <v-col cols="6" class="mx-auto">
          <epic-item-card
            v-for="epicItem in epicItems"
            :key="epicItem.identifier"
            :epic-item="epicItem"
            class="my-2"
          />
        </v-col>
      </v-row>
    </section>
   </template>
    
   <script>
   import EpicItemCard from '../components/EpicItemCard.vue'
   import { mapActions, mapState } from 'pinia'
   import useNasaStore from '@/stores/nasa'
//    const apiKey = 'pv7mgIb4MCWKU5a8q0Zm8phM3KZiCaKdOXA0Hmth'
//    const apiUrl = 'https://api.nasa.gov/EPIC'
    
   export default {
    components: { EpicItemCard },
    name: 'EpicView',

    computed: {
    ...mapState(useNasaStore, ['photos'])
    },
    methods: {
    ...mapActions(useNasaStore, ['loadPhoto']),
   }, 
    data: () => ({
      epicItems: []
    }), 

    mounted() {
    this.loadPhoto()
  }
    
}

   </script>
    
   <style>
   </style>
   