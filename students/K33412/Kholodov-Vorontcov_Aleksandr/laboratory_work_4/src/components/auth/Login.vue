<template>
  <section class="vh-100">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-start h-100">
        <div class="col-5">
          <div class="card" style="border-radius: 1rem;">
            <div class="card-body p-4">
              <div class="row p-3">
                <svg class="img-logo" href="/" style="height: 50px">
                  <use xlink:href="#logo">
                  </use>
                </svg>
              </div>

              <div class="row py-5 px-3">
                <h3 class="mb-0">Войдите в систему Coinbase</h3>
              </div>

              <form type="submit" @submit.prevent="onLogSubmit">
                <div class="row mb-4 px-3">
                  <div class="form-outline col-12 ">
                    <label class="form-label fw-bolder" for="typeEmailX">Электронная почта</label>
                    <input v-model.trim.lazy="user.email" type="email" id="typeEmailX"
                           class="form-control input form-control-md"
                           placeholder="Ваш адрес электронной почты" name="email" autocomplete="off"
                           required/>
                  </div>
                </div>

                <div class="row mb-4 px-3">
                  <div class="form-outline col-12  ">
                    <label class="form-label fw-bolder" for="typePasswordX">Пароль</label>
                    <input v-model.trim.lazy="user.password" type="password" id="typePasswordX"
                           class="form-control input form-control-md"
                           placeholder="Ваш пароль" name="password" autocomplete="off" required/>
                  </div>
                </div>

                <div class="row px-3">
                  <p class=" mb-4">
                    <a class="password-forgot" href="#">Забыли пароль?</a>
                  </p>
                </div>

                <div class="row px-3">
                  <a href="" class="login-link">
                    <button class="btn btn-primary col-12 mb-3" style="border-radius: 100px"
                            :disabled="!formReady" type="submit">Войти
                    </button>
                  </a>
                </div>
              </form>

              <div class="row px-3 mb-4">
                <a href="/register" class="">
                  <button class="btn btn-light col-12" style="border-radius: 100px" type="submit">Создать учетную запись</button>
                </a>
              </div>

              <div class="row col-md-6 mx-auto">
                <a href="#" class="extra-link">Войти в бизнес-аккаунт</a>
              </div>

              <div class="row col-md-7 mx-auto mb-2">
                <a href="https://www.coinbase.com/legal/privacy" class="extra-link">Политика
                  конфиденциальности</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>



<script>
import {mapActions} from "pinia";
import useUsersStore from "@/stores/users";
import router from "@/router";

export default {
  name: 'Login',
  data() {
    return {
      user: {
        email: "",
        password: "",
      }
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['signUp']),
    async onLogSubmit() {

      await this.signUp(this.user)

    }
  },
  computed: {
    formReady() {
      return Object.values(this.user).every(value => value !== '')
    }
  },
  beforeMount() {
    localStorage.getItem('pinia_users') ? router.push('/personal') : router.push('/login')
  }
}
</script>

<style>
.img-logo {
  width: 50% !important;
}

.container {
  padding-top: 100px;
}

.form-control {
  height: 60px;
  border-radius: 1rem;
}

.btn {
  height: 60px;
  border-radius: 100px;
}

.password-forgot {
  text-decoration: none;
}

.extra-link {
  text-decoration: none;
}

.btn-primary {
  background-color: var(--btn-color);
}

.btn-primary:hover {
  background-color: var(--btn-hover);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
}

body {
  background-color: var(--bg-color);
}

.card {
  background-color: var(--card-color);
  border-color: var(--border-input);
}

a {
  color: var(--link-color);
}

a:hover {
  color: var(--link-hover);
}

h3 {
  color: var(--text-color);
}

label {
  color: var(--text-color);
}

.form-control {
  background-color: var(--bg-color);
  border-color: var(--border-input);
  color: var(--text-color);
}

.form-control:focus {
  background-color: var(--bg-color);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
  color: var(--text-color)
}

.btn-light, .btn-light:hover {
  background-color: var(--btn-secondary);
  color: var(--text-color);
  border-color: var(--btn-secondary);
}

</style>
