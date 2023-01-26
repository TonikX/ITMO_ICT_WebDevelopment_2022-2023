<template>
  <v-app>
    <bar-layout>
      <HomePageBar />
    </bar-layout>
    <v-main class = "vh-100" style = "background-color: hsl(0, 0%, 96%);">
      <HomePage />
    </v-main>
  </v-app>
</template>

<script>
import { defineComponent } from "vue";

// Components
import HomePage from "../components/HomePage.vue";
import BarLayout from "@/layouts/BarLayout.vue";
import HomePageBar from '@/components/HomePageBar.vue'

export default defineComponent({
  name: "HomeView",

  components: {
    BarLayout,
    HomePage,
    HomePageBar
  },
  methods: {
        Logout () {
            localStorage.clear()
            this.$router.push({ name: 'Login' })    
        },
        Home () {
            this.$router.push({ name: 'Home' })
            },
        Books () {
            this.$router.push({ name: 'Books' })
            }
        }
});
</script>
