<!--<template>-->
<!--<div>-->
<!--    <div-->
<!--      elevation="2"-->
<!--      outlined-->
<!--      class="my-2"-->
<!--    >-->
<!--      <div>-->
<!--        <h2>Личный кабинет</h2>-->
<!--      </div>-->

<!--      <br>-->
<!--      <h3>Форма регистрации участника</h3>-->
<!--     <v-form @submit.prevent="signParticipant">-->

<!--      <div class="row">-->
<!--        <div class="col-25">-->
<!--          <label for="fname">Никнейм</label>-->
<!--        </div>-->
<!--        <div class="col-75">-->
<!--          <input v-model="name" type="text" id="fname" name="name" placeholder="Никнейм">-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="row">-->
<!--        <div class="col-25">-->
<!--          <label for="fandom">Фандом</label>-->
<!--        </div>-->
<!--        <div class="col-75">-->
<!--          <select v-model="fandom" id="fandom" name="fandom">-->
<!--            <option value="n">n</option>-->
<!--            <option value="s">s</option>-->
<!--            <option value="h">h</option>-->
<!--            <option value="d">d</option>-->
<!--          </select>-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="row">-->
<!--        <div class="col-25">-->
<!--          <label for="age">Возраст</label>-->
<!--        </div>-->
<!--        <div class="col-75">-->
<!--          <input v-model="age" id="age" name="age" placeholder="Возраст">-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="row">-->
<!--        <div class="col-25">-->
<!--          <label for="character">Персонаж</label>-->
<!--        </div>-->
<!--        <div class="col-75">-->
<!--          <textarea v-model="character" id="character" name="character" placeholder="Персонаж"></textarea>-->
<!--        </div>-->
<!--      </div>-->

<!--      <button type="submit">Зарегистрировать</button>-->

<!--  </v-form>-->
<!--    </div>-->
<!--  <br>-->

<!--    <div>-->
<!--      <div style="margin-top:1cm">-->
<!--        <a @click.prevent="goHome">На главную</a>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import $ from "jquery";-->
<!--export default {-->
<!--  name: 'Profile',-->

<!--  data () {-->
<!--    return {-->
<!--      //participant: Object,-->
<!--      name: '',-->
<!--      fandom: '',-->
<!--      age: Number,-->
<!--      character: ''-->
<!--    }-->
<!--  },-->

<!--  methods: {-->
<!--    async signParticipant () {-->
<!--      -->
<!--      $.ajax({-->
<!--                type: "POST",-->
<!--                data: {-->
<!--                        name: this.name,-->
<!--                        fandom: this.fandom,-->
<!--                        age: this.age,-->
<!--                        character: this.character-->
<!--                },-->
<!--                url: "http://127.0.0.1:8000/participants/"-->
<!--            }).done(function () {-->
<!--                console.log(this.data)-->
<!--                //this.$router.push({ name: 'participants' }) //сделать Participants.vue-->
<!--            });-->
<!--    },-->

<!--    goHome () {-->
<!--      this.$router.push({ name: 'home' })-->
<!--    },-->

<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->

<!--</style>-->

<template>
  <div class="edit">
    <h2>Редактирование профиля</h2>
    <v-form
      @submit.prevent="saveChanges"
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
            :items="fandomOptions"
            name="fandom"
            label="Фандом"
          ></v-select>

          <v-text-field
            label="Возраст"
            v-model="editForm.age"
            name="age"/>

          <v-text-field
            label="Персонаж"
            v-model="editForm.character"
            name="character"/>

          <v-btn type="submit" color="primary" dark>Сохранить</v-btn>
        </v-col>
      </v-row>
    </v-form>
    <p class="mt-15"><router-link to="/cosplays/profile">Назад</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'Profile',

  data: () => ({
    editForm: {
      name: '',
      fandom: '',
      age: '',
      character: '',
    },
    fandomOptions: ['h', 'n', 'd', 's']
  }),

  created () {
    this.loadReaderData()
  },

  methods: {
    async loadReaderData () {
      const response = await this.axios
        .get('http://127.0.0.1:8000/participants/', {
          headers: {
            Authorization: `Token ${sessionStorage.getItem('auth_token')}`
          }
        })
      this.reader_old = response.data

      this.editForm.name = response.data.name
      this.editForm.fandom = response.data.fandom
      this.editForm.age = response.data.age
      this.editForm.character = response.data.character
    },

    async saveChanges () {
      for (const [key, value] of Object.entries(this.editForm)) {
        if (value === '') {
          delete this.editForm[key]
        }
      }

      try {
        const response = await this.axios
          .patch('http://127.0.0.1:8000/participants/',
            this.editForm, {
              headers: {
                Authorization: `Token ${sessionStorage.getItem('auth_token')}`
              }
            })
        console.log(response)

        this.$refs.editForm.reset()
        await this.$router.push({ name: 'profile' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.name) {
          alert('Имя: ' + e.response.data.name)
        } else {
          console.error(e.message)
        }
      }
    }
  }
}
</script>

<style>
</style>
