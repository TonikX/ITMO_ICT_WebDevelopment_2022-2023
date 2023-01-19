<template>
  <v-app :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }" :dark="true">
    <v-container>
      <h3 class="headline">Races scores!</h3>
      <v-row class="mt-4">
        <v-col v-for="race in races" :key="race.id" cols="12" sm="4">
          <race-card :data="race"></race-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axiosInstance from "@/utils/axios";
import RaceCard from "@/components/RaceCard";

export default {
  name: "RacesList",
  components: {
    RaceCard,
  },
  data() {
    return {
      races: [],
    };
  },
  mounted() {
    axiosInstance
      .get("/api/races")
      .then((response) => {
        if (response.status === 200) this.races = response.data;
        else throw new Error("Error");
      })
      .catch((err) => {
        alert(`Error loading the races, try again - ${err}`);
      });
  },
};
</script>

<style scoped></style>
