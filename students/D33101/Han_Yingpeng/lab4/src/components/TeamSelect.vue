<template>
  <v-select
    v-model="selected"
    :hint="`${selected.id}, ${selected.name}`"
    :items="teams"
    item-text="name"
    item-value="id"
    label="Team"
    persistent-hint
    return-object
    single-line
  ></v-select>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      selected: {},
      teams: [],
    };
  },
  props: {
    selected1: {
      type: Object,
      default: () => ({}),
    },
    mounted() {
      axiosInstance
        .get(`/api/teams`)
        .then((response) => {
          if (response.status === 200) {
            this.teams = response.data;
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the teams, try again - ${err}`);
        });
    },
  },
};
</script>

<style scoped></style>
