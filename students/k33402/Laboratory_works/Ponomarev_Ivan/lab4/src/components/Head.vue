<template>
    <nav class="navbar navbar-expand-lg" data-bs-toggle="white">
        <div class="container-fluid justify-content-between">
            <a class="navbar-brand me-2" href="index.html">
                <img src="@/assets/logo.png" alt="Events" width="58" height="58">
              </a>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-tabs mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="/">Главная</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="/">Мероприятия</a>
              </li>
              <li class="nav-item">
                <a class="nav-link " aria-current="page" href="/calendar">
                  Календарь
                </a>
              </li>
            </ul>
          </div>
          <div class="d-flex align-items-center">
            <button v-if="AuthToken==null" type="button" class="btn px-3 btn-dark" data-bs-toggle="modal" data-bs-target="#loginModal" id="login_button">
              Войти
              </button>
            <a v-if="AuthToken!=null" class="profile_button" href="/profile" id="profile_button">
              <img src="@/assets/icon-prof.png">
            </a>
            <button v-if="AuthToken!=null" @click="logOut()" type="button" class="btn px-3 btn-dark m-3" id="logout_button">
              Выйти
              </button>
          </div>
        </div>
      </nav>
      <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
        <div class="modal-dialog" >
          <div class="modal-content" style="border-radius: 2rem;">
            <div class="modal-body">
              <div class="mb-md-2 mt-md-1 pb-5">
                <div class="h-modal d-flex justify-content-between mb-2">
                  <h2 class="fw-bold mb-3 text-uppercase a">вход</h2>
                  <button type="button" class="btn-close  mt-1" data-bs-dismiss="modal" aria-label="Close" id="closeButton" ref="closeButton"></button>
                </div>

                <div class="form-outline form-white mb-4">
                  <label for="username" class="form-label">Введите свой username:</label>
                  <input type="username" class="form-control" id="username" name="username" v-model="username">
                </div>
  
                <div class="form-outline form-white">
                  <label for="password" class="form-label">Введите пароль:</label>
                  <input type="password" class="form-control" id="password" name="password" v-model="password">
                </div>
            </div>
            <div class="modal-footer justify-content-center flex-column">
              <button @click="sign_in(this)" type="submit" class="btn btn-success mb-3">Войти</button>
              <em>Не зарегестрированы?</em>
              <a href="/signup" type="button" class="btn btn-dark">Регистрация</a>
            </div>
          </div>
          </div>
        </div>
      </div>

</template>

<script>
    import { mapActions, mapState } from 'pinia';
    import userStore from '@/store/user_store';
    
    export default {
        name: "Head",

        data(){
          return {
            username: "",
            password: ""
          }
        },

        computed: {
            ...mapState(userStore, ['user']),
            ...mapState(userStore, ['authToken']),
            User() {
                return this.user    
            },
            AuthToken() {
                return this.authToken
            }
        },
        methods: {
            ...mapActions(userStore,['login']),
            ...mapActions(userStore,['logout']),
            ...mapActions(userStore,['get_user']),
            async sign_in() {
                if (!this.username || !this.password) {
                     this.err = 'Error! Enter username and password!'
                        return
                }
              const data = {}
              data["username"]=this.username
              data["password"]=this.password
              try{
                const response = await this.login(data)
                await this.get_user(localStorage.authToken)
                this.$refs.closeButton.click()
              }
              catch(e){
                if (e.response.status==400){
                  alert("Пароль/логин неправильные! Попробуйте снова!")
                  this.username=""
                  this.password=""
              }
              }
            },
            async logOut(){
                const response=await this.logout()
                this.$router.push('/')
            }
        }
    }
</script>