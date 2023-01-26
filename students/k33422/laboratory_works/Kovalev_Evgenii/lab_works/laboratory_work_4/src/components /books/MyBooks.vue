<template>
  <div className="my-books">
    <h1>Мои взятые книги</h1>
    <v-row v-if="bookList.length > 0" className="justify-center mt-8">
      <Book v-for="value in bookList" :book="value"/>
    </v-row>
    <v-row v-else className="justify-center align-center mt-8 empty">
      <p>Не найдено книг</p>
    </v-row>
  </div>
</template>

<script setup>
import {computed, onMounted} from 'vue';
import {useAppStore} from '@/store/app';
import Book from './Book.vue';

const store = useAppStore();

onMounted(() => {
  store.getMyBooks();
})

const bookList = computed(() => store.myBooks);
</script>

<style scoped>
h1 {
  text-align: center;
}

.empty {
  min-height: 176px;
}
</style>
