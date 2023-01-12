<template>
    <div>
      <div class="navbar">
        <v-app-bar dense dark>
          <v-btn icon @click="goHome">
            <v-icon>mdi-home</v-icon>
          </v-btn>
          <v-toolbar-title>Clinic</v-toolbar-title>
          <v-btn class="ma-2" outlined color="white" @click="goDoctorlist">Лист врачей</v-btn>
          <v-spacer></v-spacer>
          <v-btn icon @click="logout">
            <v-icon>mdi-exit-to-app</v-icon>
          </v-btn>
        </v-app-bar>
      </div>
      <div>
        <div>
            <p>{{ data_.Doctor.last_name }} {{ data_.Doctor.first_name }} {{ data_.Doctor.middle_name }}</p>
        </div>
        <div>
          <h1>Расписание</h1>
            <v-simple-table>
              <thead>
                <th class="text-center">
                  Понедельник
                </th>
                <th class="text-center">
                  Вторник
                </th>
                <th class="text-center">
                  Среда
                </th>
                <th class="text-center">
                  Четверг
                </th>
                <th class="text-center">
                  Пятница
                </th>
                <th class="text-center">
                  Суббота
                </th>
                <th class="text-center">
                  Воскресенье
                </th>
              </thead>
              <tbody>
              <tr>
                  <td v-for="week_day in week_days" v-bind:key="week_day">
                    <router-link :to="{ name:'Cabinet', params:{ id: data_.Timetable[week_day].cabinet.id } }">
                      <div v-if="data_.Timetable[week_day].cabinet.number">
                        Кабинет: {{ data_.Timetable[week_day].cabinet.number }}
                      </div>
                    </router-link>
                    <div v-if="!data_.Timetable[week_day].cabinet.number">
                      Выходной
                    </div>
                  </td>
              </tr>
              </tbody>
            </v-simple-table>
        </div>
      </div>
    </div>
</template>
  
<script>
  import $ from 'jquery'
  export default {
    name: 'Profile',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        data_: ''
      }
    },
    created () {
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.loadData()
    },
    methods: {
      loadData () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/profile',
          type: 'GET',
          success: (response) => {
            this.data_ = response
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      goDoctorlist () {
        this.$router.push({ name: 'Doctorlist' })
      },
      goHome () {
        this.$router.push({ name: 'Home' })
      },
      logout () {
        sessionStorage.removeItem('auth_token')
        window.location = '/'
      }
    }
 }
</script>
  
<style scoped>
.block-content {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FFFFFF; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
}
.v-data-table {
    line-height: 2;
    width: 800px;
    max-width: 100%;
}
.button-card {
    margin: auto;
    text-align: center;
    display: block;
}
.button {
    margin: 8px;
  }
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
}
</style>