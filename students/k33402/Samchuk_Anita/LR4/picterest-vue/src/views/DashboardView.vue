<template>
  <div class="container-fluid">
    <NavbarWithFilters></NavbarWithFilters>

    <section class="photos mt-4">
      <div class="pinterest-grid">
        <router-link
          v-for="photo in photos"
          :key="photo.id"
          :to="'/post/' + photo.id">
          <img
            class="main-image"
            alt="dashboard-photo-1"
            :src="photo.urls.small"
          />
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
import NavbarWithFilters from '@/components/NavbarWithFilters'

export default {
  name: 'DashboardView',

  components: {
    NavbarWithFilters
  },

  beforeMount () {
    this.loadPhotos()
  },

  computed: {
    photos () {
      return this.$store.getters.photos
    }
  },

  methods: {
    loadPhotos () {
      this.$store.dispatch('getPhotos')
    }
  },

  head: {
    title: 'Picterest- Home'
  }
}
</script>
