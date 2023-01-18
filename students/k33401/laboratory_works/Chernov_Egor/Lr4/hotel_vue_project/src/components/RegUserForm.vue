<template>
  <div class="container">
    <h1 class="row">Registration</h1>
    <input class="row my-2" v-model="email" type="text" placeholder="E-mail" />
    <input class="row my-2" v-model="username" type="text" placeholder="Username" />
    <input class="row my-2" v-model="password" type="password" placeholder="Password" />
    <button class="row">Create</button>
  </div>
</template>

<script>
export default {
  name: "RegUserForm",

  data() {
    return {
      email: "",
      username: "",
      password: ""
    }
  }
}
</script>

<style scoped>

</style>