<template>
  <div class="container pt-5 pb-3 text-center">
    <div class="row pb-3">
      <div class="col">
        <h1>Профиль пользователя {{ user.username }}</h1>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-auto">
        <button type="button" class="btn btn-outline-secondary" @click="this.$router.push({name: 'change_password'})">Сменить
          пароль
        </button>
      </div>
      <div class="col-auto">
        <button type="button" class="btn btn-outline-danger" @click="logout">Выйти</button>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery"

export default {
  name: "ProfileUserBlock",
  data() {
    return {
      user: {}
    }
  },
  created() {
    this.loadUser()
  },
  methods: {
    loadUser() {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/me',
        type: "GET",
        success: (response) => {
          this.user = response
        }
      })
    },
    logout() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/logout",
        type: "POST",
        success: () => {
          localStorage.setItem("auth_token", "")
          delete $.ajaxSettings.headers['Authorization']
          this.$router.push({name: "welcome"})
        },
        error: (response) => {
          alert(Object.values(response.responseJSON)[0])
        }
      })
    }
  }
}
</script>
