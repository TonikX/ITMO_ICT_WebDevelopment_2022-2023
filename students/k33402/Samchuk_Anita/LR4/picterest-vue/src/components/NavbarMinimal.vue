<template>
  <div class="container-fluid my-navbar sticky-top">
    <nav class="navbar navbar-light">
      <router-link to="/" class="navbar-brand">
        <img
          src="@/assets/logo.png"
          width="30"
          height="30"
          class="d-inline-block align-top"
          alt=""
        />
        Picterest
      </router-link>
      <ProfileBlock></ProfileBlock>
    </nav>
  </div>
</template>

<script>
import ProfileBlock from '@/components/ProfileBlock'

export default {
  name: 'TheNavbarMinimal',

  components: {
    ProfileBlock
  }
}
</script>

<style scoped></style>
