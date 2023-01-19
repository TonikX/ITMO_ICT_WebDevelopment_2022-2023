<template>
    <a class="page-link" v-on:click="change(link, page)">{{ text }}</a>
</template>

<script>
export default {
    name: "PageLink",
    props: {
        page: Number,
        text: String,
        link: String,
        classes: String
    },

    methods: {
        change: function (link, page) {
            let params = new URLSearchParams()
            if (link != null) {
                params = new URLSearchParams(new URL(link).search)
            } else {
                params = new URLSearchParams(new URL(document.location).search)
                params.set('page', page)
            }
            window.location.href = `http://localhost:8080?${params.toString()}`
        }
    }
}
</script>
