<template>
  <div class="edit">
    <h2>Edit profile</h2>
    <v-form
        @submit.prevent="saveChanges"
        ref="changeForm"
        class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
              label="Имя"
              v-model="changeForm.first_name"
              name="first_name"/>

          <v-text-field
              label="Фамилия"
              v-model="changeForm.last_name"
              name="last_name"/>

          <v-text-field
              label="Телефон"
              v-model="changeForm.tel"
              name="tel"/>

          <v-btn type="submit" color="#ff6347" dark>Save</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15">
      <router-link to="/show/profile" style="text-decoration: none; color: #ff6347">Back</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'ProfileEdit',

  data: () => ({
    reader_old: Object,
    changeForm: {
      // password: '',
      first_name: '',
      last_name: '',
      tel: '',
    },
  }),

  methods: {
    async saveChanges() {
      for (const [key, value] of Object.entries(this.changeForm)) {
        if (value === '') {
          delete this.changeForm[key]
        }
      }
      try {
        const response = await this.axios
            .patch('http://127.0.0.1:8000/auth/users/me/',
                this.changeForm, {
                  headers: {
                    Authorization: `Token ${sessionStorage.getItem('auth_token')}`
                  }
                })
        console.log(response)
        this.$refs.changeForm.reset()
        await this.$router.push({name: 'profile'})
      } catch (e) {
        console.error(e.message)
      }
    }
  }
}

</script>

<style>
</style>
