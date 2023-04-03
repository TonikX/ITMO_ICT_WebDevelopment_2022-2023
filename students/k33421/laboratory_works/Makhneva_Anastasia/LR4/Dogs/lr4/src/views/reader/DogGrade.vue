<template>
  <div class="edit">
    <h3>оценка собаки</h3>
    <v-form
      @submit.prevent="signPart" 
      ref="editFormPart"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">
          
          <v-select
            v-model="editFormPart.participant"
            :items="participants"
            item-text="name"
            item-value="id"
            name="participant"
            label="участник"
          ></v-select>

          <v-select
            v-model="editFormPart.medal"
            :items="medals"
            name="medal"
            label="медаль"
          ></v-select>

          <v-text-field
            label="дата вакцинации"
            v-model="editFormPart.vaccinated"
            name="vaccinated"
            type="date"/>

          <v-checkbox
            v-model="editFormPart.dismissed"
            :label="'пропуск участия'"
          ></v-checkbox>


          <v-text-field
            label="оценка"
            v-model="editFormPart.final_grade"
            type='number'
            name="final_grade"/>

            <v-btn type="submit" color="#2e061a" dark>Оценить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile" style="text-decoration: none; color: #2e061a">назад</a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import $ from "jquery";
const array1 = [];
import axios from "axios";

export default {
  name: 'DogGrade',
  data: () => ({

    editFormPart: {
      medal: "",
      vaccinated: "",
      dismissed: "",
      final_grade: "",
      participant: "",
    },

    medals: ['g', 's', 'b'],
    participants: array1, 
  }),
    methods: {
        
        async signPart () {
            console.log(1)
        
        $.ajax({
                    type: "POST",
                    data: {
                            medal: this.editFormPart.medal,
                            vaccinated: this.editFormPart.vaccinated,
                            dismissed: this.editFormPart.dismissed,
                            final_grade: this.editFormPart.final_grade,
                            participant: this.editFormPart.participant,
                    },
                    url: "http://127.0.0.1:8000/participation/"
                }).done(function () {
                    console.log(this.data)
                    alert("готово")
                    //this.$router.push({ name: 'participants' }) //сделать Participants.vue
                });
        },

        goProfile () {
        this.$router.push({ name: 'profile' })
    }
    },
      beforeMount: function () {
        this.$nextTick(async function () {
            const response = await axios.get('http://127.0.0.1:8000/participants/?format=json')
            for (let part of response.data) {
                array1.push(part);
      }
    })
  }
        
}


</script>
