<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/employees")' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить сотрудника</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
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
            label="Этаж"
            v-model="addForm.floor"
          />
          <v-text-field
            label="День"
            v-model="addForm.day"
          />
          <v-btn color="secondary" @click="add">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'EmployeesCreate',
  data: () => ({
    addForm: {
      last_name: '',
      first_name: '',
      patronymic: '',
      floor: '',
      day: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/hotels/employees/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/employees/')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>