<template>
  <div class="all-books">
    <h1>Все доступные книги</h1>
    <v-row v-if="bookList.length > 0" class="justify-center mt-8">
      <Book v-for="value in bookList" :book="value" />
    </v-row>
    <v-row v-else class="justify-center align-center mt-8 empty">
      <p>Не найдено книг</p>
    </v-row>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useAppStore } from '@/store/app';
import Book from './Book.vue';
const store = useAppStore();
onMounted(() => {
  store.getAllBooks();
})

const bookList = computed(() => store.allBooks.filter(v => !v.reader));
</script>

<style scoped>
h1 {
  text-align: center;
}
.empty {
  min-height: 176px;
}
</style>