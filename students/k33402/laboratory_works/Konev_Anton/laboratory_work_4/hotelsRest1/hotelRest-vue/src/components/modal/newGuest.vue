<template>
  <transition name="modal">
    <div class="modal-mask" @click="$emit('close-modal')">
      <div v-if="showSuccess" class="alert alert-success d-flex justify-content-center align-text-top fw-bold">
        Вы успешно создали пользователя!
      </div>
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <form type="submit" @submit.prevent="onCreateSubmit">
            <h1>Добавление гостя</h1>
            <div class="d-flex">
              <div class="w-50">
                <div class="form-outline mb-3 w-75">
                  <label class="form-label" for="form12">Фамилия*</label>
                  <input type="text"
                         id="form12"
                         class="form-control"
                         required
                         v-model="guest.last_name"
                         autocomplete="off"/>
                </div>
                <div class="form-outline mb-3 w-75">
                  <label class="form-label" for="form22">Имя*</label>
                  <input type="text"
                         id="form22"
                         class="form-control"
                         required
                         v-model="guest.first_name"
                         autocomplete="off"/>
                </div>
                <div class="form-outline mb-5 w-75">
                  <label class="form-label" for="form32">Отчество*</label>
                  <input type="text"
                         id="form32"
                         class="form-control"
                         required
                         v-model="guest.middle_name"
                         autocomplete="off"/>
                </div>
              </div>

              <div class="w-50">
                <div class="form-outline mb-3 w-75">
                  <label class="form-label" for="form42">Паспорт*</label>
                  <input type="text"
                         id="form42"
                         class="form-control"
                         required
                         v-model="guest.passport"
                         autocomplete="off"/>
                </div>
                <div class="form-outline mb-3 w-75">
                  <label class="form-label" for="form52">Город*</label>
                  <input type="text"
                         id="form52"
                         class="form-control"
                         required
                         v-model="guest.city"
                         autocomplete="off"/>
                </div>
              </div>
            </div>

            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-primary btn-block p-2 mb-3 fw-semibold">Создать</button>
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
import useGuestsStore from "@/stores/guests";

export default {
  name: 'newGuest',
  data() {
    return {
      guest: {
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        middle_name: '',
        city: '',
        passport: ''
      },
      showSuccess: false
    }
  },
  methods: {
    ...mapActions(useGuestsStore, ['sendBooking']),
    ...mapActions(useUsersStore, ["signUp"]),

    async onCreateSubmit() {
      this.guest.username = this.guest.first_name
      this.guest.password = this.guest.first_name + this.guest.passport
      await this.signUp(this.guest)

      this.showSuccess = true;
      setTimeout(() => {
        this.showSuccess = false;
        this.$emit('sclose-modal')
        window.location.reload()
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
  width: 60%;
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

</style>

