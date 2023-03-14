<template>
  <div class="container-fluid">
    <NavbarMinimal></NavbarMinimal>
    <div class="container">
      <div class="row">
        <div class="col-6">
          <section class="settings mt-4">
            <h4 class="mb-4">Profile</h4>
            <div class="form-group row mb-3">
              <div class="col-6">
                <label class="label" for="first-name">First Name</label>
                <input id="first-name" type="text" class="form-control" placeholder="First Name" required>
              </div>
              <div class="col-6">
                <label class="label" for="last-name">Last Name</label>
                <input id="last-name" type="text" class="form-control" placeholder="Last Name" required>
              </div>
            </div>
            <div class="form-group mb-3">
              <label class="label" for="name">Username</label>
              <input id="name" type="text" class="form-control" placeholder="Username" required>
            </div>
            <div class="form-group mb-3">
              <label class="label" for="email">Email</label>
              <input id="email" type="text" class="form-control" placeholder="Email" required="">
            </div>
            <div class="form-group mb-3">
              <label class="label" for="description">Bio</label>
              <textarea id="description" type="text" class="form-control" placeholder="Enter a Bio"></textarea>
            </div>
            <div class="form-group d-flex justify-content-end">
              <button type="submit" class="btn btn-secondary px-3 mx-2">Cancel</button>
              <button type="submit" class="btn btn-primary px-3">Save</button>
            </div>
          </section>
        </div>
        <div class="col-6">
          <h4 class="mt-4">Liked pictures</h4>
          <div class="pinterest-grid-profile">
            <img v-for="photo in likedPhotos" :key="photo.photo" class="main-image" :src="photo.url"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavbarMinimal from '@/components/NavbarMinimal'

export default {
  name: 'ProfileView',

  computed: {
    likedPhotos () {
      return this.$store.getters.likedPhotos
    }
  },

  beforeMount () {
    if (!localStorage.getItem('accessToken')) {
      this.$router.push('/login')
    }

    this.$store.dispatch('getLikedPhotos', { accessToken: localStorage.accessToken, userId: JSON.parse(localStorage.user).id })
  },

  components: {
    NavbarMinimal
  }
}
</script>

<style scoped></style>
