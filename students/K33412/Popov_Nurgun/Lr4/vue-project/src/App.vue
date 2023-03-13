<template>
  <section id="app">
    <Header></Header>
    <router-view></router-view>
    <Foot></Foot>
<!--    <img alt="Vue logo" src="./assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  </section>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'
import Foot from './components/footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Foot
  }
}
</script>

<style>
</style>