<template>
  <div>
    <br><br>
    <b-table striped hover :items="clients" :fields="fields" caption-top>
      <template #table-caption>Все клиенты</template>
    </b-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Clients',
  data () {
    return {
      fields: [
        { key: 'passport', label: '' },
        { key: 'last_name_client', label: 'Фамилия' }, 
        { key: 'first_name_client', label: 'Имя' }, 
        { key: 'patronymic_client', label: 'Отчество' }, 
        { key: 'city', label: 'Город' }, 
      ],
      clients: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadClients()
  },
  methods: {
            loadClients() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/clients/',
                  type: "GET",
                  success: (response) => {
                    this.clients = response.data.data
                  },
                })
            },
        },
}
</script>


<style scoped>

</style>