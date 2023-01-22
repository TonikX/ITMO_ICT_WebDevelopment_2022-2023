<template @userrec>
  <section class="registration-page">
    <div class="container py-5 ">
      <div class="row justify-content-center align-items-center">
        <div class="col">
          <div class="card-registration">
            <div class="card-body">
              <p class="mb-10">Обязательные поля отмечены звездочкой: *</p>
              <form @submit.prevent="onRegSubmit">
                <div class="row">
                  <div class="col-3 mb-3 ">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="firstName">Имя*</label>
                      <input v-model.trim.lazy="user.firstName" type="text" id="firstName"
                             class="form-control form-control-lg"
                             placeholder="Имя" name="firstName" autocomplete="off" required/>
                    </div>
                  </div>

                  <div class="col-md-3 mb-3">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="lastName">фамилия*</label>
                      <input v-model.trim.lazy="user.lastName" type="text" id="lastName"
                             class="form-control form-control-lg"
                             placeholder="фамилия" name="lastName" autocomplete="off" required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-11 mb-4 d-flex align-items-center">
                    <div class="form-outline w-100">
                      <label class="form-label fw-bolder" for="emailAddress">Электронная
                        почта*</label>
                      <input v-model.trim.lazy="user.email" type="email" id="emailAddress"
                             class="form-control form-control-lg"
                             placeholder="Электронная почта" name="email" autocomplete="off"
                             required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-11 mb-4 pb-2">
                    <div class="form-outline">
                      <label class="form-label fw-bolder" for="password">Пароль*</label>
                      <input v-model.trim.lazy="user.password" type="password" id="password"
                             class="form-control form-control-lg"
                             placeholder="Выберите пароль" name="password" autocomplete="off"
                             required/>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-11 mb-4">
                    <input class="form-check-input" type="checkbox" value="" id="invalidCheck" v-model="agree" required>
                    <label class="form-check-label" for="invalidCheck">
                      Я подтверждаю, что мне исполнилось 18, и принимаю положения следующих
                      документов: <a class="card-link"
                                     href="https://www.coinbase.com/legal/user_agreement">Пользовательское
                      Соглашение</a> и <a class="card-link m-0"
                                          href="https://www.coinbase.com/legal/privacy">Политика
                      конфеденциальности</a>.
                    </label>
                  </div>
                </div>

                <div class="row">
                  <div class="col-11">
                    <div class="d-grid gap-2 mt-20">
                      <button class="btn btn-primary fw-bolder" type="submit" :disabled="!formReady">Создать учетную
                        запись
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import {mapActions} from 'pinia';
import useUsersStore from "@/stores/users";
import router from "@/router";

export default {
  name: 'Register',
  data() {
    return {
      user: {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        coins: [],
      },
      agree: false
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['register']),
    async onRegSubmit() {

      await this.register(this.user);

    }
  },
  computed: {
    formReady() {
      return Object.values(this.user).every(value => value !== '') && this.agree
    }
  },
  beforeCreate() {
    localStorage.getItem('pinia_users') ? router.push('/personal') : router.push('/register')
  }
}
</script>

<style>
.form-check-label {
  font-size: 14px;
}

.form-control {
  height: 70px;
  border-radius: 8px;
}

.card-link {
  text-decoration: none;
}

.btn-primary {
  height: 70px;
}

body {
  background-color: var(--bg-color);
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

.btn-primary {
  background-color: var(--btn-color);
}

.btn-primary:hover {
  background-color: var(--btn-hover);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
}

.form-check-input:checked {
  background-color: var(--btn-hover);
  color: var(--btn-hover);
  box-shadow: 0 0 10px var(--btn-hover);
  border-color: var(--btn-hover);
}

.form-check-input:focus {
  box-shadow: 0 0 10px var(--btn-hover);
  border-color: var(--btn-hover);
}

.form-check-input {
  border-color: var(--btn-hover);
  margin-right: 10px;
}

a {
  color: var(--link-color);
}

a:hover {
  color: var(--link-hover);
}

@media (prefers-color-scheme: dark) {
  .nav-logo {
    filter: invert(10%);
  }
}
</style>