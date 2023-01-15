<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/clients")' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить гостя</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Никнейм"
            v-model="addForm.username"
          />
          <v-text-field
            label="Пароль"
            v-model="addForm.password"
          />
          <v-text-field
            label="Паспорт"
            v-model="addForm.passport"
          />
          <v-text-field
            label="Фамилия"
            v-model="addForm.last_name"
          />
          <v-text-field
            label="Имя"
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Отчество"
            v-model="addForm.patronymic"
          />
          <v-text-field
            label="Родной город"
            v-model="addForm.town"
          />
          <v-text-field
            label="Номер"
            v-model="addForm.number"
          />
          <v-btn color="secondary" @click="add">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'ClientsCreate',
  data: () => ({
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
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/hotels/clients/create/', this.addForm)
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

<style scoped>
  v-date-picker {
          background-color: red;
  }
</style>