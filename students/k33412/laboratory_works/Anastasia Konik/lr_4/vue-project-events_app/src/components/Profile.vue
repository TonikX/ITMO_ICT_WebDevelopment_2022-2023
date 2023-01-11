<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" display="none">
    <symbol id="Edit" viewBox="0 0 16 16">
      <path
          d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
      <path
          d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
    </symbol>
    <symbol id="Done" viewBox="0 0 16 16">
      <path
          d="M2.5 8a5.5 5.5 0 0 1 8.25-4.764.5.5 0 0 0 .5-.866A6.5 6.5 0 1 0 14.5 8a.5.5 0 0 0-1 0 5.5 5.5 0 1 1-11 0z"/>
      <path d="M15.354 3.354a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l7-7z"/>
    </symbol>
  </svg>
  <main class="container p-5 mb-5">
    <section id="user_profile" class="container row mx-auto">
      <section>
        <div class="row d-flex col-md-5 col-lg-4 col-xl-4 col-sm-8" style="float: left; margin-right: 10px">
          <img id="user_image" :src="user.img_url" alt="User image" style="float: left; border-radius: 10%">
          <input v-show="upload_input" type="file" id="user_image" accept="image/*" @change="handleUpload"
                 ref="user_photo">
        </div>
        <div class="row d-flex col-xl-6 col-lg-8 col-md-8 col-sm-12" style="float: none">
          <h1 id="user_name" class="text">{{ user.first_name }} {{ user.last_name }}</h1>
          <p id="user_login" class="text" style="font-size: 14pt">{{ user.email }}</p>
          <p v-if="user.user_info === null" id="user_info" ref="info" class="info text placeholder_text mt-1">Tell
            something
            about yourself</p>
          <p v-else id="user_info" ref="info" class="info text placeholder_text">{{ user.user_info }}</p>
        </div>
      </section>
      <div>
        <button class="btn btn-primary mx-1 mt-3" type="button" @click="edit" id="edit-button" ref="edit_btn"
                aria-pressed="true" :disabled="!isActive">Edit
          profile
          <svg class="icon">
            <use xlink:href="#Edit"></use>
          </svg>
        </button>
        <button class="btn btn-success invisible mt-3" type="button" @click="done" ref="done_btn" id="done-button"
                aria-pressed="true">Done
          <svg class="icon">
            <use xlink:href="#Done"></use>
          </svg>
        </button>
      </div>
      <div>
        <button class="btn btn-secondary mt-3 mx-1" @click="logout_btn" type="button" aria-pressed="true">Logout
        </button>
      </div>
    </section>
    <section id="user_events" class="container row mx-auto justify-content-center">
      <p class="text mt-4" style="font-size: 20pt"><b>Your events:</b></p>
      <div class="card event col-xl-4 col-lg-4 col-md-4 col-sm-6 card mx-3 mt-3"
           v-for="event in Events" :key="event.id">
        <card :title="event.title" :address="event.address" :img_src="event.img_src"
              :short_description="event.short_description" :id="event.id"></card>
      </div>
    </section>
  </main>
</template>

<script>
import {mapActions, mapState} from "pinia";
import useUsersStore from "@/stores/users";
import Card from "@/components/Card.vue";

export default {
  name: "Profile",
  components: {Card},
  data() {
    return {
      isActive: true,
      upload_input: false,
    }
  },
  computed: {
    ...mapState(useUsersStore, ['user', 'token', 'userEvents']),
    Events() {
      return this.userEvents
    }
  },
  methods: {
    ...mapActions(useUsersStore, ['logout', 'CurrentUser', 'getUserEvents']),


    async logout_btn() {
      // window.localStorage.removeItem('user_token')
      await this.logout()
      this.$router.push('/signin')
    },

    edit() {
      this.$refs["info"].innerHTML = ''
      this.$refs["info"].contentEditable = 'true'
      this.$refs["done_btn"].classList.replace('invisible', 'visible')
      this.isActive = false
      this.upload_input = true
    },

    async done() {
      this.$refs["info"].contentEditable = 'false'
      this.$refs["info"].classList.remove('placeholder_text')
      this.$refs["done_btn"].classList.replace('visible', 'invisible')
      let user_input = this.$refs["info"].innerHTML
      let image_input = this.$refs.user_photo.files[0]
      this.isActive = true
      this.upload_input = false

      if (image_input !== undefined) {
        let data = new FormData()
        data.append('image_url', image_input)

        const response = await fetch(`http://localhost:8000/api/user/edit/${this.user.id}/`, {
          method: "PUT",
          body: data,
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log(response)
        console.log(this.user)
      }

      if (user_input === '') {
      } else {
        let user_input_send = {'user_info': `${user_input}`}

        const response = await fetch(`http://localhost:8000/api/user/edit/${this.user.id}/`, {
          method: "PUT",
          body: JSON.stringify(user_input_send),
          headers: {
            'Content-Type': 'application/json'
          }
        })
        console.log(response)
      }
    },
  },
  mounted() {
    this.CurrentUser().then(result => {
      if (!result?.username) {
        this.$router.replace({path: '/main'})
      }
      this.getUserEvents()
    })
  }
}
</script>

<style scoped>

</style>