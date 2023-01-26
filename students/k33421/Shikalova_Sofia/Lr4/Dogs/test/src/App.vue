<template>
  <v-app>
    <v-app-bar
      app
      color="#3949AB"
      dark
    >
      <div class="d-flex align-center"> 
        <div class="text-h4">ITMO Dogs</div>
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
