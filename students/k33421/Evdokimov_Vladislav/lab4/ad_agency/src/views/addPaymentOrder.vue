<template>
    <v-app>
  <h1>Создание платёжного поручения</h1>
  <v-form @submit.prevent class="my-1">
    <v-row>
      <v-col class="mx-auto">
         <v-select
            v-model="PaymentOrder.req"
            :items="req_selector"
            item-text="text"
            item-value="id"
            name="Заявка"
            label="Заявка"/>
        <v-select
            v-model="PaymentOrder.client"
            :items="client_selector"
            label="Клиент"
            class="input"/>
        <v-text-field
            v-model="PaymentOrder.pay_date"
            label="Оплатить до"
            class="input"
            type="datetime-local"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createRequest">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkRequests">Список заявок</v-btn></div><br>
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
      PaymentOrder: {
        req: '',
        client: '',
        pay_date: '',
        },
      req_selector: ['1', '2'],
      client_selector: ['ООО "Контик', 'ООО "Панельки"'],
      clients: [],
      requests: [],
    }),

  methods: {
    createPaymentOrder() {
      axios.post('http://127.0.0.1:8000/request/create/', {
        req: this.PaymentOrder.req,
        client: this.PaymentOrder.client,
        pay_date: this.PaymentOrder.pay_date
      })
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
    this.GetRequests()
    this.GetClients()
    this.GetRequests()

    },
}

</script>

<style scoped>
</style>


