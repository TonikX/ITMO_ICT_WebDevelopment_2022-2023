<template>
  <v-data-table
    :headers="headers"
    :items="requests"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Заявки</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-text-field
          v-model="filter.status"
          label="Статус"
        ></v-text-field>
        <v-text-field
          v-model="filter.from_date"
          label="Дата обращения с "
          type="date"
        ></v-text-field>
        <v-text-field
          v-model="filter.to_date"
          label="Дата обращения по"
          type="date"
        ></v-text-field>
        <v-text-field
          v-model="filter.legal_entity"
          label="Юр. лицо"
        ></v-text-field>
        <v-btn
          icon
          color="primary"
          @click="GetFiltered">
          <v-icon>mdi-filter</v-icon>
        </v-btn>
        <v-btn
          icon
          color="primary"
          @click="clearFilter">
          <v-icon>mdi-filter-remove</v-icon>
        </v-btn>
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
              Добавить заявку
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ requestsForm }}</span>
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
                      :items=clients
                      item-text="contact_person"
                      item-value="id"
                      label="Клиент"
                      v-model="editedItem.client"
                      :rules="rules.requireds"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      label="Дата обращения"
                      v-model="editedItem.req_date"
                      :rules="rules.required"
                      type="date"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.workload"
                      label="Нагрузка"
                      :rules="[rules.required, rules.counter30]"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.final_price"
                      label="Стоимость"
                      :rules="[rules.required, rules.counter30]"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      :items="status_options"
                      label="Статус"
                      v-model="editedItem.status"
                      :rules="rules.required"
                    ></v-select>
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
            <v-card-title class="headline">Вы уверены, что хотите удалить заявку?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="DeleteRequest">Подтвердить</v-btn>
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
    requests: [],
    clients: [],
    status_options: ['не оплачено', 'оплачено'],
    filter: {
      status: '',
      from_date: '',
      to_date: '',
      legal_entity: ''
    },
    rules: {
      required: value => !!value || 'Required.',
      requireds: [(value) => value.length > 0 || 'Required.'],
      counter20: value => value.length <= 20 || 'Max 20 characters',
      counter30: value => value.length <= 30 || 'Max 30 characters'
    },
    dialog: false,
    dialogDelete: false,
    headers: [
      { text: 'ID', value: 'id' },
      { text: 'Клиент', value: 'client' },
      { text: 'Дата обращения', value: 'req_date' },
      { text: 'Нагрузка', value: 'workload' },
      { text: 'Стоимость', value: 'final_price' },
      { text: 'Статус', value: 'status' },
      { text: 'Действия', value: 'actions', sortable: false }
    ],
    editedIndex: -1,
    editedItem: {
      client: 0,
      req_date: '2023-01-01',
      workload: '',
      final_price: 0,
      status: 'н'
    },
    defaultItem: {
      client: 0,
      req_date: '2023-01-01',
      workload: '',
      final_price: 0,
      status: 'н'
    }
  }),
  computed: {
    requestsForm () {
      return this.editedIndex === -1 ? 'Добавить заявку' : 'Изменение данных о заявке'
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
    this.GetRequests()
    this.GetClients()
  },

  methods: {
    matchStatus () {
      if (this.editedItem.status === 'не оплачено') {
        this.editedItem.status = 'н'
      } else if (this.editedItem.status === 'оплачено') {
        this.editedItem.status = 'о'
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
    async GetFiltered () {
      let filterUrl
      filterUrl = ''
      if (this.filter.status) {
        filterUrl += 'status=' + this.filter.status
      }
      if (this.filter.legal_entity) {
        if (filterUrl !== '') {
          filterUrl += '&'
        }
        filterUrl += 'legal_entity=' + this.filter.legal_entity
      }
      if (this.filter.from_date) {
        if (filterUrl !== '') {
          filterUrl += '&'
        }
        filterUrl += 'from_date=' + this.filter.from_date
      }
      if (this.filter.to_date) {
        if (filterUrl !== '') {
          filterUrl += '&'
        }
        filterUrl += 'to_date=' + this.filter.to_date
      }

      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/request/' + '?' + filterUrl, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.requests = response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async GetClients () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/client/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.clients = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async CreateRequest () {
      this.matchStatus()
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/ad_agency/request/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async UpdateRequest () {
      this.editedIndex = 1
      this.matchStatus()
      try {
        const response = await this.axios
          .put('http://127.0.0.1:8000/ad_agency/request/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async DeleteRequest () {
      this.editedIndex = 1
      this.dialogDelete = true
      try {
        const response = await this.axios
          .delete('http://127.0.0.1:8000/ad_agency/request/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })

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
        this.UpdateRequest()
      } else {
        this.CreateRequest()
      }
      this.close()
    },
    clearFilter () {
      this.filter = Object.assign({})
      window.location.reload()
    }
  }
}
</script>
