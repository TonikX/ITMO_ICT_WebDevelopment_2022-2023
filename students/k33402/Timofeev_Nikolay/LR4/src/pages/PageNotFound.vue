<template>
    <div class="container">
        <nav-bar></nav-bar>
        <section>
            <hr class="opacity-100 m-0" />
            <h1 class="d-flex p-2 justify-content-center">404</h1>
            <p class="lead d-flex justify-content-center">Page {{ this.$route.path }} not found</p>
            <div class="text-center">
                <a class="btn btn-primary text-center"
                    ><router-link class="text-white" to="/">Bring me home</router-link></a
                >
            </div>
            <hr class="opacity-100" />
        </section>
        <page-footer></page-footer>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PageFooter from "@/components/PageFooter.vue";

export default {
    components: { PageFooter, NavBar },
};
</script>
