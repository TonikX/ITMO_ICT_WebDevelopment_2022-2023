<template>
    <div class="empty-div"></div>
    <div class="text-center">
        <h1 class="">{{ book.title }}</h1>
        <p class="mt-1 h6 text-primary" id="modalauthor">{{ book.author.name }}</p>
    </div>


    <div class="mt-5 w-100 mx-auto container">
        <div class="row justify-content-between">
            <div class="col col-12 col-sm-6">
                <p>{{ book.description }}</p>
                <h5>Genres:</h5>
                <ul>
                    <li v-for="g in book.genre">
                        <genre-link :name="g.name" :slug="g.slug"></genre-link>
                    </li>
                </ul>

                <h5 v-if="book.avg_rating" class="mt-5" id="rated">
                    <span class="text-danger text-end">{{ book.avg_rating }}</span> / 5
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-star-fill" viewBox="0 0 16 16">
                        <path
                            d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                    </svg>
                </h5>
                <h5 v-else id="unrated">
                    <p class="text-main mb-0 mt-1 text-secondary">
                        Unrated
                    </p>
                </h5>
            </div>
            <div class="col col-11 col-sm-5">
                <img class="img-fluid img-thumbnail" id="modalimg" :src="book.image" alt="Book image">
            </div>

        </div>
        <div v-if="user" class="col col-11 mt-5 text-center">
            <div v-if="status">
                <p class="mb-5">Already on your shelf.</p>
                <update-book :read="read" :review="review" :rate="rate" :id="id"></update-book>
            </div>

            <div v-else class="">
                <button type="button" class="btn btn-outline-success mx-3" v-on:click="add(book.id, token, false)">Буду
                    читать
                </button>
                <button type="button" class="btn btn-success" v-on:click="add(book.id, token, true)">Прочитано</button>
            </div>
        </div>
    </div>

</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBooksStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";
import GenreLink from "@/components/GenreLink.vue";
import UpdateBook from "@/components/UpdateBook.vue";

export default {
    name: "BookPage",

    components: {BaseLayout, GenreLink, UpdateBook},

    computed: {
        ...mapState(useBooksStore, ['book', 'user', 'token'])
    },

    methods: {
        ...mapActions(useBooksStore, ['loadBook', 'addBook', 'loadUserinfo']),
        add: async function(id, token, read) {
            const response = await this.addBook(id, token, read)
            const response2 = await this.loadUserinfo(token)

            location.reload()
        }
    },

    data() {
        return {
            status: false,
            read: false,
            rate: null,
            review: "",
            id: 0
        }
    },

    mounted() {
        const slug = new URL(document.location).hash
        this.loadBook(slug.substring(1,))

        if (this.user) {

            for (const book of this.user.reading_set) {
                //console.log(book.book.slug, this.book.slug)
                if (book.book.slug === this.book.slug) {
                    this.status = true
                    this.read = book.is_read
                    this.rate = book.rate
                    this.review = book.review_text
                    this.id = book.book.id
                    break
                }
            }
        }
    },
}
</script>

<style scoped>

</style>
