<template>
    <form @submit.prevent="PostReview">
        <input type="text" class="form-control w-100 h-100" id="reviewText" placeholder="your review..."
               v-model="text">
    </form>
</template>

<script>
export default {
    name: "ReviewForm",

    data() {
        return {
            text: ''
        }
    },
    methods: {
        PostReview() {
            this.$emit('PostReview', this.text)
            this.text = ''
        }
    }
}
</script>

<style scoped>
form {
    min-height: 5em;
}
input {
    border-color: var(--bs-light);
    border-width: 0.3em;
}
</style>
