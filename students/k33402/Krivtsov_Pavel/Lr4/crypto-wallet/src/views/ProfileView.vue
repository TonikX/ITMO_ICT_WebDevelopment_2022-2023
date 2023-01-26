<template>
  <ProfileUserBlock/>

  <hr class="featurette-divider">

  <div class="container py-3">
    <div class="row row-cols-1 g-4">
      <UserCurrenciesList :ownerships="ownerships"/>
    </div>
  </div>
</template>

<script>
import $ from "jquery"

import UserCurrenciesList from "../components/UserCurrenciesList.vue";
import ProfileUserBlock from "../components/ProfileUserBlock.vue";

export default {
  name: "ProfileView",
  components: {
    UserCurrenciesList,
    ProfileUserBlock
  },
  data() {
    return {
      ownerships: []
    }
  },
  created() {
    this.loadOwnerships()
  },
  methods: {
    loadOwnerships() {
      $.ajax({
        url: 'http://127.0.0.1:8000/ownerships',
        type: "GET",
        success: (response) => {
          this.ownerships = response
        }
      })
    }
  }
}
</script>
