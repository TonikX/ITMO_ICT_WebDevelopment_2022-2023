<template>
  <section>
    <section style="margin-top: 50px;">
      <div class="container-xxl pt-5">
        <div class="row">
          <div class="col-6 pt-4">
            <h1>Find your event</h1>
            <p class="w-75 pt-3">With Eventika people organize events, make friends, find support, grow a business, and explore their interests. Hundreds of events are happening every day—join the fun.</p>
          </div>
          <div class="col-6">
            <img class="w-100" alt="Not Found" src="../assets/event.jpg">
          </div>
        </div>
      </div>
    </section>
  
    <section id="eventsection">
      <div class="container-xxl" style="margin-top: 160px;">
        <h2>Upcoming events</h2>
        <div class="d-flex justify-content-end" style="margin-right: 80px" @change="checkfilter">
          <div class="dropdown  ms-3">
            <select class="form-select" aria-label=".form-select-lg example" id="event-type">
              <option>Any type</option>
              <option value="online">Online</option>
              <option value="inperson">In person</option>
            </select>
          </div>
          <div class="dropdown  ms-3">
            <select class="form-select" aria-label=".form-select-lg example" id="category">
              <option>Any category</option>
              <option value="technology">Technology</option>
              <option value="career">Career & Business</option>
              <option value="health">Health</option>
              <option value="sports">Sports</option>
            </select>
          </div>
        </div>
  
        <div class="row mt-4" id="event_cards">
        </div>
  
      </div>
    </section>
  
    <Card :cardInfo=filteredArray></Card>
  </section>
  </template>
  
  <script>
  import axios from "axios";
  import Card from "../components/Card.vue"
  export default {
    name: "Main",
    data: function (){
      return{
        APIResponse: [],
        filteredArray: [],
  
      }
    },
    components:{
      Card
    },
  
    methods:{
      async APIData(){
        try{
          const res = await axios.get(`http://localhost:3000/events`);
          this.APIResponse = res.data;
          
          // console.log(this.APIResponse)
  
  
        }catch (error){
          console.log("error", error)
        }
      },
      checkfilter(){
        const eventTypeValue = document.getElementById("event-type").value;
        const categoryValue = document.getElementById("category").value;
      
      for (let i = 0; i < this.APIResponse.length; i++) {
          if ((this.APIResponse[i].eventtype == (eventTypeValue) || eventTypeValue==="Any type") &&
              (this.APIResponse[i].category==(categoryValue) || categoryValue==="Any category")) {
                this.filteredArray.push(this.APIResponse[i])
          } else {
            console.log("API data error")
          }
          
      }console.log(this.filteredArray)
      }
    },
     mounted() {
      this.APIData()
      // this.checkfilter()
      // console.log(this.APIResponse)
    },
  
  }
  </script>
  
  <style scoped>
  
  </style>