<template>
  <guest :id="id"/>
</template>

<script>
import Guest from "@/components/Guest.vue";

export default {
  props: {
    id: String
  },
  components: {
    Guest
  }
}
</script>