<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/employees")' elevation="4">Отмена</v-btn>
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
            label="Фамилия"
            item-text='this.employee_cur.last_name'
            v-model="addForm.last_name"
          />
          <v-text-field
            label="Имя"
            item-text='this.employee_cur.first_name'
            v-model="addForm.first_name"
          />
          <v-text-field
            label="Отчество"
            item-text='this.employee_cur.patronymic'
            v-model="addForm.patronymic"
          />
          <v-text-field
            label="Этаж"
            item-text='this.employee_cur.floor'
            v-model="addForm.floor"
          />
          <v-text-field
            label="День"
            item-text='this.employee_cur.day'
            v-model="addForm.day"
          />
          <v-btn color="secondary" @click="update">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'EmployeesUpdate',
  data: () => ({
    emp_id: 0,
    employee_cur: {
      last_name: '',
      first_name: '',
      patronymic: '',
      floor: '',
      day: ''
    },
    addForm: {
      last_name: '',
      first_name: '',
      patronymic: '',
      floor: '',
      day: ''
    }
  }),
  created () {
    this.emp_id = this.$route.params.emp_id
    this.axios
      .get(`http://127.0.0.1:8000/hotels/employees/update/${this.emp_id}/`)
      .then((res) => {
        console.log(res)
        this.employee_cur = res.data
        this.addForm.last_name = this.employee_cur.last_name
        this.addForm.first_name = this.employee_cur.first_name
        this.addForm.patronymic = this.employee_cur.patronymic
        this.addForm.floor = this.employee_cur.floor
        this.addForm.day = this.employee_cur.day
        console.log(this.employee_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/hotels/employees/update/${this.emp_id}/`, this.addForm)
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