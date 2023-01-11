<template>
  <v-app-bar
      color="white"
  >
    <template v-slot:prepend>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </template>

    <v-app-bar-title>Library App - <b>{{ pageName }}</b></v-app-bar-title>
    <v-spacer></v-spacer>
    <v-btn @click="logOut">Выход</v-btn>
  </v-app-bar>
  <v-navigation-drawer
      v-model="drawer"
      location="left"
      temporary
  >
    <h3 class="ml-4 mt-4">Страницы</h3>
    <v-list
    >
      <v-list-item
          v-for="item in items"
          :key="item.title"
          :title="item.title"
          :to="item.value"
          :subtitle="item.subtitle"
          :active="path == item.value"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useAppStore } from '@/store/app';
const store = useAppStore();
const route = useRoute();
const drawer = ref(false);
const items = reactive([
  {
    title: 'Мои книги',
    subtitle: 'Посмотреть мои книги',
    value: '/',
  },
  {
    title: 'Книги в библиотеке',
    subtitle: 'Взять книгу в библиотеке',
    value: '/books',
  },
]);

const path = computed(() => route.path)
const pageName = computed(() => route.name)

const logOut = () => {
  store.logOut();
}
</script>
