<template>
    <v-app>
  <h1>Создание заявки</h1>
  <v-form @submit.prevent class="my-1">
    <v-row>
      <v-col class="mx-auto">
         <v-select
             v-model="request.client"
            :items="client_selector"
            item-text="text"
            item-value="id"
            name="Клиент"
            label="Клиент"/>
        <v-text-field
            v-model="request.req_date"
            label="Дата создания заявки"
            class="input"
            type="datetime-local"/>
        <v-text-field
            v-model="request.workload"
            label="Нагрузка в ч."
            class="input"
            type="number"/>
        <v-text-field
            v-model="request.start_date"
            label="Начало исполнения"
            class="input"
            type="datetime-local"/>
        <v-text-field
            v-model="request.end_date"
            label="Конец исполнения"
            class="input"
            type="datetime-local"/>
        <v-text-field
            v-model="request.final_price"
            label="Итоговая стоимость"
            class="input"
            type="number"
            placeholder="Стоимость"/>
        <v-select
            v-model="request.status"
            label="Статус"
            :items="status_types"
            placeholder="Статус"/>
        <v-text-field
            v-model="request.payment"
            label="Дата оплаты"
            class="input"
            type="datetime-local"
            placeholder="Дата"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createRequest">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkRequests">Список клиентов</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline"  rounded="lg" @click="goHome">Назад</v-btn></div>

      </v-col>
    </v-row>
  </v-form>
    </v-app>
</template>

<script>
import axios from "axios"
export default {
  name: "RequestForm",
  data: () => ({
      clients: [],
      request: {
        client: '',
        req_date: '',
        workload: '',
        start_date: '',
        end_date: '',
        final_price: '',
        payment: '',
        bank_details: '',
        status: ''
      },
      status_types: ['Не оплачено', 'Оплачено!'],
      client_selector: ['У.П.А-ООО "Контик"', 'ООО "Панельки"'],
    }),

  methods: {
    createRequest() {
      axios.post('http://127.0.0.1:8000/request/create/', {
        client: this.request.client,
        req_date: this.request.req_date,
        workload: this.request.workload,
        start_date: this.request.start_date,
        end_date: this.request.end_date,
        final_price: this.request.final_price,
        payment: this.request.payment,
        bank_details: this.request.bank_details,
        status: this.request.status,
      })
    },
    async GetClients () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/client/')

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.clients = response.data
        return response.data
      } catch (e) {
        console.error('ERROR')
      }
    },

    goHome() {
      this.$router.push({ name: 'homepage'})
    },
    checkRequests() {
      this.$router.push({ name: 'requests'})
    },
  },
  mounted() {
    this.createRequest()
    this.GetClients()
    },
}

</script>

<style scoped>
</style>


