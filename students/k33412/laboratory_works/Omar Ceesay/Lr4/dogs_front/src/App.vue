<template>
  <v-app>
    <v-app-bar
        app
        color="$gray-900"
        dark
    >
      <div class="d-flex align-center">
        <!--<img src="@/assets/dogImg.png"/>-->
        <v-icon size="46">mdi-dog-side</v-icon>
        <div class="text-h4">Anual Dog Show</div>
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
