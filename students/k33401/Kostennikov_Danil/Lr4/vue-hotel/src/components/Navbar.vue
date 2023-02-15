<template></template>

<script>
import { mapActions, mapState } from "pinia";
import usersStore from "@/stores/user";

export default {
  name: "Navbar",
  computed: {
    ...mapState(usersStore, ["user", "token"]),
  },

  methods: {
    ...mapActions(usersStore, ["logout", "login"]),

    async logout_() {
      await this.logout();
      console.log("logout");
      console.log("user", this.user);
    },
  },
};
</script>
