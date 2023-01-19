<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <div class="row w-100 align-items-center">
                <div class="col col-lg-8 d-none d-lg-flex">
                    <div class="d-flex flex-row flex-wrap justify-content-evenly" id="navGenres">
                        <div class="p-1 mx-2" v-for="genre in genres.results" :key="genre.id">
                            <genre-link :name="genre.name" :slug="genre.slug"></genre-link>
                        </div>
                    </div>
                </div>
                <div class="col col-lg-4 p-2 text-end">
                    <search-bar></search-bar>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useLibraryStore from "@/stores/books";
import BaseLayout from "@/layouts/BaseLayout.vue";
import GenreLink from "@/components/GenreLink.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
    name: "NavbarGenres",

    components: {SearchBar, BaseLayout, GenreLink},

    computed: {
        ...mapState(useLibraryStore, ['genres'])
    },

    methods: {
        ...mapActions(useLibraryStore, ['loadGenres'])
    },

    mounted() {
        this.loadGenres()
    }
}
</script>

<style scoped>

</style>
