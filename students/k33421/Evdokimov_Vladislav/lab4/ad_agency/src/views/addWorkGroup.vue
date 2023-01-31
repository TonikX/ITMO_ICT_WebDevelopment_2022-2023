<template>
  <h1>Выбор рабочей группы</h1>
  <v-form @submit.prevent class="my-1">
    <v-row>
      <v-col class="mx-auto">
         <v-select
             v-model="WorkGroup.req"
            :items="request_types"
            item-text="name"
            item-value="id"
            name="Выберите заявку"
            label="Выберите заявку"/>
        <v-select
            v-model="WorkGroup.staff"
            :items="staff_types"
            label="Выберите группу"
            class="input"/>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="createWorkGroup">Создать</v-btn></div><br>
        <div class="d-flex align-center flex-column flex-md-row">
          <v-btn variant="outlined" color="outline" rounded="lg" @click="checkStaff">Список сотрудников</v-btn></div><br>
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
      WorkGroup: {
        req: '',
        staff: '',
       },
      staff_types: ['Трифан Андрей Жукович', 'Нефёдов Роман Александрович', 'Трин Кирилл Петрович'],
      request_types: ['1', '2', '3'],
      staffs: [],
      requests: [],
    }),

  methods: {
    createWorkGroup() {
      axios.post('http://127.0.0.1:8000/workgroup/create/', {
        req: this.WorkGroup.req,
        staff: this.WorkGroup.staff
      })
    },
    async GetStaff () {
      try {
        const response = await this.axios
            .get('http://127.0.0.1:8000/staff/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.staffs = response.data
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
    checkStaff() {
      this.$router.push({ name: 'staffList'})
    },
  },
  mounted() {
    this.createWorkGroup()
    this.GetStaff()
    this.GetRequests()

    },
}

</script>

<style scoped>
</style>


