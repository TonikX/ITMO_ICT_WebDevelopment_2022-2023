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
        Неправильный логин или пароль. Попробуйте снова
      </div>
    </div>
    <div class="d-grid gap-2 mb-3">
      <button
        class="btn text-light"
        @click="authorize"
        style="background-color: #2a9d8f"
      >
        Войти
      </button>
    </div>
    <p class="text-center text-muted">Еще нет аккаунта?</p>
    <div class="d-grid gap-2">
      <button class="btn" @click="goSignUp" style="background-color: #e9c46a">
        Зарегистрироваться
      </button>
    </div>
  </span>
</template>

<script>

import axios from "axios";

export default {
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
    goSignUp() {
      this.$router.replace({ path: "/signup" });
    },
    goUser() {
      this.$router.replace({ path: "/about" });
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
        })
        .catch((e) => {
          this.retryEnter = true;
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
