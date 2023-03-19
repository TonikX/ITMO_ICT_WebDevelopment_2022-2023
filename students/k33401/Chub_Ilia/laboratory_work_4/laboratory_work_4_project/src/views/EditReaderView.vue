<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <DefaultNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Информация о читателе </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер телефона"
                v-model="form.phone_number"
                name="phone_number"
                placeholder="+79516571701"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Адрес"
                v-model="form.address"
                name="address"
                placeholder="Russia, Saint-Petersburg, Bolshaya Moskovskaya 1-3"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-select
                v-model="form.education"
                :items="educationOptions"
                label="Образование"
                name="education"
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="4" class="mx-auto"></v-col>
            <v-checkbox
              v-model="form.is_has_academic_degree"
              name="is_has_academic_degree"
              :label="'Наличие учёной степени'"
            ></v-checkbox>
          </v-row>

          <v-col cols="5" class="mx-auto">
            <v-btn block color="blue" @click.prevent="saveChanges()"> Обновить</v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
      <br><br>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'EditReaderView',
  components: {BarLayout, DefaultNavigationBar},
  data: () => ({
    reader_old: Object,
    form: {
      phone_number: '',
      address: '',
      education: '',
      is_has_academic_degree: ''
    },
    educationOptions: ['primary', 'secondary', 'higher']
  }),
  created() {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData() {
      const get_user_response_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {Authorization: `Token ${localStorage.auth_token}`}
        })
      const user = get_user_response_response.data
      const get_userreader_request_url = "http://127.0.0.1:8000/library/userreaders/" + user.id
      const get_userreader_response = await axios.get(get_userreader_request_url)
      const userreader = get_userreader_response.data
      const get_reader_request_url = "http://127.0.0.1:8000/library/readers/" + userreader.reader
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data

      this.reader_old = reader
      this.form.phone_number = reader.phone_number
      this.form.address = reader.address
      this.form.education = reader.education
      this.form.is_has_academic_degree = reader.is_has_academic_degree
    },

    async saveChanges() {
      try {
        const patch_reader_request_url = "http://127.0.0.1:8000/library/readers/" + this.reader_old.ticket

        await axios.patch(patch_reader_request_url, this.form)
        await this.$router.push({name: 'Reader'})
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.is_has_academic_degree) {
          alert('Учёная степень: ' + e.response.data.is_has_academic_degree)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          alert(e.message)
        }
      }
    }
  }
}
</script>
