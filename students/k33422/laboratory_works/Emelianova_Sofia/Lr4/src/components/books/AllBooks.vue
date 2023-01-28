<template>
    <div class="all-books">
        <h1>Все доступные книги</h1>
        <v-row v-if="!!bookList" class="justify-center mt-8">
            <Book v-for="value, index in bookList" :book="value" :bookName="index" />
        </v-row>
        <v-row v-else class="justify-center align-center mt-8 empty">
            <p>Не найдено книг</p>
        </v-row>
        <pre>{{ bookList }}</pre>
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

    const bookList = computed(() => store.getAllBooksSorted);
</script>

<style scoped>
    h1 {
        text-align: center;
    }
    .empty {
        min-height: 176px;
    }
</style>