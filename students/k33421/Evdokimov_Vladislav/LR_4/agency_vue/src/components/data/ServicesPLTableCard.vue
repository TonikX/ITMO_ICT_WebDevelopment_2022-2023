<template>
  <v-data-table
    :headers="headers"
    :items="services"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Прайс-лист на услуги</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Добавить новую услугу
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ serviceForm }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="editedItem.service_type"
                      :items=service_types
                      item-text="name"
                      item-value="abbr"
                      label="Услуга"
                      :rules="rules.requireds"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.title"
                      label="Описание"
                      :rules="[rules.required, rules.counter50]"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.price"
                      label="Цена"
                      :rules="[rules.required, rules.counter30]"
                      type="number"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Отмена
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Вы уверены, что хотите удалить эту услугу?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="DeleteService">Подтвердить</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data: () => ({
    services: [],
    service_types: [
      { name: 'Размещение рекламы на билбордах', abbr: 'Размещение рекламы на билбордах' },
      { name: 'Размещение рекламы на общественном транспорте', abbr: 'Размещение рекламы на общественном транспорте' },
      { name: 'Размещение рекламы в соц.сетях', abbr: 'Размещение рекламы в соц.сетях' },
      { name: 'Размещение рекламы на улице', abbr: 'Размещение рекламы на улице' }
    ],
    rules: {
      required: value => !!value || 'Required.',
      requireds: [(value) => value.length > 0 || 'Required.'],
      counter20: value => value.length <= 20 || 'Max 20 characters',
      counter30: value => value.length <= 30 || 'Max 30 characters',
      counter50: value => value.length <= 50 || 'Max 50 characters'
    },
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: 'ID', value: 'id' },
      { text: 'Услуга', value: 'service_type' },
      { text: 'Описание', value: 'title' },
      { text: 'Цена', value: 'price' },
      { text: 'Действия', value: 'actions', sortable: false }
    ],
    editedIndex: -1,
    editedItem: {
      service_type: 'у',
      title: '',
      price: 0
    },
    defaultItem: {
      service_type: 'у',
      title: '',
      price: 0
    }
  }),
  computed: {
    serviceForm () {
      return this.editedIndex === -1 ? 'Добавить услугу' : 'Изменение данных об услуге'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },
  created () {
    this.GetServices()
  },

  methods: {
    async GetServices () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/servicespl/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.services = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async CreateService () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/ad_agency/servicespl/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async UpdateService () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://127.0.0.1:8000/ad_agency/servicespl/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async DeleteService () {
      this.editedIndex = 1
      this.dialogDelete = true
      try {
        const response = await this.axios
          .delete('http://127.0.0.1:8000/ad_agency/servicespl/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 204) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = 1
      this.editedItem = Object.assign({}, item)
      this.editedItem.service_type = this.service_types.find(item => item.name === this.editedItem.service_type).abbr
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = 1
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    save () {
      if (this.editedIndex > -1) {
        this.UpdateService()
      } else {
        this.CreateService()
      }
      this.close()
    }
  }
}
</script>
