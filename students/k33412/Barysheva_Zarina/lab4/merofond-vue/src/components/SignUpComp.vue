<template>
    <span id="background">
      <div class="mb-3 text-center">
        <label for="login" class="form-label fs-5">Имя пользователя</label>
        <input
          :class="{ 'form-control': true, 'is-invalid': retryEnter }"
          id="login"
          v-model="username"
        />
      </div>
      <div class="mb-3 text-center">
        <label for="pass" class="form-label fs-5">Пароль</label>
        <input
          type="password"
          :class="{ 'form-control': true, 'is-invalid': retryEnter }"
          id="pass"
          v-model="password"
        />
        <div
          v-if="retryEnter"
          id="validationServerUsernameFeedback"
          :class="{ 'invalid-feedback': retryEnter }"
          class="text-center"
        >
          Пароль не должен быть похож на имя пользователя и должен содержать больше 8 символов
          ИЛИ 
          Это имя уже занято, попробуйте другое
        </div>
      </div>
      <div class="d-grid gap-2 mb-3">
        <button class="btn text-light" @click="registration" style="background-color: #2A9D8F;">Зарегистрироваться</button>
      </div>
      <p class="text-center text-muted">Есть аккаунт?</p>
      <div class="d-grid gap-2">
        <button class="btn" @click="goLogin" style="background-color: #E9C46A;">
            Войти 
        </button>
      </div>
    </span>
  </template>
  
  <script>
  
  import axios from "axios";
  
  export default {
//   setup() {
//     if (localStorage.getItem("token")) {
//       router.replace({ path: "/user" });
//     }
//   },
  data() {
    return {
      password: "",
      username: "",
      retryEnter: false,
    };
  },
  methods: {
    goEvents() {
      this.$router.replace({ path: "/events" });
    },
    goLogin() {
      this.$router.replace({ path: "/login" });
    },
    registration() {
        axios
            .post("http://127.0.0.1:7777/auth/users/", {
            username: this.username,
            password: this.password,
            })
            .then((resp) => {
            this.authorize();
            })
            .catch((e) => {
            this.retryEnter = true;
            });
    },
    authorize() {
      axios
        .post("http://127.0.0.1:7777/auth/token/login", {
          username: this.username,
          password: this.password,
        })
        .then((resp) => {
          localStorage.setItem("token", resp.data.auth_token);
          this.goEvents();
        // })
        // .catch((e) => {
        //   this.retryEnter = true;
        });
    },
  },
};
</script>

<style>
#background {
  background-color: white;
}
p {
  color: var(--main-font-color);
}
</style>

  