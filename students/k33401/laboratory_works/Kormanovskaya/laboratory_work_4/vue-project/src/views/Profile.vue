<template>
    <div v-if="user">
        <div class="empty-div"></div>
        <div class="text-center">
            <h1 class="">{{ user.username }}</h1>
            <p class="mt-1 h6 text-primary" id="modalauthor"></p>
        </div>
        <div class="mt-5 w-100 mx-auto container">
            <div class="mt-5">
                <div v-if="user.reading_set.length" class="row justify-content-evenly align-items-end mb-3"
                     id="library">
                    <div class="col col-10 col-sm-5 col-md-4 col-xl-2" v-for="book in user.reading_set" :key="book.id">
                        <book-card :title="book.book.title" :author="book.book.author" :avg_rating="book.rate"
                                   :slug="book.book.slug" :image="book.book.image" :description="book.book.description"
                                   :genres="book.book.genres"></book-card>
                    </div>
                </div>
                <div v-else class="mt-5">
                    <div class=""></div>
                    <h3 class="text-muted mt-5">Your bookshelf is empty</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBooksStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";
import BookCard from "@/components/BookCard.vue";

export default {
    name: "Profile",
    components: {BaseLayout, BookCard},

    computed: {
        ...mapState(useBooksStore, ['token', 'user'])
    },

    methods: {
        ...mapActions(useBooksStore, ['loadUserinfo']),
    },

    async mounted() {
        if (!this.user) {
            window.location.href = 'http://localhost:8080/'
        }
        const response = await this.loadUserinfo(this.token)
        localStorage.user = response.data
    }
}
</script>

<style scoped>

</style>
