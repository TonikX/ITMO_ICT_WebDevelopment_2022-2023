<template>
    <Head />
    <ProfileAbout />
</template>

<script>

import Head from "@/components/Head.vue"
import ProfileAbout from "@/components/ProfileAbout.vue"


export default {
  name: 'ProfileView',
  components: {
    ProfileAbout,
    Head
  }
}
</script>