<template>
  <transition name="modal">
    <div class="modal-mask" @click="$emit('close-modal')">
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <form type="submit" @submit.prevent="onLogSubmit">
            <h1>Войти в аккаунт</h1>
            <div class="form-outline mb-4">
              <label class="form-label" for="form1">Логин*</label>
              <input type="text"
                     id="form1"
                     class="form-control"
                     required
                     autocomplete="off"
                     v-model="user.username"/>
            </div>
            <div class="form-outline mb-5">
              <label class="form-label" for="form2">Пароль*</label>
              <input type="password"
                     id="form2"
                     class="form-control"
                     v-model="user.password"
                     required
                     autocomplete="off"/>
            </div>

            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-primary btn-block p-2 mb-4 fw-semibold"
                      @click="$emit('close-modal')">Войти
              </button>
            </div>

            <div class="d-flex justify-content-center">
              <p class="text mx-2">Нет аккаунта?</p>
              <a class="link-primary fw-semibold" href="#" @click="$emit('show-register')">Регистрация</a>
            </div>
          </form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>

import {mapActions} from "pinia";
import useUsersStore from "@/stores/users";

export default {
  name: 'Login',
  data() {
    return {
      user: {
        username: '',
        password: '',
      },

    }
  },
  methods: {
    ...mapActions(useUsersStore, ['onLogin']),

    async onLogSubmit() {
      await this.onLogin(this.user)

    }
  }
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 35%;
  height: fit-content;
  margin: 0 auto;
  padding: 50px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

h1 {
  margin-bottom: 30px;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>

