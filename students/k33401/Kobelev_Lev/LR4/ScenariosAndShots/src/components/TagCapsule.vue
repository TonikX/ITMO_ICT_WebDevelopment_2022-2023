<template>
    <span class="b-badge rounded-pill px-2 py-1 mx-1 my-1"> {{ name }} </span>
</template>

<script>
export default {
    name: "TagCapsule",

    props: {
        name: {
            type: String
        }
    }
}
</script>

<style scoped>
.b-badge {
    color: #333;
    background-color: var(--bs-light);
    font-weight: normal;
    font-size: x-small;
}
</style>
