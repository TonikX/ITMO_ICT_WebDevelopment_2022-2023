<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img :src="logo" class="my-3" contain height="200" />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Добро пожаловать в библиотеку <u>VueLib</u>
        </h1>

        <h4>Как попасть офлайн?</h4>
        <p class="subheading font-weight-regular">
          Библиотека работает с <u>10:00 - 22:00</u> ежедневно без перерывов и
          выходных. <br />Подробная информация о расположении в
          <a
            href="https://yandex.ru/maps/org/rossiyskaya_gosudarstvennaya_biblioteka/1009286515/?ll=37.609352%2C55.751265&z=17.09"
            target="_blank"
            >Яндекс.Картах</a
          >
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-5">Ваши возможности:</h2>

        <v-row justify="center" align-content="stretch">
          <!-- <a>
            Изменить или удалить личную информацию
            <v-btn v-if="auth" @click="LK()" text>
              <span class="mr-2">ЛК</span>
            </v-btn>
          </a>
          <a>
            Изменить или удалить личную информацию
            <v-btn v-if="auth" @click="LK()" text>
              <span class="mr-2">ЛК</span>
            </v-btn>
          </a>

          <a>
            Изменить или удалить личную информацию
            <v-btn v-if="auth" @click="LK()" text>
              <span class="mr-2">ЛК</span>
            </v-btn>
          </a> -->


          <!-- <a
            v-for="(next, i) in whatsNext"
            :key="i"
            :href="next.href"
            class="subheading mx-3"
            target="_blank"
          > -->
          <a
            v-for="(next, i) in whatsNext"
            :key="i"
            class="subheading mx-3"
            target="_blank"
          >
            {{ next.text }}
          </a>
          <!-- <v-btn v-if="auth" @click=" {{ next.method }}" text> 
            <span class="mr-2">{{ next.text }}</span>
          </v-btn> -->
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import logo from "../assets/logo.svg";

export default {
  name: "HomePage",

  computed: {
    auth() {
      var auth;
      if (localStorage.auth_token) {
        auth = true;
      }
      return auth;
    },
  },

  methods: {
    Books() {
      this.$router.push({ name: "Books" });
    },

    LK() {
      this.$router.push({ name: "Reader" });
    },
  },

  data: () => ({
    logo,
    whatsNext: [
      {
        text: "Изменить или удалить личную информацию",
        // href: window.location.href.replace("home", "") + "books",
      },
      {
        text: "Просмотреть все книг в библиотеке",
        // href: "https://vuetifyjs.com/introduction/roadmap/",
      },
      {
        text: "Забронировать или вернуть книгу",
        // href: "https://vuetifyjs.com/getting-started/frequently-asked-questions",
      },
    ],
  }),
};
</script>
