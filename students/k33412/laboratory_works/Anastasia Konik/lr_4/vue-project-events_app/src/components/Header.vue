<template>
  <header class="container-fluid">
    <nav class="navbar navbar-expand-md">
      <div class="container-fluid">
        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar" id="Menu_btn"
                aria-label="Menu">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbar">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link active" to="/main">Main</router-link>
            </li>
            <li class="nav-item signinup_link">
              <router-link class="nav-link active" to="/signin">Sign in</router-link>
            </li>
            <li class="nav-item signinup_link">
              <router-link class="nav-link active" to="/signup">Sign up</router-link>
            </li>
            <li class="nav-item profile_link">
              <router-link class="nav-link active" to="/profile">Profile</router-link>
            </li>
            <li class="nav-item profile_link">
              <router-link class="nav-link active" to="/calendar">Calendar</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HeaderBlock",
  methods: {
    show_menu() {
      let token = localStorage.getItem('user_token')
      console.log(token)
      if (token !== null) {
        let menu_items = document.getElementsByClassName("signinup_link")
        while (menu_items.length > 0) {
          menu_items.item(0).parentNode.removeChild(menu_items.item(0))
        }
      } else {
        let menu_items = document.getElementsByClassName("profile_link")
        while (menu_items.length > 0) {
          menu_items.item(0).parentNode.removeChild(menu_items.item(0))
        }
      }
    }
  },
  mounted() {
    this.show_menu()
  }
}
</script>

<style scoped>

</style>