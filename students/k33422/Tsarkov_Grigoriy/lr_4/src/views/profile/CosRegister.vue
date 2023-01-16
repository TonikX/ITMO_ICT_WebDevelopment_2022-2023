<template>
   <div class="edit">
    <h3>Регистрация участника</h3>
      <v-form
      @submit.prevent="signCos"
      ref="editForm"
      class="my-2">
      <v-row>
        <v-col cols="5" class="mx-auto">

          <v-text-field
            label="Никнейм"
            v-model="editForm.name"
            name="name"/>

          <v-select
            v-model="editForm.fandom"
            :items="options"
            name="fandom"
            label="Фандом"
          ></v-select>

          <v-text-field
            label="Возраст"
            v-model="editForm.age"
            name="age"
            type="number"/>

          <v-text-field
            label="Персонаж"
            v-model="editForm.character"
            name="character"/>

            <v-btn type="submit" color="primary" dark>Зарегистрировать</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <v-card>
      <v-card-text style="margin-top:1cm">
        <a @click.prevent="goProfile">Назад</a>
      </v-card-text>
    </v-card>
   </div>
</template>

<script>
import $ from "jquery";
export default {
  name: 'CosRegister',
  data: () => ({
    editForm: {
      name: '',
      fandom: '',
      age: '',
      character: '',
    },

    options: ['n', 'h', 's', 'd'],
  }),
    methods: {
        async signCos () {
          console.log(1)
          $.ajax({
                    type: "POST",
                    data: {
                            name: this.editForm.name,
                            fandom: this.editForm.fandom,
                            age: this.editForm.age,
                            character: this.editForm.character
                    },
                    url: "http://127.0.0.1:8000/participants/"
                }).done(function () {
                    console.log(this.data)
                    alert("Участник добавлен")
                });
        },

        goProfile () {
        this.$router.push({ name: 'profile' })
        },
    }
}

</script>