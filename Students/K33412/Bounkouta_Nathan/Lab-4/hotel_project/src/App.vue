<template>
  <v-app className="grey lighten-4">
    <Navbar/>
    <v-main className="d-flex align-center text-center">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    //
  })
}
</script>
