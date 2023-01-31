<template>
  <h1>Выбор услуги</h1>
  <v-form @submit.prevent class="my-1">
    <v-row>
      <v-col class="mx-auto">
         <v-select
             v-model="services.service"
            :items="service_types"
            item-text="name"
            item-value="id"
            name="Услуга"
            label="Выберите услугу"/>
        <v-select
            v-model="services.req"
            :items="client_selector"
            label="Заявка"
            class="input"
            type="number"/>
        <v-text-field
            v-model="services.total_cost"
            label="Цена"
            class="input"
            type="number"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createSerivce">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkServices">Список услуг</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline"  rounded="lg" @click="goHome">Назад</v-btn></div>

      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from "axios"
export default {
  name: "RequestForm",
  data: () => ({
      services: {
        service: '',
        req: '',
        total_cost: '',
      },
      requests: [],
    client_selector: ['1', '2', '3'],
    service_types: ['Реклама в соц.сетях', 'Реклама на улице'],
    }),

  methods: {
    createSerivce() {
      axios.post('http://127.0.0.1:8000/chosenservices/create/', {
        service: this.services.service,
        req: this.services.req,
        total_cost: this.services.total_cost,
      })
    },
    async GetServices () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/services/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.clients = response.data
        return response.data
      } catch (e) {
        console.error('ERROR')
      }
    },

    async GetRequests () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/request/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.requests = response.data
        return response.data
      } catch (e) {
        console.error('ERROR')
      }
    },

    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkServices() {
      this.$router.push({ name: 'services'})
    },
  },
  mounted() {
    this.createSerivce()
    this.GetServices()
    this.GetRequests()

    },
}

</script>

<style scoped>
</style>


