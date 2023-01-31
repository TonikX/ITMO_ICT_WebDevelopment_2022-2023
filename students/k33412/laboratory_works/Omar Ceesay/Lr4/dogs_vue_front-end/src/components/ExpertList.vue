<template>
  <div>
    <v-card
        elevation="2"
        outlined
        class="my-2"
    >
      <v-card-text>
        <div v-for="expert in experts" :key="expert.id">
          <!-- v-for - directive to display a list of elements based on an array. -->
          <div><strong>name:</strong> {{ expert.name }}</div>
          <div><strong>lastname:</strong> {{ expert.last_name }}</div>
          <div><strong>club:</strong> {{ expert.club }}</div>
          <br>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: { // «Props» -- is a special keyword denoting properties. It can be registered with a component to pass data from a parent component to one of its child components.
    experts: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
/* eslint-disable */
</style>
