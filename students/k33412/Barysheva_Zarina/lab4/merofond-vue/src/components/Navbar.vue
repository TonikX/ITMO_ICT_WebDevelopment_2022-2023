<template>
  <span>
  <nav class="navbar sticky-top mb-3" style="background-color: #13242A;">
    <div class="container-fluid">
      <a class="navbar-brand d-inline-block" id="clickable" @click="goEvents">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="white" class="bi bi-calendar-check d-inline-block align-text-bottom" viewBox="0 0 16 16">
                    <path d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                </svg>
                <h2 class="d-inline-block text-light mx-2"> Мерофонд</h2>
            </a>
        <span v-if="isToken">
            <li class="d-inline-block">
              <div class="d-grid gap-4 d-md-flex justify-content-end align-top">
                <button type="button" @click="goUser" class="btn text-light" style="background-color:#2A9D8F">
                   Личный кабинет
                </button>
            <button type="button" @click="goLogin" class="btn text-light" style="background-color:#E24D28">
                Выйти
            </button>
            </div>
            </li>
        </span>
    </div>
  </nav>
</span>
</template>

<script>

export default {
    props: {
      page: "",
    },
    data() {
        return {
            isToken: null,
        }
    },
    mounted() {
        const token = localStorage.getItem("token");
        if (!token) {
            this.isToken = 0;
        }
        else {
            this.isToken = 1;
        }
    },
  methods: {
    goUser() {
      this.$router.replace({ path: "/user" });
    },
    goEvents() {
      this.$router.replace({ path: "/events" });
    },
    goLogin() {
      localStorage.clear();
      this.$router.replace({ path: "/login" });
    },
  },
};
</script>

<style>
#clickable {
  cursor: pointer;
}
</style>
