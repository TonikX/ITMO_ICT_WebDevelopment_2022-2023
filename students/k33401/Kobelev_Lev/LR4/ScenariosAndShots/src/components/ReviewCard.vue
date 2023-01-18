<template>
    <div class="p-3 pb-0">
        <p>{{ text }}</p>
        <p>by <i>{{ author }}</i>, {{ date }}</p>
    </div>
</template>

<script>
export default {
    name: "ReviewCard",

    props: {
        author: String,
        text: String,
        date: String
    }
}
</script>

<style scoped>
div {
    background: var(--bs-light);
    min-height: 5em;
}
</style>
