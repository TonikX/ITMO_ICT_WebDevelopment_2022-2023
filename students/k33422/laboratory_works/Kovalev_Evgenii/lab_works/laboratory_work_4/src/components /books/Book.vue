<template>
  <v-card class="pa-4 ma-2 book">
    <v-card-item>
      <v-card-title v-if="bookName">{{ bookName }}</v-card-title>
      <v-card-title v-else>{{ book.book }}</v-card-title>
      <v-card-subtitle v-if="bookName">{{ book.length }} книг(-и) в наличии </v-card-subtitle>
      <v-card-subtitle v-else v-for="value in book.reading_rooms">{{ value }} </v-card-subtitle>
      <v-card-text class="mt-6">
        <v-row v-if="bookName" class="align-center">
          <p>{{ book.length <= 1 ? 'Книгу нельзя взять' : 'Книгу можно взять' }}</p>
          <v-spacer></v-spacer>
          <v-btn @click="bookTake" color="success" class="ml-4 elevation-0" :disabled="book.length <= 1">Взять</v-btn>
        </v-row>
        <v-row v-else class="align-center">
          <p>Книга взята <b>{{ book.own_date }}</b></p>
          <v-spacer></v-spacer>
          <v-btn @click="bookReturn" color="success" class="ml-4 elevation-0">Вернуть</v-btn>
        </v-row>
      </v-card-text>
    </v-card-item>
  </v-card>
</template>

<script setup>
import { useAppStore } from '@/store/app';
const store = useAppStore();
const props = defineProps({
  book: Object,
  bookName: String
})

const bookTake = async () => {
  await store.bookTake(props.bookName);
}

const bookReturn = async () => {
  await store.bookReturn(props.book.book);
}
</script>

<style scoped>
.book {
  max-width: 400px;
}
</style>
