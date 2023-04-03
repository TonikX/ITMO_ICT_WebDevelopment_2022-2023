<template>
  <div>
    <br><br>
    <b-table striped hover :items="cleaners" :fields="fields" caption-top>
      <template #table-caption>Все служащие</template>
    </b-table>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Cleaners',
  data () {
    return {
      fields: [
        { key: 'id_cleaner', label: '' },
        { key: 'last_name_cleaner', label: 'Фамилия' }, 
        { key: 'first_name_cleaner', label: 'Имя' }, 
        { key: 'patronymic_cleaner', label: 'Отчество' },
      ],
      cleaners: '',
    }
  },
  created() {
    $.ajaxSetup({
                    headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                });
    this.loadCleaners()
  },
  methods: {
            loadCleaners() {
                $.ajax({
                  url: 'http://127.0.0.1:8000/cleaners/',
                  type: "GET",
                  success: (response) => {
                    this.cleaners = response.data.data
                  },
                })
            },
        },
}
</script>


<style scoped>

</style>