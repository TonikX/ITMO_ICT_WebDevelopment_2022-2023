<template>
  <div class="edit">
      <div>
        <h2>Личный кабинет</h2>
      </div>

      <h3>Форма регистрации вашей собаки</h3>  

     <form @submit.prevent="signDogs"
      ref="editForm"
      class="my-2">
      <div class="row">


        <div class="col-25">
          <label for="fname">Кличка</label>
        </div>
        <div class="col-75">
          <input v-model="name" type="text" id="fname" name="name" placeholder="Кличка">
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="breed">Порода</label>
        </div>
        <div class="col-75">
          <select v-model="breed" id="breed" name="breed">
            <option value="h">haski</option>
            <option value="t">terrier</option>
            <option value="b">bulldog</option>
          </select>
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
          <label for="family">Родословная</label>
        </div>
        <div class="col-75">
          <textarea v-model="family" id="family" name="family" placeholder="Родословная"></textarea>
        </div>
      </div>

      <div class="row">
        <div class="col-25">
          <label for="owner_data">Данные хозяина</label>
        </div>
        <div class="col-75">
          <textarea v-model="owner_data" id="owner_data" name="owner_data" placeholder="Данные хозяина"></textarea>
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
      //participant: Object,
      name: '',
      breed: '',
      age: '',
      family: '',
      owner_data: '',
      //club
    },
    options: ['h', 'b', 't']
  }),


  methods: {
    async signDogs () {
      
      $.ajax({
                type: "POST",
                data: {
                        name: this.name,
                        breed: this.breed,
                        age: this.age,
                        family: this.family,
                        owner_data: this.owner_data
                },
                url: "http://127.0.0.1:8000/participants/"
            }).done(function () {
                console.log(this.data)
                //this.$router.push({ name: 'participants' }) //сделать Participants.vue
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
