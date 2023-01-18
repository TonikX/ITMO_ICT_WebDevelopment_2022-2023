<template>
    <main>
        <FilterMenu/>
        <cards-layout>
            <div class="container-fluid px-3 px-sm-3 px-md-4 px-lg-5">
                <div v-if="scenarios.length"
                     class="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-2">
                    <div class="col" v-for="scenario in scenarios" :key="scenario.id">
                        <scenario-card v-on:SetLike="LikeScenario" :name="scenario.name"
                                       :author="scenario.author.username" :image="scenario.image"
                                       :description="scenario.short_description" :likes="scenario.likes" :liked="scenario.liked"
                                       :tags="scenario.tags" :username="username" :id="scenario.id"/>
                    </div>
                </div>
                <div v-else class="nothing-container">
                    Oops! Nothing found :(
                    <br>
                    try another search options
                </div>
            </div>
        </cards-layout>
    </main>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useScenariosStore from '../stores/scenarios'
import useUserStore from "../stores/user"

import CardsLayout from '../layouts/CardsLayout.vue'
import ScenarioCard from "../components/ScenarioCard.vue"
import FilterMenu from "../components/FilterMenu.vue"

export default {
    name: "HomeView",

    components: {FilterMenu, CardsLayout, ScenarioCard},

    computed: {
        ...mapState(useScenariosStore, ['scenarios']),
        ...mapState(useUserStore, ['username', 'authToken'])
    },

    methods: {
        ...mapActions(useScenariosStore, ['loadScenarios', 'likeScenario']),
        LikeScenario: function (id) {
            this.likeScenario(id, this.authToken)
        },
    },

    mounted() {
        this.loadScenarios(this.authToken)
    }
}
</script>

<style>
.nothing-container {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: xx-large;
    font-weight: normal;
}
</style>
