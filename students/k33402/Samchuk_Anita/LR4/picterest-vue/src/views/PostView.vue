<template>
  <div class="container-fluid">
    <NavbarMinimal></NavbarMinimal>
    <div class="container">
      <section class="d-flex post-wrap mt-3">
        <img class="w-50 post-image" :src="photo ? photo.urls.regular : ''" />
        <div class="w-50 p-4 post-wrap">
          <div class="d-flex align-items-center justify-content-between">
            <h5 class="mb-1">{{ photo ? photo.user.name : '' }}</h5>
            <button @click="like" class="btn btn-primary btn-sm">Like</button>
          </div>
          <div>{{ date }}</div>
          <div class="mb-3">{{ photo ? photo.location.name : '' }}</div>
          <div>{{ photo ? photo.description : '' }}</div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import NavbarMinimal from '@/components/NavbarMinimal'
import axios from 'axios'

export default {
  name: 'PostView',

  components: {
    NavbarMinimal
  },

  beforeMount () {
    this.$store.dispatch('loadPhoto', this.$route.params.id)
  },

  computed: {
    photo () {
      return this.$store.getters.postPhoto
    },

    date () {
      const photo = this.photo

      return new Date(photo.created_at).toDateString()
    }
  },

  methods: {
    async like () {
      try {
        const userId = JSON.parse(localStorage.getItem('user')).id

        const response = await axios.post(
          'http://localhost:3000/600/likedPhotos',
          {
            photo: this.photo.id,
            url: this.photo.urls.small,
            userId
          },
          {
            headers: {
              Authorization: 'Bearer ' + localStorage.accessToken
            }
          }
        )

        if (response.status === 201) {
          console.log('liked')
        }
      } catch (e) {
        alert(e.response.data)
      }
    }
  }
}
</script>

<style scoped></style>
