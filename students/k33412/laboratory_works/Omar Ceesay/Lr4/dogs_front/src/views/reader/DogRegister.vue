<template>
  <div class="edit">
    <h3>Dog's registration</h3>
    <v-form
        @submit.prevent="signDogs"
        ref="editForm"
        class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
              label="Nickname"
              v-model="editForm.name"
              name="name"/>

          <v-select
              v-model="editForm.breed"
              :items="options"
              name="breed"
              label="breed"
          ></v-select>

          <v-text-field
              label="Age"
              v-model="editForm.age"
              name="age"
              type="number"/>

          <v-text-field
              label="Family"
              v-model="editForm.family"
              name="family"/>


          <v-text-field
              label="data owner"
              v-model="editForm.owner_data"
              name="owner_data"/>

          <v-btn type="submit" color="#ff6347" dark>Register</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile" style="text-decoration: none; color: #198754">Back</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import $ from "jquery";

export default {
  name: 'DogRegister',
  data: () => ({
    editForm: {
      //participant: Object,
      name: '',
      breed: '',
      age: '',
      family: '',
      owner_data: '',
      //club,

    },

    options: ['h', 'b', 't'],
    //participants:
  }),
  methods: {
    async signDogs() {
      console.log(1)

      $.ajax({
        type: "POST",
        data: {
          name: this.editForm.name,
          breed: this.editForm.breed,
          age: this.editForm.age,
          family: this.editForm.family,
          owner_data: this.editForm.owner_data
        },
        url: "http://127.0.0.1:8000/participants/"
      }).done(function () {
        console.log(this.data)
        alert("Собака добавлена")
        //this.$router.push({ name: 'participants' }) //сделать Participants.vue
      });
    },

    goProfile() {
      this.$router.push({name: 'profile'})
    },
  }
}

</script>
