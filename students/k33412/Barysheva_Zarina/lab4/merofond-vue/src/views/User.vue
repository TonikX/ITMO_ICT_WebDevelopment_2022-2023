<template>
  <span>
    <Navbar />
    <user-comp />
</span>
</template>

<script>

import Navbar from "../components/Navbar.vue";
import UserComp from '../components/UserComp.vue';

export default {
  components: { Navbar, UserComp },
}

</script>