<template> 
    <v-spacer></v-spacer>
    <v-btn @click="goSignUp()"
        text
      > Регистрация</v-btn>
</template>
<script>
export default {
name: "LoginBar",
methods: {
    goSignUp () {
      this.$router.push({ name: 'Registration' })
    },
}
}
</script>