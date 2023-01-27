<template>
  <section id="about_event">
    <section>
      <div class="container-xxl col-9 d-flex bg-white border py-4
        px-5" style="margin-top: 50px;">
        <h2 class="col-10">{{this.dataToUsed.title}}</h2>
        <a href="#" class="btn btn-dark col-2" @click.prevent="joinEvent(this.dataToUsed.id)">Join the event</a>
      </div>
    </section>

    <section class="container-xxl col-9 mt-4">
      <div class="row justify-content-center">
        <div class="col-9" style="padding-right: 50px">
          <img :src="dataToUsed.img" class="w-100">
          <h5 class="mt-5">About this Event</h5>
          <p >{{this.dataToUsed.description}}</p>
          <a href="#" class="btn btn-dark w-100 py-3" @click.prevent="joinEvent(this.dataToUsed.id)">Join the event</a>
          <h5 class="mt-5">Events you may like</h5>
          <Card :card-info="generalCardData"></Card>
        </div>
        <div class="col bg-white border h-100 pb-2 right-block-sticky">
          <div class="p-3">
            <h5>Date & Time</h5>
            <p>{{this.dataToUsed.date}}</p>
            <h5 class="mt-4">Location</h5>
            <p>{{this.dataToUsed.location}}</p>
          </div>
<!--          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2482.527039981535!2d-0.08138018428164229!3d51.52189247963755!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761cb10a2721e7%3A0x6a92d93fc7b70414!2sPrincipal%20Place!5e0!3m2!1sru!2sru!4v1665956949308!5m2!1sru!2sru" style="border:0;" class="w-100" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>-->
        </div>
      </div>
    </section>

  </section>
</template>

<script>
import axios from "axios";
import Card from "../components/Card.vue"
import { storeToRefs } from 'pinia'
import { useStateStore } from '../store/UserStatus.js'
export default {
  name: "card_description",
  components:{
      Card
  },
  data: function (){
    return{
        dataToUsed: [],
        URLParam: this.$route.params.id,
        generalCardData:[],
        CheckUserState: null

    }
  },
  methods:{
    async fetMethod(){
      const res = await axios.get(`http://localhost:3000/events/${this.URLParam}`);
      this.dataToUsed = res.data;
      console.log(this.dataToUsed)
      console.log(localStorage.getItem('userInfo.'))
    },
    async Gennral (){
      const test = await axios.get(`http://localhost:3000/events`);
      this.generalCardData = test.data;

    }
    ,
    async joinEvent(sth){
      if (this.CheckUserState === false){
        alert ("Register Or log in first please")
      }else{
        let uidFromLocalStorage = JSON.parse(localStorage.getItem('userInfo'));
        const sender = await axios.post(`http://localhost:3000/user_joined_events`,{
          user_id: uidFromLocalStorage[0].id ,
          event_id: sth,
        });
        alert('Event Has added to your Profile')
        console.log(sender)
      }
    },
    checkState(){
      const  { userState } = storeToRefs(useStateStore())
      this.CheckUserState= userState;
    }
  },
  mounted() {
    this.fetMethod()
    this.Gennral()
    this.checkState()

  }

}
</script>

<style scoped>

</style>