<template>
  <v-container>
    <v-row>
      <h1>Изменение данных пользователя "{{ EditedItem.username }}"</h1>
      <p></p>
    </v-row>
    <v-row>
      <v-text-field
        v-model="EditedItem.first_name"
        label="Имя"
        required
      ></v-text-field>
    </v-row>
    <v-row>
      <v-text-field
        v-model="EditedItem.last_name"
        label="Фамилия"
        required
      ></v-text-field>
    </v-row>
    <v-row>
      <v-text-field
        v-model="EditedItem.tel"
        label="Телефон"
        required
      ></v-text-field>
    </v-row>
    <v-row>
      <v-text-field
        v-model="EditedItem.role"
        label="Роль"
        required
      ></v-text-field>
    </v-row>
    <v-btn
      color="anchor"
      class="mr-4"
      @click="reset"
    >
      Отмена
    </v-btn>
    <v-btn
      color="primary"
      class="mr-4"
      @click="ChangeAccountDetails"
    >
      Сохранить изменения
    </v-btn>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    AccountDetails: [],
    EditedItem: [],
    data: {}
  }),
  created () {
    this.GetAccountDetails()
  },
  methods: {
    async GetAccountDetails () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/auth/users/me/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.AccountDetails = response.data
        this.EditedItem = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async ChangeAccountDetails () {
      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/auth/users/me/', JSON.stringify(this.EditedItem), { headers: { Authorization: 'Token ' + localStorage.getItem('token'), 'Content-Type': 'application/json' } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    reset () {
      this.EditedItem = this.AccountDetails
      window.location.reload()
    }
  }
}
</script>
