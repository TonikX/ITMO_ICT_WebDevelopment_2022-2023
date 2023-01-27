<template>
    <nav aria-label="pagination">
        <ul class="pagination justify-content-center" id="pagination">
            <li v-for="page in P" :key="page.id" :class="page.classes">
                <page-link :text="page.text" :page="page.number" :classes="page.classes" :link="page.link"></page-link>
            </li>
        </ul>
    </nav>
</template>
<script>
import PageLink from "@/components/PageLink.vue";

export default {
    name: "Pagination",
    components: {PageLink},
    props: {
        page: Number,
        elems: Number,
        next: String,
        prev: String,
    },

    data() {
        const params = new URLSearchParams(new URL(document.location).search)
        let page = 1
        if (params) {
            if (params.has('page')) {
                page = Number(params.get('page'))
            }
        }
        let pages = []

        const pagesCount = Math.ceil(this.elems / 6)

        for (let i = 1; i <= pagesCount; i++) {
            console.log(i, page, i === page)
            pages.push(
                {
                    "number": i,
                    "text": i.toString(),
                    "link": null,
                    "classes": i === page ? "page-item disabled" : "page-item"
                }
            )
        }
        return {
            P: pages,
        }
    },
}
</script>
