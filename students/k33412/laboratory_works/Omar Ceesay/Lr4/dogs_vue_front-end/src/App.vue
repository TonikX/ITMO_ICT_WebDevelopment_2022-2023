<template>
  <v-app>
    <v-app-bar
      app
      color="$gray-900"
      dark
      dense 
      elevation="6"
    >
      <div class="d-flex align-center"> 
        <!--<img src="@/assets/dogImg.png"/>-->
        <v-icon size="46">mdi-dog-side</v-icon> 
        <v-toolbar-title class="text-uppercase text-h3">Annual Dog Show</v-toolbar-title>
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

  data: () => ({
    //
  }),
};
</script> 


