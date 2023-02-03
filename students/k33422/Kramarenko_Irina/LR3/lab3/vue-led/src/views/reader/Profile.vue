<template>
  <div class="edit">
      <div>
        <h2>Личный кабинет</h2>
      </div>

      <h3>Форма регистрации работника</h3>

     <form @submit.prevent="signWorkers"
      ref="editForm"
      class="my-2">
      <div class="row">


        <div class="col-25">
          <label for="name">Имя</label>
        </div>
        <div class="col-75">
          <input v-model="name" type="text" id="name" name="name" placeholder="Имя">
        </div>
      </div>


      <div class="row">
        <div class="col-25">
          <label for="age">Возраст</label>
        </div>
        <div class="col-75">
          <input v-model="age" id="age" name="age" placeholder="Возраст">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="education">Образование</label>
        </div>
        <div class="col-75">
          <textarea v-model="education" id="education" name="education" placeholder="Образование"></textarea>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="work_exp">Опыт работы</label>
        </div>
        <div class="col-75">
          <input v-model="work_exp" id="work_exp" name="work_exp" placeholder="Опыт работы">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="passport">Паспортные данные</label>
        </div>
        <div class="col-75">
          <input v-model="passport" id="passport" name="passport" placeholder="Серия и номер">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="occupation">Должность</label>
        </div>
        <div class="col-75">
          <select v-model="occupation" id="occupation" name="occupation">
            <option value="COMMANDER">commander</option>
            <option value="RELIEF PILOT">relief pilot</option>
            <option value="NAVIGATOR">navigator</option>
            <option value="ATTENDANT">attendant</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="employer">Работодатель</label>
        </div>
        <div class="col-75">
          <select v-model="employer" id="employer" name="employer">
            <option value="S7">S7</option>
            <option value="POBEDA">Pobeda</option>
            <option value="AEROFLOT">Aeroflot</option>
            <option value="NORDSTAR">Nordstar</option>
          </select>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="status">Статус</label>
        </div>
        <div class="col-75">
          <select v-model="status" id="status" name="status">
            <option value="WORKING">working</option>
            <option value="RETIRED">retired</option>
            <option value="FIRED">fired</option>
          </select>
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
      name: '',
      age: '',
      education: '',
      work_exp: '',
      passport: '',
      occupation: '',
      employer: '',
      status: ''
    },
    //options: ['COMMANDER', 'RELIEF PILOT', 'NAVIGATOR', 'ATTENDANT'], ['S7', 'POBEDA', 'AEROFLOT', 'NORDSTAR'], ['WORKING', 'RETIRED', 'FIRED']
  }),


  methods: {
    async signWorkers () {
      
      $.ajax({
                type: "POST",
                data: {
                        name: this.name,
                        age: this.age,
                        education: this.education,
                        work_exp: this.work_exp,
                        passport: this.passport,
                        occupation: this.occupation,
                        employer: this.employer,
                        status: this.status,
                        access: false
                },
                url: "http://127.0.0.1:8000/airport/worker/create"
            }).done(function () {
                console.log(this.data)
                //this.$router.push({ name: 'workers' })
            });
    },
   

    goHome () {
      this.$router.push({ name: 'home' })
    },

  }
}
</script>

<style>

</style>
