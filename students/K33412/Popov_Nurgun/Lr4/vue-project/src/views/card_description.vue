<template>
  <section id="about_event">
    <div class="container-xxl col-10 mt-4">
      <h2 class="mb-3">{{this.dataToUsed.title}}</h2>
      <div class="row mb-5">
        <div class="col-8">
          <img class="rounded w-100 mb-3" :aria-labelledby="dataToUsed.id" :src="dataToUsed.img_src">
          <p class="lower-text-size py-3"><strong>Детали</strong></p>
          <p class="event-text-size mb-3">{{this.dataToUsed.description}}</p>
        </div>
        <div class="col">
          <div class="rounded-3 p-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="container justify-content-between col-12 row">
              <div class="col-4">
                <img class="rounded w-100" :src="dataToUsed.img_src_2" alt="books">
              </div>
              <div class="col">
                <p class="event-text-size">{{this.dataToUsed.group_name}}</p>
                <p class="event-text-size event-bottom-text">{{this.dataToUsed.group_type}}</p>
              </div>
            </div>
          </div>
          <div class="rounded-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="p-3">
              <p class="event-text-size">Дата и время:</p>
              <p class="event-text-size event-bottom-text mb-3">{{this.dataToUsed.date}}</p>
              <p class="event-text-size">Место:</p>
              <p class="event-text-size event-bottom-text">{{this.dataToUsed.location}}</p>
            </div>
            <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1998.99229034957!2d30.3539683!3d59.9322701!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469631a5b366e8cd%3A0x5db5df3c54a9e502!2sMama%20Roma!5e0!3m2!1sru!2sru!4v1668966318386!5m2!1sru!2sru" height="300" style="border:0;" class="w-100" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map"></iframe>
          </div>
          <div class="rounded-3 p-3 event-right-card mx-auto mb-3" style="width: 350px;">
            <div class="text-center">
              <a href="#" @click.prevent="joinEvent(this.dataToUsed.id)" class="btn btn-primary">Присоединиться к мероприятию</a>
            </div>
          </div>
        </div>
      </div>
    </div>
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
      },
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
  .event-right-card {
    background-color: #f1f1f1;
  }
  .event-text-size {
    font-size: medium;
    font-weight: 500;
  }
  .event-bottom-text {
    opacity: .7;
  }
</style>