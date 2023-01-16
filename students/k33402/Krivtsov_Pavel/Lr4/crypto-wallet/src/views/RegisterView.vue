<template>
  <main class="text-center sign-body">
    <div class="sign-form w-100 m-auto">
      <RegisterForm/>
    </div>
  </main>
</template>

<script>
import RegisterForm from "../components/RegisterForm.vue";

export default {
  name: "RegisterView",
  components: {
    RegisterForm
  }
}
</script>

<style scoped>

</style>