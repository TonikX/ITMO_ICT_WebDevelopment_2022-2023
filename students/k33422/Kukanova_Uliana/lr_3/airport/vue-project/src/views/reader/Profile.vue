<template>
  <div class="edit">
      <div>
        <h2>Личный кабинет</h2>
      </div>

      <h3>Форма регистрации рейса</h3>

     <form @submit.prevent="signFlights"
      ref="editForm"
      class="my-2">
      <div class="row">


        <div class="col-25">
          <label for="number">Номер рейса</label>
        </div>
        <div class="col-75">
          <input v-model="number" type="number" id="number" name="number" placeholder="Номер рейса">
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="distance">Расстояние до пункта назначения</label>
        </div>
        <div class="col-75">
          <input v-model="distance" type="number" id="distance" name="distance" placeholder="Расстояние в км">
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="departure">Пункт вылета</label>
        </div>
        <div class="col-75">
          <textarea v-model="departure" id="departure" name="departure" placeholder="Пункт вылета"></textarea>
        </div>
      </div>

<div class="row">
        <div class="col-25">
          <label for="arrival">Пункт назначения</label>
        </div>
        <div class="col-75">
          <textarea v-model="arrival" id="arrival" name="arrival" placeholder="Пункт назначения"></textarea>
        </div>
      </div>

     <div class="row">
             <div class="col-25">
               <label for="completed">Количество совершенных рейсов</label>
             </div>
             <div class="col-75">
               <input v-model="completed" type="number" id="completed" name="completed" placeholder="Количество совершенных рейсов">
             </div>
           </div>
    
      <button type="submit">Зарегистрировать</button>
       
  </form>
  <br>
    <div>
      <div style="margin-top:1cm">
        <!--<a @click.prevent="goCatalogue">Каталог</a><br>-->
        <a @click.prevent="goHome">На главную</a>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
export default {
  name: 'Profile',

  data: () => ({
    editForm: {
      number: '',
      distance: '',
      departure: '',
      arrival: '',
      completed: ''
    },
  }),


  methods: {
    async signFlights () {
      
      $.ajax({
                type: "POST",
                data: {
                        number: this.number,
                        distance: this.distance,
                        departure: this.departure,
                        arrival: this.arrival,
                        completed: this.completed
                },
                url: "http://127.0.0.1:8000/schedule/create/"
            }).done(function () {
                console.log(this.data)
                //this.$router.push({ name: 'flights' })
            });
    },
   

    goHome () {
      this.$router.push({ name: 'home' })
    },

    //goEdit () {
      //this.$router.push({ name: 'profile_edit' })
    //}
  }
}
</script>

<style>

</style>
