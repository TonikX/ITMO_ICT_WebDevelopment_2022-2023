<template>
    <div class="text-start">
        <h6 class="mt-3">Reading status</h6>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="is_read" :checked="!!read">
            <label class="form-check-label" for="is_read">I have read this book</label>
        </div>
        <h6 class="mt-3">Rating</h6>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="null" v-model="ratevalue" id="rate0">
            <label class="form-check-label" for="rate0">
                Do not rate this time
            </label>
        </div>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="1" v-model="ratevalue" id="rate1">
            <label class="form-check-label" for="rate1">
                1
            </label>
        </div>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="2" v-model="ratevalue" id="rate2">
            <label class="form-check-label" for="rate2">
                2
            </label>
        </div>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="3" v-model="ratevalue" id="rate3">
            <label class="form-check-label" for="rate3">
                3
            </label>
        </div>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="4" v-model="ratevalue" id="rate4">
            <label class="form-check-label" for="rate4">
                4
            </label>
        </div>
        <div class="form-check" id="ratecheck">
            <input class="form-check-input" type="radio" :value="5" v-model="ratevalue" id="rate5">
            <label class="form-check-label" for="rate5">
                5
            </label>
        </div>
        <div class="mb-3">
            <h6 class="mt-3 ">Review</h6>
            <textarea class="form-control" v-model="reviewtext" id="review_text">{{ review }}</textarea>
        </div>
    </div>
    <button type="submit" class="btn btn-primary" v-on:click="update(token, false, ratevalue, reviewtext)">Update
    </button>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useLibraryStore from "@/stores/books";

export default {
    name: "UpdateBook",

    computed: {
        ...mapState(useLibraryStore, ['token', 'user'])
    },

    props: {
        rate: null,
        review: "",
        read: false,
        id: 0
    },

    data() {
        return {
            reviewtext: this.review,
            ratevalue: this.rate
        }
    },

    methods: {
        ...mapActions(useLibraryStore, ['loadUserinfo', 'updateBook']),

        update: async function (token, read, rate, review) {
            read = document.getElementById('is_read').checked
            const response = await this.updateBook(token, this.id, this.read, this.rate, this.review)
            const response2 = await this.loadUserinfo(token)
        }
    }

}
</script>

<style scoped>

</style>
