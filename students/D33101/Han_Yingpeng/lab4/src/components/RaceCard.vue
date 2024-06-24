<template>
  <v-card
    class="mx-auto"
    max-width="400"
    :to="clickable ? `races/${data.id}` : ''"
    :link="clickable"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://i.ytimg.com/vi/L9ZYdShgtPE/maxresdefault.jpg"
    >
      <v-card-title style="background-color: rgba(0, 0, 0, 0.6)">
        {{ data.name }}
      </v-card-title>
    </v-img>
    <v-card-subtitle class="pb-0">
      {{ data.description }}
    </v-card-subtitle>
    <v-card-text class="text--primary mt-2">
      <div><b>Start time:</b> {{ data.start_time || "---" }}</div>
      <div><b>Start time:</b> {{ data.finish_time || "---" }}</div>
      <div><b>Winner:</b> {{ data.winner ? data.winner.name : "---" }}</div>
    </v-card-text>
    <div v-if="showRiders">
      <v-divider class="mx-4"></v-divider>
      <v-card-text class="text--primary pb-0 text-left">
        Participants:
      </v-card-text>
      <ul>
        <li v-for="rider in data.riders" :key="rider.id">
          <v-card-text class="text--secondary text-left pt-1 pb-1">
            {{ `${rider.name} - ${rider.team.name}` }}
          </v-card-text>
        </li>
      </ul>
      <v-divider class="mx-4 mt-3"></v-divider>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        text
        :color="
          data.start_time && !data.winner
            ? 'green'
            : !data.start_time && !data.winner
            ? 'red'
            : 'blue'
        "
      >
        Status:
        {{
          data.start_time && !data.winner
            ? "In Progress"
            : !data.start_time && !data.winner
            ? "Not started"
            : "Finished"
        }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      default: () => ({}),
    },
    clickable: {
      type: Boolean,
      default: true,
    },
    showRiders: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped></style>
