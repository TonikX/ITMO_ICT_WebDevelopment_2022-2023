<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/rooms")' elevation="4">Отмена</v-btn>
    </div>
    <h2 class="display-1 font-weight-bold mb-3" style="text-align: center;">Добавить комнату</h2>
    <br>
    <v-form
      @submit.prevent="add"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-text-field
            label="Номер комнаты"
            v-model="addForm.number"
          />
          <v-select
            label="Тип"
            v-model="addForm.type"
            :items="types">
            <option v-for="option in types" :key="option.id">
              {{ option }}
            </option>
          </v-select>
          <v-text-field
            label="Номер телефона"
            v-model="addForm.phone"
          />
          <v-text-field
            label="Цена"
            v-model="addForm.price"
          />
          <v-text-field
            label="Этаж"
            v-model="addForm.floor"
          />
          <v-btn color="secondary" @click="add">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'RoomsCreate',
  data: () => ({
    types: ['single', 'double', 'triple'],
    addForm: {
      number: '',
      type: '',
      phone: '',
      price: '',
      floor: ''
    }
  }),
  methods: {
    async add () {
      await this.axios
        .post('http://127.0.0.1:8000/hotels/rooms/create/', this.addForm)
        .then((res) => {
          console.log(res)
          this.$refs.addForm.reset()
          this.$router.push('/rooms/')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>