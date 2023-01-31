<template>
  <div>
    <v-card
        elevation="2"
        outlined
        class="my-2"
    >
      <v-card-text>
        <div v-for="participation in participations" :key="participation.id">
          <!-- v-for - директива для отображения списка элементов на основе массива. -->
          <div><strong>Medal:</strong> {{ participation.medal }}</div>
          <div><strong>Vaccination:</strong> {{ participation.vaccinated }}</div>
          <div><strong>Dismissed:</strong> {{ participation.dismissed }}</div>
          <div><strong>Grade:</strong> {{ participation.final_grade }}</div>
          <div><strong>participant:</strong> {{ participation.participant }}</div>
          <div><strong>Ring:</strong> {{ participation.rings }}</div>
          <br>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: { // «Props» -- это специальное ключевое слово, обозначающее свойства . Его можно зарегистрировать в компоненте для передачи данных от родительского компонента к одному из его дочерних компонентов.
    participations: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
/* eslint-disable */
</style>
