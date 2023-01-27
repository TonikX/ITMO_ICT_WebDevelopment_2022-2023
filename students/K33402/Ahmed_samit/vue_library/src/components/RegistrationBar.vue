<template>
        <v-spacer></v-spacer>
        <v-btn v-if="!auth" @click="goLogin()"
            text
          >
            <span class="mr-2">Вход</span>
    </v-btn>
      
    </template>

 <script>
 export default {
  name: 'RegistrationBar',
  methods: {
        goLogin () {
          this.$router.push({ name: 'Login' })
        },
 }
}
 
</script>
    
    <style>
    </style>