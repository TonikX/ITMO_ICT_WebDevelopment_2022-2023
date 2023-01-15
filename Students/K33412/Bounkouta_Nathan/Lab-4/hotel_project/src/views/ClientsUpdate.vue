<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/clients")' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Редактировать</h2>
    <br>
    <v-form
      @submit.prevent="update"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="4" class="mx-auto">
          <v-text-field
            label="Никнейм"
            item-text='this.client_cur.username'
            v-model="addForm.username"
          />
          <v-text-field
            label="Пароль"
            item-text='this.client_cur.password'
            v-model="addForm.password"
          />
          <v-text-field
            label="Паспорт"
            item-text='this.client_cur.passport'
            v-model="addForm.passport"
          />
          <v-text-field
            label="Фамилия"
            item-text='this.client_cur.last_name'
            v-model="addForm.last_name"
          />
          <v-text-field
            label="Имя"
            item-text='this.client_cur.first_name'
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Отчество"
            item-text='this.client_cur.patronymic'
            v-model="addForm.patronymic"
          />
          <v-text-field
            label="Родной город"
            item-text='this.client_cur.town'
            v-model="addForm.town"
          />
          <v-text-field
            label="Номер"
            item-text='this.client_cur.number'
            v-model="addForm.number"
          />
          <v-btn color="secondary" @click="update">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'ClientsUpdate',
  data: () => ({
    client_id: 0,
    client_cur: {
      username: '',
      password: '',
      passport: '',
      last_name: '',
      first_name: '',
      patronymic: '',
      town: '',
      date: '',
      number: ''
    },
    addForm: {
      username: '',
      password: '',
      passport: '',
      last_name: '',
      first_name: '',
      patronymic: '',
      town: '',
      date: '',
      number: ''
    }
  }),
  created () {
    this.client_id = this.$route.params.client_id
    this.axios
      .get(`http://127.0.0.1:8000/hotels/clients/update/${this.client_id}/`)
      .then((res) => {
        console.log(res)
        this.client_cur = res.data
        this.addForm.username = this.client_cur.username
        this.addForm.password = this.client_cur.password
        this.addForm.passport = this.client_cur.passport
        this.addForm.last_name = this.client_cur.last_name
        this.addForm.first_name = this.client_cur.first_name
        this.addForm.patronymic = this.client_cur.patronymic
        this.addForm.town = this.client_cur.town
        this.addForm.date = this.client_cur.date
        this.addForm.number = this.client_cur.number
        console.log(this.client_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/hotels/clients/update/${this.client_id}/`, this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/clients/')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>