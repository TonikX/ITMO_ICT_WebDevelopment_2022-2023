<template>
<div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-xl-9">
      
              <h1 class="mb-4">Регистрация</h1>
              <div class="card" style="border-radius: 15px;">
                <div class="card-body">
      
                  <div class="row align-items-center pt-4 pb-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Имя пользователя</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="username" type="text" class="form-control form-control-lg" id="username" name="username"/>
      
                    </div>
                  </div>

                  <hr class="mx-n3">

                  <div class="row align-items-center pt-4 pb-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Имя</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="first_name" type="text" class="form-control form-control-lg" id="first_name" name="first_name"/>
      
                    </div>
                  </div>

                  <hr class="mx-n3">

                  <div class="row align-items-center pt-4 pb-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Телефонный номер</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="phone" type="text" class="form-control form-control-lg" id="phone" name="phone"/>
      
                    </div>
                  </div>
                  <hr class="mx-n3">


                  <div class="row align-items-center pt-4 pb-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Фамилия</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="last_name" type="text" class="form-control form-control-lg" id="last_name" name="last_name"/>
      
                    </div>
                  </div>

                  <hr class="mx-n3">


                  <div class="row align-items-center py-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Почта</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="email" type="email" class="form-control form-control-lg" placeholder="example@example.com" id="email" name="email"/>
      
                    </div>
                  </div>
    

                  <hr class="mx-n3">

                  <div class="row align-items-center pt-4 pb-3">
                    <div class="col-md-3 ps-5">
      
                      <h6 class="mb-0">Пароль</h6>
      
                    </div>
                    <div class="col-md-9 pe-5">
      
                      <input v-model="password" type="password" class="form-control form-control-lg" />
      
                    </div>
                  </div>

                  <hr class="mx-n3">
      
      
                  <div class="px-5 py-4">
                    <button @click="sign_up()" class="btn btn-dark btn-lg">Регистрация</button>
                  </div>
      
                </div>
              </div>
            </div>
          </div>
</template>

<script>
    import { mapActions, mapState } from 'pinia';
    import userStore from '@/store/user_store'

    export default {
        name: "Head",

        data(){
          return {
            username: "",
            first_name: "",
            phone: "",
            last_name: "",
            email: "",
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
            ...mapActions(userStore,['addNewUser']),
            async sign_up() {
                if (!this.username || !this.password || !this.first_name ||
                    !this.phone || !this.email || !this.last_name) {
                     alert("Заполните все поля!!!!")
                }
              const data = {}
              data["username"]=this.username
              data["password"]=this.password
              data["first_name"]=this.first_name
              data["last_name"]=this.last_name
              data["phone"]=this.phone
              data["email"]=this.email
              const response = await this.addNewUser(data)
              const  log_data = {}
              log_data['username'] = this.username
              log_data['password'] = this.password
              await this.login(log_data)
              localStorage.setItem("id", response.data.id)
              this.$router.push("/profile")
            }
        }
    }

</script>