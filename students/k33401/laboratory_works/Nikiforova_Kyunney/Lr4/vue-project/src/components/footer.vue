<template>
<section>
  <footer class="text-center text-white bg-dark" style="margin-top:160px">
    <div class="row p-4 justify-content-center">
      <div class="col-3 text-start">
        <h5>Your account</h5>
        <ul class="nav flex-column">
          <li class="nav-item mb-2">
            <router-link class="nav-link p-0 text-white" :to="{name: 'register'}">Sign up</router-link>
            <!-- <a href="sign_up.html" class="nav-link p-0 text-white"></a> -->
          </li>
          <li class="nav-item mb-2">
            <router-link class="nav-link p-0 text-white" :to="{name: 'login'}">Log in</router-link>
            <!-- <a href="log_in.html" class="nav-link p-0 text-white">Log in</a> -->
          </li>
          <li class="nav-item mb-2">
            <a href="#" class="nav-link p-0 text-white">Help</a>
          </li>
        </ul>
      </div>
      <div class="col-3 text-start">
        <h5>Discover</h5>
        <ul class="nav flex-column">
          <li class="nav-item mb-2">

            <a href="#eventsection" class="nav-link p-0 text-white">Events</a>
          </li>
          <li class="nav-item mb-2">
            <router-link class="nav-link p-0 text-white" :to="{name: 'calendar'}">Calendar</router-link>
            <!-- <a href="calendar.html" class="nav-link p-0 text-white">Calendar</a> -->
          </li>
        </ul>
      </div>
      <div class="col-3 text-start">
        <h5>Contact</h5>
        <ul class="nav flex-column">
          <li class="nav-item mb-2">
            <a href="#" class="nav-link p-0 text-white">eventika@gmail.com</a>
          </li>
          <li class="nav-item mb-2">
            <a href="#" class="nav-link p-0 text-white">+79042753422</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
      © 2022 Eventika
    </div>
  </footer>
</section>
</template>

<script>
export default {
  name: "footer"
}
</script>

<style scoped>

</style>