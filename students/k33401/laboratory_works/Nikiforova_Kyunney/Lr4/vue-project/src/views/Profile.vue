<template>
<section>
  <div class="container-xxl col-9" style="margin-top: 50px;">
    <div class="row justify-content-center">
      <div class="col-md-3">
        <div class="py-5 bg-dark rounded-top">
          <img src="../assets/avatar.svg" class="w-50 mx-auto d-block">
          <h5 class="text-white text-center mt-4">{{this.CurrentUser.firstname}} {{this.CurrentUser.lastname}}</h5>
        </div>
        <ul class="list-group">
<!--          <li class="list-group-item">-->
<!--            <a class="text-decoration-none link-dark" href="#">My profile</a>-->
<!--          </li>-->
          <li class="list-group-item list-group-item-secondary">
            <a class="text-decoration-none link-dark active" aria-current="true" href="#">My events</a>
          </li>
          <li class="list-group-item">
            <a class="text-danger text-decoration-none link-dark" @click.prevent="logout">Log out</a>
          </li>
        </ul>
      </div>

      <div class="col-md-9" style="padding-left: 50px;">
        <h3>My events</h3>
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
        // const UserInfo = await axios.get(`http://localhost:3000/users/${CurrentUID}`);
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

</style>