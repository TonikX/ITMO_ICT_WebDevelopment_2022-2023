<template>
  <v-app>
    <v-app-bar
      app
      color="#c25b8e"
      dark
    >
      <div class="d-flex align-center"> 
        <v-icon size="46">mdi-dog-side</v-icon>
        <div class="text-h4">sob@kiRU</div>
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
