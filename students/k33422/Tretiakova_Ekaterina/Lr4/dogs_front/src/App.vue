<template>
  <v-app>
    <v-app-bar
      app
      color="#8D6E63"
      dark
    >
      <div class="d-flex align-center"> 
        <v-icon size="46">mdi-dog</v-icon>
        <div class="text-h4">DogsApp</div>
      </div>

      <v-spacer></v-spacer>


    </v-app-bar>

    <v-main>
       <router-view/>
    </v-main>
  </v-app>
</template>

<script>
//import Home from "@/views/Home.vue"

export default {
  name: 'App',

  // components: {
  //   Home
  // },

  data: () => ({
    //
  }),
};
</script>
