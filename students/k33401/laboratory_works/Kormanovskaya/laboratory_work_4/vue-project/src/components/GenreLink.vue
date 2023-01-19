<template>
    <a href="#" v-on:click="show(slug)" class="text-decoration-none text-main bg-accent p-1">{{ name }}</a>
</template>

<script>
export default {
    name: "GenreLink",
    props: {
        name: {
            type: String,
            required: true
        },
        slug: {
            type: String,
            required: true
        }
    },
    methods: {
        show: function (slug) {
            const params = new URLSearchParams([['genre', slug]])
            window.location.href = `http://localhost:8080/?${params.toString()}`
        }
    }
}


</script>

<style scoped>

</style>
