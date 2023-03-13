<template>
  <section>
    <div class="container justify-content-between mt-5 row mx-auto">
      <div class="container-xxl pt-5">
        <div class="row">
          <div class="col-12 col-xl-6 col-md-12">
            <h1>Сделай свой день интереснее с нами</h1>
            <p class="w-70 pt-3">Чем бы вы ни планировали заняться в этом году, вы всегда можете рассчитывать на помощь Meetings. С помощью Meetings люди приобретают друзей, обращаются за поддержкой, развивают свой бизнес и находят людей с общими интересами. Каждый день проводятся тысячи мероприятий — присоединяйтесь!</p>
          </div>
          <div class="col-12 col-xl-6 col-md-12">
            <img class="rounded w-100" src="../assets/Meeting.webp" alt="Meeting">
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container justify-content-between">
      <div class="row py-5">
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Карьерный рост</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Читайте с друзьями</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Двигайтесь с нами</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Пишите вместе</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Про природу</a>
          </div>
        </div>
        <div class="col">
          <div class="text-center">
            <a class="btn btn-secondary" href="#">Духовный рост</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="eventsection">
    <div class="container justify-content-between mt-5 row mx-auto">
      <div class="container-xxl pt-2">
        <div class="filters-row row">
          <div class="col-12 col-xl-6 col-md-12">
            <h2>Предстояющие мероприятия</h2>
          </div>
          <div class="col-12 col-xl-6 col-md-12">
            <div class="d-flex justify-content-end" @change="checkfilter">
              <div class="dropdown ms-3">
                <select class="form-select dropdown-color" aria-label=".form-select-lg example" id="event-type">
                  <option>Тип мероприятия</option>
                  <option value="Кино">Кино</option>
                  <option value="Вечеринка">Вечеринка</option>
                  <option value="Туризм">Туризм</option>
                </select>
              </div>          
              <div class="dropdown ms-3">
                <select class="form-select dropdown-color" aria-label=".form-select-lg example" id="event-place">
                  <option>Место проведения</option>
                  <option value="Онлайн">Онлайн</option>
                  <option value="Лично">Лично</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div class="row mt-4" id="event_cards">
        </div>
        <Card :cardInfo=APIResponse></Card>
        <Card :cardInfo=filteredArray></Card>
      </div>
    </div>
  </section>

  <seсtion>
    <div class="row justify-content-center text-center mt-3">
      <div class="col-auto">
        <h1 class="mt-5 mb-4">Как работает Meetings</h1>
        <p>Знакомьтесь с новыми людьми, которые разделяют ваши интересы,</p>
        <p>на онлайн- и очных мероприятиях. Создайте аккаунт бесплатно.</p>
      </div>
    </div>
  </seсtion>

  <section>
    <div class="container justify-content-between mb-5">
      <div class="row py-5">
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/HandsUp.png" alt="HandsUp">
            <p class="lower-text-size mb-3">Вступить в группу</p>
              <p>Занимайтесь тем, что вам нравится, встречайтесь с другими людьми, которым это нравится, найдите свое сообщество. Остальное уже история!</p>
          </div>
        </div>
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/Ticket.png" alt="Ticket">
            <p class="lower-text-size mb-3">Найти мероприятие</p>
              <p>Есть мероприятия практически на любую тему, о которой вы только можете подумать, от онлайн-игр и фотографии до йоги и пеших прогулок.</p>
          </div>
        </div>
        <div class="col">
          <div class="text-center mb-3">
            <img class="rounded w-50 mb-3" src="../assets/Group.png" alt="Group">
            <p class="lower-text-size mb-3">Создать группу</p>
              <p>Вам не нужно быть экспертом, чтобы собирать людей вместе и увлекаться общими интересами.</p>
          </div>
        </div>
      </div>
    </div>
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
        const categoryValue = document.getElementById("event-place").value;
        for (let i = 0; i < this.APIResponse.length; i++) {
          if ((this.APIResponse[i].eventtype===(eventTypeValue) || eventTypeValue==="Тип мероприятия") && 
              (this.APIResponse[i].eventplace===(categoryValue) || categoryValue==="Место проведения")) {
               this.filteredArray.push(this.APIResponse[i])
          } else {
            console.log("API data error")
          }
        }
        console.log(this.filteredArray)
      }
    },
      mounted() {
      this.APIData()
      // this.checkfilter()
      // console.log(this.APIResponse)
    }
  }
</script>

<style scoped>
</style>