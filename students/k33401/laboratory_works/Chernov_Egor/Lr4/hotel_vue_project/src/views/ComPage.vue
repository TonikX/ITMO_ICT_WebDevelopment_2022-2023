<template>
  <base-layout>
    <nav-bar />
    <div id="comPage">
      <div class="container col-8 justify-content-center py-4">
        <h1 class="text-center">My comments:</h1>
        <ul class="navbar-nav p-3">
          <li class="nav-item" v-for="comment in comments" :key="comment.id">
            <com-item v-if="comment.user_com.id === idUser" :username="comment.user_com.username" :rating_com="comment.rating_com" :review_com="comment.review_com" :check_in_com="comment.check_in_com" :check_out_com="comment.check_out_com" />
          </li>
        </ul>
      </div>
    </div>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import NavBar from "@/components/NavBar.vue";
import ComItem from "@/components/CommentRoom.vue";
import {mapActions, mapState} from "pinia";
import useRegComStore from "@/stores/regCom";

export default {
  name: "RegPage",

  components: { BaseLayout, NavBar, ComItem },

  data() {
    return {
      idUser: localStorage.getItem('idUser')
    }
  },

  computed: {
    ...mapState(useRegComStore, ['comments'])
  },

  methods: {
    ...mapActions(useRegComStore, ['loadComments'])
  },

  mounted() {
    this.loadComments()
  }
}
</script>

<style scoped>
#comPage {
  min-height: 100vh;
}
</style>