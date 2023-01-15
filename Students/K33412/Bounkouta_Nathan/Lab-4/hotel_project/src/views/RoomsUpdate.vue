<template>
  <div class="add">
    <div style="text-align: right;">
      <v-btn color=accent @click='$router.push("/rooms")' elevation="4">Отмена</v-btn>
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
            label="Номер комнаты"
            item-text='this.room_cur.number'
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
            item-text='this.room_cur.phone'
            v-model="addForm.phone"
          />
          <v-text-field
            label="Цена"
            item-text='this.room_cur.price'
            v-model="addForm.price"
          />
          <v-text-field
            label="Этаж"
            item-text='this.room_cur.floor'
            v-model="addForm.floor"
          />
          <v-btn color="secondary" @click="update">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  name: 'RoomsUpdate',
  data: () => ({
    room_id: 0,
    types: ['single', 'double', 'triple'],
    room_cur: {
      number: '',
      type: '',
      phone: '',
      price: '',
      floor: ''
    },
    addForm: {
      number: '',
      type: '',
      phone: '',
      price: '',
      floor: ''
    }
  }),
  created () {
    this.room_id = this.$route.params.room_id
    this.axios
      .get(`http://127.0.0.1:8000/hotels/rooms/update/${this.room_id}/`)
      .then((res) => {
        console.log(res)
        this.room_cur = res.data
        this.addForm.number = this.room_cur.number
        this.addForm.type = this.room_cur.type
        this.addForm.phone = this.room_cur.phone
        this.addForm.price = this.room_cur.price
        this.addForm.floor = this.room_cur.floor
        console.log(this.room_cur)
      })
  },
  methods: {
    async update () {
      await this.axios
        .put(`http://127.0.0.1:8000/hotels/rooms/update/${this.room_id}/`, this.addForm)
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