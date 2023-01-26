<template>
  <v-footer padless>
    <v-col class="text-center"  cols="12">
      {{ new Date().getFullYear() }} — <strong>Билеты в любую сторону</strong>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  name: "Foot",
  data: () => ({}),
};
</script>