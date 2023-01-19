<template>
    <div class="d-flex">
        <input class="form-control flex-fill mx-3 white-bg" type="text" id="textSearch"
               placeholder="Search books..."
               aria-label="Search books...">
        <button class="btn btn-primary" aria-label="Search" type="submit"
                v-on:click="search()">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                 class="bi bi-search" viewBox="0 0 16 16">
                <path
                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    name: "SearchBar",
    methods: {
        search: function (event) {
            let text = document.querySelector('#textSearch').value
            const params = new URLSearchParams([['text', text]])
            window.location.href = `http://localhost:8080/?${params.toString()}`
        }
    }
}
</script>

<style scoped>

</style>
