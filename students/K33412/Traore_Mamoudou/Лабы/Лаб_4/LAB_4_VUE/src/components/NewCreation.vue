<template>
    <div>
      <div>
        <v-app-bar color="#653d19" dense dark>
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
      <div class="block-content">
        <v-card width="700" color="#fff8f2">
          <div class="label">Произведение</div>
          <form>
            <v-text-field class="input" v-model="name" type="text" label="Имя"></v-text-field>
            <v-container fluid>
              <v-textarea name="input-7-1" filled label="Описание произведения" auto-grow v-model="description"
                          type="text"></v-textarea>
            </v-container>
            <div class="sign-block">
              <v-col class="sign-block">
                <v-select class="select-line" v-model="type" :items="typeTips" label="Тип произведения" dense solo></v-select>
                <v-select class="select-line" v-model="creator" :items="doctors" item-text="name" item-value="id" label="Автор" dense solo></v-select>
                <v-btn class="select-line" color="primary" @click="newCreation">Сохранить</v-btn>
              </v-col>
            </div>
          </form>
        </v-card>
      </div>
    </div>
</template>
  
<script>
  import $ from 'jquery'
  export default {
    name: 'NewCreation',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        name: '',
        description: '',
        creator: '',
        type: '',
        doctors: '',
        typeTips: ['Изобразительное искусство', 'Кино', 'Литература', 'Музыка']
      }
    },
    created () {
      if (this.$route.params.creationId !== undefined) {
        this.loadCreation()
      }
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
      this.loaddoctors()
    },
    methods: {
      loaddoctors () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/doctors/',
          type: 'GET',
          success: (response) => {
            this.doctors = response
          },
          error: (response) => {
            alert(response)
          }
        })
      },
      newCreation () {
        if (this.$route.params.creationId !== undefined) {
          $.ajax({
            url: 'http://127.0.0.1:8000/api/creations/' + this.$route.params.creationId + '/update/',
            type: 'PATCH',
            data: {
              name: this.name,
              description: this.description,
              creator: this.creator,
              type: this.type
            },
            success: (response) => {
              alert('Информация о произведении обновлена')
              this.$router.push({ name: 'Home' })
            },
            error: (response) => {
              alert(response)
            }
          })
        } else {
          $.ajax({
            url: 'http://127.0.0.1:8000/api/creations/create/',
            type: 'POST',
            data: {
              name: this.name,
              description: this.description,
              creator: this.creator,
              type: this.type
            },
            success: (response) => {
              alert('Создано произведение')
              console.log(response)
              this.$router.push({ name: 'Home' })
            },
            error: (response) => {
              alert(response)
            }
          })
        }
      },
      loadCreation () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/creations/' + this.$route.params.creationId + '/',
          type: 'GET',
          success: (response) => {
            this.name = response.name
            this.description = response.description
            this.creator = response.creator
            this.type = response.type
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
  .input{
    padding: 12px;
}
  .label {
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    margin-bottom: 10px;
    text-decoration: none;
    font-family: 'Roboto', serif;
    font-style: normal;
    text-align: center;
    transition: .5s linear;
    width: 450px;
    font-size: 40px;
}
  .sign-block {
    display: flex;
    justify-content: space-around;
    padding: 12px;
}
  .select-line{
    margin: 2px;
}
</style>