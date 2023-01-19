<template>
    <base-layout>
        <div class="mt-5">
            <div v-if="books.count > 0" class="row justify-content-evenly align-items-end mb-3" id="library">
                <div class="col col-10 col-sm-5 col-md-4 col-xl-2" v-for="book in books.results" :key="book.id">
                    <book-card :title="book.title" :author="book.author" :avg_rating="book.avg_rating"
                               :slug="book.slug" :image="book.image" :description="book.description" :genres="book.genres"></book-card>
                </div>
            </div>
            <div v-else class="mt-5">
                <div class=""></div>
                <h3 class="text-muted mt-5">Nothing found</h3>
            </div>
        </div>
        <div>
            <!-- <pagination :elems="books['count']" :next="books['next']"
                        :prev="books.previous"></pagination> -->
        </div>
    </base-layout>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBooksStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";
import BookCard from "@/components/BookCard.vue";
import Pagination from "@/components/Pagination.vue";

export default {
    name: "BooksPage",

    components: {Pagination, BaseLayout, BookCard},

    computed: {
        ...mapState(useBooksStore, ['books'])
    },

    methods: {
        ...mapActions(useBooksStore, ['loadBooks']),
    },

    mounted() {
        const params = new URLSearchParams(new URL(document.location).search)

        if (params) {

        }
        this.loadBooks(params)
    },
}
</script>

<style scoped>

</style>
