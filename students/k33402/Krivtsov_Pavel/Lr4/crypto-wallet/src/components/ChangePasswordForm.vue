<template>
  <form method="post" @submit.prevent="changePassword">
    <div class="container pb-4">
      <router-link class="logo-link" to="/">
        <img class="filter-logo" src="@/assets/wallet2.svg" alt="Wallet" width="50" height="50">
        <p class="fs-3">crypto wallet</p>
      </router-link>
    </div>

    <div class="form-floating mb-2">
      <input v-model="current_password" type="password" name="password" class="form-control" id="current_password"
             placeholder="Password" required>
      <label for="current_password">Старый пароль</label>
    </div>

    <hr/>

    <div class="form-floating pb-1">
      <input v-model="new_password" type="password" name="password" class="form-control" id="new_password"
             placeholder="Password" required>
      <label for="new_password">Новый пароль</label>
    </div>

    <div class="form-floating pb-5">
      <input v-model="re_new_password" type="password" name="password" class="form-control" id="re_new_password"
             placeholder="Password" required>
      <label for="re_new_password">Новый пароль еще раз</label>
    </div>

    <button class="w-100 btn btn-lg btn-main mb-3" type="submit">Сменить пароль</button>

    <div>
      <router-link to="/profile" class="link-side">Назад</router-link>
    </div>
  </form>
</template>

<script>
import $ from "jquery"

export default {
  name: "ChangePasswordForm",
  data() {
    return {
      current_password: "",
      new_password: "",
      re_new_password: ""
    }
  },
  methods: {
    changePassword() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/users/set_password/",
        type: "POST",
        data: {
          new_password: this.new_password,
          re_new_password: this.re_new_password,
          current_password: this.current_password
        },
        success: () => {
          console.log("success")
          alert("Ваш пароль успешно обновлен")
          this.$router.push({name: "profile"})
        },
        error: (response) => {
          console.log(response)
          alert(Object.values(response.responseJSON)[0])
          this.new_password = ""
          this.re_new_password = ""
          this.current_password = ""
        }
      })
    }
  }
}
</script>
