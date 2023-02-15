<template>
  <base-layout> <register> </register>> </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import Register from "@/components/Register.vue";
import { mapActions, mapState } from "pinia";

import usersStore from "@/stores/user";

export default {
  name: "RegisterPage",
  components: { BaseLayout, Register },

  computed: {
    ...mapState(usersStore, ["user", "token"]),
  },

  methods: {
    ...mapActions(usersStore, ["register"]),
  },
};
</script>
