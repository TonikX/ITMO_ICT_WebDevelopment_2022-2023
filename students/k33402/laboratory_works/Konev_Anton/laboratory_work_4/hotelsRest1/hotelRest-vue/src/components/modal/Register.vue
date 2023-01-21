<template>
  <transition name="modal">
    <div class="modal-mask" @click="$emit('close-register')">
      <div v-if="showSuccess" class="alert alert-success d-flex justify-content-center align-text-top fw-bold">
        Вы успешно прошли регистрацию! Теперь надо войти в аккаунт
      </div>
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <form type="submit" @submit.prevent="onRegSubmit">
            <h1>Регистрация</h1>
            <div class="form-outline mb-4">
              <label class="form-label" for="form1Example1">Имя пользователя*</label>
              <input type="text" id="form1Example1" class="form-control" v-model.trim="user.username" required
                     autocomplete="off"/>
            </div>
            <div class="form-outline mb-4">
              <label class="form-label" for="form2Example2">Email*</label>
              <input type="email" id="form2Example2" class="form-control" v-model.trim="user.email" required
                     autocomplete="off"/>
            </div>
            <div class="form-outline mb-4">
              <label class="form-label" for="form3Example3">Пароль*</label>
              <input type="password" id="form3Example3" class="form-control" v-model.trim="user.password" required
                     autocomplete="off"/>
            </div>
            <div class="form-outline mb-5">
              <label class="form-label" for="form4Example4">Повторите пароль*</label>
              <input type="password" id="form4Example4" class="form-control" required autocomplete="off"/>
            </div>

            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-primary btn-block p-2 mb-4 fw-semibold">Регистрация</button>
            </div>

            <div class="d-flex justify-content-center">
              <p class="text mx-2">Уже есть аккаунт?</p>
              <a class="link-primary fw-semibold" href="#" @click="$emit('show-modal')">Войти</a>
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
  name: 'Register',
  data() {
    return {
      user: {
        username: '',
        password: '',
        email: '',
        is_admin: true
      },
      showSuccess: false
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['signUp']),

    async onRegSubmit() {
      await this.signUp(this.user)

      this.showSuccess = true;
      setTimeout(() => {
        this.showSuccess = false;
        this.$emit('show-modal')
      }, 4000)
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

.alert {
  position: absolute;
  margin-top: 30px;
  width: 100%;
  height: 60px;
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

