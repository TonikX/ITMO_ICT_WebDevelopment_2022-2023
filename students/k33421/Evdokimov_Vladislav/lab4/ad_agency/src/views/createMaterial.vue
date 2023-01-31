<template>
  <h1>Создание материала</h1>
  <v-form @submit.prevent class="my-0">
    <v-row>
      <v-col class="mx-auto">
        <v-text-field
            v-model="materials.title"
            class="input"
            type="text"
            placeholder="Название"/>
        <v-text-field
            v-model="materials.description_material"
            class="input"
            type="text"
            placeholder="Описание"/>
        <v-text-field
            v-model="materials.price"
            class="input"
            type="number"
            placeholder="Цена"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createMaterial">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkMaterials">Список материалов</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline"  rounded="lg" @click="goHome">Назад</v-btn></div>

      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "MaterialForm",
  data () {
    return {
      materials: {
        title: '',
        description_material: '',
        price: '',
      },
    }
  },
  methods: {
    createMaterial() {
      axios.post('http://127.0.0.1:8000/materials/create/', {
        title: this.materials.title,
        description_material: this.materials.description_material,
        price: this.materials.price,
      })
    },
    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkMaterials() {
      this.$router.push({ name: 'materials'})
    }
  }
}
</script>

<style scoped>
</style>