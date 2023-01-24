<template>
  <HeaderUnlogged/>
  <Register/>
</template>

<script>
import Register from "@/components/auth/Register.vue";
import HeaderUnlogged from "@/components/headers/HeaderUnlogged.vue";

export default {
  components: {
    Register,
    HeaderUnlogged
  }
}
</script>