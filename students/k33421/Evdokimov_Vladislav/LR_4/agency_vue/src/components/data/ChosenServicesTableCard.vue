<template>
  <v-data-table
    :headers="headers"
    :items="chosenservices"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Выбранные услуги</v-toolbar-title>
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
              Добавить выбранные услуги
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ chosenservicesForm }}</span>
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
                      :items=services
                      item-text="title"
                      item-value="id"
                      label="Услуга"
                      v-model="editedItem.service"
                      :rules="rules.requireds"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      :items=requests
                      item-text="id"
                      item-value="id"
                      label="Заявка"
                      v-model="editedItem.req"
                      :rules="rules.requireds"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.total_cost"
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
            <v-card-title class="headline">Вы уверены, что хотите удалить запись о выбранных услугах?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="DeleteChosenServices">Подтвердить</v-btn>
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
    chosenservices: [],
    services: [],
    requests: [],
    rules: {
      required: value => !!value || 'Required.',
      requireds: [(value) => value.length > 0 || 'Required.'],
      counter30: value => value.length <= 30 || 'Max 30 characters'
    },
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: 'ID', value: 'id' },
      { text: 'Услуга', value: 'service' },
      { text: 'Заявка', value: 'req' },
      { text: 'Цена', value: 'total_cost' },
      { text: 'Действия', value: 'actions', sortable: false }
    ],
    editedIndex: -1,
    editedItem: {
      service: 0,
      req: 0,
      total_cost: 0
    },
    defaultItem: {
      service: 0,
      req: 0,
      total_cost: 0
    }
  }),
  computed: {
    chosenservicesForm () {
      return this.editedIndex === -1 ? 'Добавить выбранные услуги' : 'Изменение данных о выбранных услугах'
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
    this.GetChosenServices()
    this.GetServices()
    this.GetRequests()
  },

  methods: {
    async GetChosenServices () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/chosenservices/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.chosenservices = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
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
    async GetRequests () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/request/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.requests = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async CreateChosenServices () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/ad_agency/chosenservices/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async UpdateChosenServices () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://127.0.0.1:8000/ad_agency/chosenservices/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async DeleteChosenServices () {
      this.editedIndex = 1
      this.dialogDelete = true
      try {
        const response = await this.axios
          .delete('http://127.0.0.1:8000/ad_agency/chosenservices/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

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
      this.editedItem.req = parseInt(this.editedItem.req.split('-')[0])
      this.editedItem.service = this.services.find(item => item.title === this.editedItem.service).id
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
        this.UpdateChosenServices()
      } else {
        this.CreateChosenServices()
      }
      this.close()
    }
  }
}
</script>
