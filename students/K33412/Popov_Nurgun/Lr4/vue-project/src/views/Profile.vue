<template>
  <section>
    <div class="container-xxl col-11" style="margin-top: 50px;">
      <div class="row justify-content-center">
        <div class="col-md-3">
          <div class="py-3 bg-dark rounded-top">
            <img src="../assets/person.jpeg" class="w-50 mx-auto d-block mt-3" alt="person">
            <p class="login-text-size text-white text-center mt-4"> {{this.CurrentUser.firstname}} {{this.CurrentUser.lastname}}</p>
            <p class="text-white text-center">{{this.CurrentUser.email}}</p>
          </div>
          <ul class="list-group">
            <li class="list-group-item">
              <a class="text-danger text-decoration-none link-dark" @click.prevent="logout">Выйти</a>
            </li>
          </ul>
        </div>

        <div class="col-md-9 mb-5" style="padding-left: 50px;">
          <h3>Предстояющие мероприятия</h3>
          <Card :card-info="eventData"></Card>
        </div>		
      </div>
    </div>	
  </section>
</template>

<script>
  import axios from "axios";
  import Card from '../components/Card'
  import { useStateStore } from '../store/UserStatus.js'
  export default {
    name: "Profile",
    data:function (){
      return{
        eventData: [],
        CurrentUser: ''
      }
    },
    components:{
      Card
    },
    methods:{
      async dataFromAPI(){
        try{
          const user = JSON.parse(localStorage.getItem('userInfo'));
          const CurrentUID = user[0].id;
          this.CurrentUser = user[0];
          const res = await axios.get(`http://localhost:3000/user_joined_events?user_id=${CurrentUID}`);
          for(let i =0; i <res.data.length; i++){
            let selectedEvents= (await axios.get(`http://localhost:3000/events/${res.data[i].event_id}`)).data
            this.eventData.push(selectedEvents)
          }
        }catch (error){
          console.log("error", error)
        }
      },
      logout(){
        const { StateChecker } = useStateStore()
        localStorage.clear();
        StateChecker(false);
        window.location.reload();
        this.$router.push({name: "Main"})
      }
    },
    mounted() {
      this.dataFromAPI()
    }
  }
</script>

<style scoped>
  .login-text-size {
    font-size: large;
    font-weight: 500;
  }
</style>