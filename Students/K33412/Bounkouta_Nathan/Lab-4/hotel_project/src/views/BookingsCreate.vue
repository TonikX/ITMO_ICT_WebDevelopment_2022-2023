<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.go(-1)' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить бронь 🕒</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Комната"
            v-model="addForm.room"
            :items="rooms"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="option in rooms" :key="option.id">
              {{ option.label }}
            </option>
          </v-select>
          <v-select
            label="Гость"
            v-model="addForm.client"
            :items="clients"
            item-text="label"
            item-value="code"
            :reduce="option => option.code">
            <option v-for="option in clients" :key="option.id">
              {{ option.label }}
            </option>
          </v-select>
          <div>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              no-title
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="addForm.check_in"
                  label="Дата заселения"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="addForm.check_in"
                :active-picker.sync="activePicker"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </div>
          <div>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              no-title
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="addForm.check_out"
                  label="Дата выселения"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="addForm.check_out"
                :active-picker.sync="activePicker"
                @change="save"
              ></v-date-picker>
            </v-menu>
          </div>
          <v-btn color="secondary" @click="create">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'BookingsCreate',
  data: () => ({
    rooms: [],
    clients: [],
    addForm: {
      room: '',
      client: '',
      check_in: '',
      check_out: ''
    }
  }),
  async created () {
    await this.axios
      .get('http://127.0.0.1:8000/hotels/clients/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = `${data[i].last_name} ${data[i].first_name}`
          const id = data[i].id
          this.clients.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/hotels/rooms/')
      .then((res) => {
        const data = res.data
        for (let i = 0; i < res.data.length; i++) {
          const label = data[i].number
          const id = data[i].id
          this.rooms.push({ label: label, code: id })
        }
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    async create () {
      await this.axios
        .post('http://127.0.0.1:8000/hotels/bookings/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
        })
        .catch((error) => {
          console.log(error)
        })
      await this.$router.push('/bookings')
    }
  }
}
</script>