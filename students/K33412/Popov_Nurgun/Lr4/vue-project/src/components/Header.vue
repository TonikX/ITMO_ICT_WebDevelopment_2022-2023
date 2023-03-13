<template>
  <section>
    <header>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-xxl">
          <!-- <a class="navbar-brand" href="index.html">Meetings</a> -->
          <router-link class="navbar-brand" :to="{name: 'Main'}">Meetings</router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <!-- <a class="nav-link" href="calendar.html">Календарь мероприятий</a> -->
                <router-link class="nav-link" :to="{name: 'calendar'}">Календарь мероприятий</router-link>
              </li>
            </ul>
          </div>
          <div class="collapse navbar-collapse justify-content-end">
            <ul class="navbar-nav">
              <li class="nav-link active" v-show="UserStatusChecker==false">
                <router-link :to="{name: 'login'}"><button type="button" class="btn text-light" id="login">Войти</button></router-link>
              </li>
              <li class="nav-link active" v-show="UserStatusChecker==false">
                <router-link :to="{name: 'register'}"><button type="button" class="btn text-light" id="signup">Регистрация</button></router-link>
              </li>
              <li class="nav-link active" v-show="UserStatusChecker">
                <router-link :to="{name: 'profile'}"><button type="button" class="btn text-light" id="profile">Профиль</button></router-link>
              </li>
              <li class="nav-link active" v-show="UserStatusChecker">
                <button type="button" class="btn btn-danger" @click.prevent="logout" id="logout">Выйти</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </section>
</template>

<script>
  import { storeToRefs } from 'pinia'
  import { useStateStore } from '../store/UserStatus.js'

  export default {
    name: "Header",
    data: function(){
    return{
      UserStatusChecker: null ,
    }
    },
    mounted(){
      this.check()
      console.log('mouthed',this.UserStatusChecker)
    },
    methods:{
      check(){
        const  { userState } = storeToRefs(useStateStore())
        this.UserStatusChecker= userState;
      },
      logout(){
        const { StateChecker } = useStateStore()
        localStorage.clear();
        StateChecker(false);
        window.location.reload();
        console.log('logout' , this.UserStatusChecker)
      }
    }
  }
</script>

<style scoped>
header {
	position: sticky;
	z-index: 1000;
	top: 0;
}
</style>