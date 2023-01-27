<template>
    <div class="card border-0 white-bg p-0 mx-1 my-4" data-card-id="${id}" id="b${id}">
        <div class="d-none d-sm-block"><img :src="image" class="card-img-top" :id=slug></div>
        <div class="card-body">
            <p class="text-truncate h6 mb-0">
                <a v-on:click="show(slug)" href="#" data-bs-toggle="modal" data-bs-target="#bookModal"
                   class="text-decoration-none text-main text-truncate">{{ title }}</a>
            </p>
            <p class="text-muted text-truncate mb-0"><small>{{ author.name }}</small></p>
            <div class="row">
                <p v-if="avg_rating" class="col text-end text-main mb-0 mt text-danger small">
                    {{ avg_rating }}
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-star-fill" viewBox="0 0 16 16">
                        <path
                            d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                    </svg>
                </p>
                <p v-else class="col text-end text-main mb-0 mt-1 text-secondary small">
                    Unrated
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "BookCard",
    props: {
        author: {
            required: true
        },
        image: {
            required: false
        },
        avg_rating: {
            type: Number,
            required: false
        },
        title: {
            type: String,
            required: true
        },
        slug: {
            type: String,
            required: true
        },
    },
    methods: {
        show: function (slug) {
            window.location.href = `http://localhost:8080/book#${slug}`
        }
    },

    mounted() {
        const im = document.querySelector(`#${this.slug}`)
        if (this.image[0] === '/') {
            im.src = `http://localhost:4000${this.image}`
        }
    }
}
</script>

<style scoped>

</style>
