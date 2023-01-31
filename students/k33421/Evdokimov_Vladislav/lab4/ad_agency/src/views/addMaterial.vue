<template>
  <h1>Выбор материала</h1>
  <v-form @submit.prevent class="my-1">
    <v-row>
      <v-col class="mx-auto">
         <v-select
             v-model="ChosenMaterials.material"
            :items="material_type"
            item-text="name"
            item-value="id"
            name="Материалы"
            label="Выберите материал"/>
        <v-select
            v-model="ChosenMaterials.req"
            :items="request_type"
            label="Выберите заявку"
            class="input"
            type="number"/>
        <v-text-field
            v-model="ChosenMaterials.price"
            label="Цена"
            class="input"
            type="number"/>
        <v-text-field
            v-model="ChosenMaterials.amount"
            label="Количество"
            class="input"
            type="number"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createMaterials">Создать</v-btn></div><br>
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
  name: "MaterialsForm",
  data: () => ({
      ChosenMaterials: {
        material: '',
        req: '',
        total_cost: '',
        amount: '',
        },
      status_types: ['Не оплачено', 'Оплачено!'],
      materials: [],
      request: [],
      material_type: ['Дерево', 'Мультимедиа устройства', 'Холст'],
      request_type: ['1', '2', '3'],
    }),

  methods: {
    createMaterials() {
      axios.post('http://127.0.0.1:8000/chosenmaterials/create/', {
        material: this.ChosenMaterials.material,
        req: this.ChosenMaterials.req,
        total_cost: this.ChosenMaterials.total_cost,
        amount: this.ChosenMaterials.amount,

      })
    },
    async GetMaterials () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/materials/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.materials = response.data
        return response.data
      } catch (e) {
        console.error('ERROR')
      }
    },

    async GetRequest () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/request/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.request = response.data
        return response.data
      } catch (e) {
        console.error('ERROR')
      }
    },

    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkMaterials() {
      this.$router.push({ name: 'materials'})
    },
  },
  mounted() {
    this.createMaterials()
    this.GetMaterials()
    this.GetRequest()
    },
}

</script>

<style scoped>
</style>


