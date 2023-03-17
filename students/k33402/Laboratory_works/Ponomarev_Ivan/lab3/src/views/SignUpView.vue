<template>
    <Head />
    <Sign_up />
</template>

<script>

import Sign_up from "@/components/Sign_up.vue"
import Head from "@/components/Head.vue"

export default {
  name: 'EventsView',
  components: {
    Sign_up,
    Head
  }
}
</script>