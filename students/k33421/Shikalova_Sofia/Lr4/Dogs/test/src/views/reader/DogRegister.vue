<template>
   <div class="edit">
    <h3>Dog registration</h3>
      <v-form
      @submit.prevent="signDogs"
      ref="editForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
            label="Dog's name"
            v-model="editForm.name"
            name="name"/>

          <v-select
            v-model="editForm.breed"
            :items="options"
            name="breed"
            label="Breed"
          ></v-select>

          <v-text-field
            label="Age"
            v-model="editForm.age"
            name="age"
            type="number"/>

          <v-text-field
            label="Pedigree"
            v-model="editForm.family"
            name="family"/>


          <v-text-field
            label="Owner info"
            v-model="editForm.owner_data"
            name="owner_data"/>

            <v-btn type="submit" color="#283593" dark>Register the dog</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile" style="text-decoration: none; color: #283593">Back</a>
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
        async signDogs () {
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
                    alert("Registration succeed")
                    //this.$router.push({ name: 'participants' })
                });
        },
        
        goProfile () {
        this.$router.push({ name: 'profile' })
    },
    }
}

</script>