<template>
    <div>
      <div>
        <v-app-bar color="#653d19" dense dark>
          <v-btn icon @click="goHome">
            <v-icon>mdi-home</v-icon>
          </v-btn>
          <v-toolbar-title>Clinic</v-toolbar-title>
          <v-btn class="ma-2" outlined color="white" @click="goDoctorlist">Лист авторов</v-btn>
          <v-spacer></v-spacer>
          <v-btn icon @click="goProfile">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-btn icon @click="logout">
            <v-icon>mdi-exit-to-app</v-icon>
          </v-btn>
        </v-app-bar>
      </div>
      <div class="block-content">
        <v-card width="600" color="#fff8f2">
          <h1>Отзыв</h1>
            <v-container fluid>
              <v-textarea name="input-7-1" filled label="Текст отзыва" auto-grow v-model="text" type="text"></v-textarea>
            </v-container>
            <div class="sign-block">
              <v-col class="d-flex" cols="12" sm="6">
                <v-select v-model="rating" :items="rateNumber" label="Поставьте оценку" dense solo></v-select>
              </v-col>
              <v-btn class="button" color="primary" v-on:click="sendReview">Отправить</v-btn>
            </div>
        </v-card>
      </div>
    </div>
  </template>
  
  <script>
  import $ from 'jquery'
  export default {
    name: 'Review',
    head () {
      return { title: 'Title' }
    },
    data () {
      return {
        text: '',
        rating: '',
        rateNumber: ['1', '2', '3', '4', '5']
      }
    },
    created () {
      this.creationId = this.$route.params.creationId
      if (this.$route.params.reviewId !== undefined) {
        this.loadReview()
      } else {
        if (this.creationId === undefined) {
          this.$router.push({ name: 'Home' })
        }
      }
      $.ajaxSetup({
        headers: { authorization: 'Token ' + sessionStorage.getItem('auth_token') }
      })
    },
    methods: {
      sendReview () {
        if (this.$route.params.reviewId !== undefined) {
          $.ajax({
            url: 'http://127.0.0.1:8000/api/reviews/' + this.$route.params.reviewId + '/update/',
            type: 'PATCH',
            data: {
              text: this.text,
              rating: this.rating,
              creation: this.creationId
            },
            success: (response) => {
              alert('Отзыв обновлен')
              this.$router.push({ name: 'Home' })
            },
            error: (response) => {
              alert(response)
            }
          })
        } else {
          $.ajax({
            url: 'http://127.0.0.1:8000/api/reviews/create/',
            type: 'POST',
            data: {
              text: this.text,
              rating: this.rating,
              creation: this.creationId
            },
            success: (response) => {
              alert('Спасибо за отзыв')
              console.log(response)
              this.$router.push({ name: 'Home' })
            },
            error: (response) => {
              alert(response)
            }
          })
        }
      },
      loadReview () {
        $.ajax({
          url: 'http://127.0.0.1:8000/api/reviews/' + this.$route.params.reviewId + '/',
          type: 'GET',
          success: (response) => {
            this.creationId = response.creation
            this.text = response.text
            this.rating = response.rating
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
      goProfile () {
        this.$router.push({ name: 'Profile' })
      },
      logout () {
        sessionStorage.removeItem('auth_token')
        window.location = '/home'
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
.sign-block {
    display: flex;
    justify-content: space-around;
}
.button {
    padding: 12px;
    margin: 12px;
}
</style>