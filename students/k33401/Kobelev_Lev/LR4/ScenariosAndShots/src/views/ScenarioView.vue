<template>
    <main>
        <scenario-layout class="mx-5 my-3">
            <div class="text-center">
                <h1> {{ selectedScenario.name }} </h1>
            </div>
            <div class="d-flex flex-row justify-content-center mb-2">
                <TagCapsule v-for="tag in selectedScenario.tags" :key="tag.id" :name="tag.name"/>
            </div>
            <div class="row">
                <div class="col col-6">
                    <img :src="selectedScenario.image" class="mx-auto d-block" alt="Scenario Image">
                </div>
                <div class="col col-6 align-middle">
                    <p class="pre-formatted">
                    {{ selectedScenario.full_description }}
                    </p>
                </div>
            </div>
            <hr>
            <div class="d-grid gap-3">
                <ReviewCard v-for="review in selectedScenario.reviews" :key="review.id" :text="review.text"
                            :author="review.author" :date="review.publish_date"/>
                <ReviewForm v-if="username" v-on:PostReview="PostScenarioReview" />
            </div>
        </scenario-layout>
    </main>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useScenariosStore from '../stores/scenarios'
import useUserStore from "../stores/user"

import ScenarioLayout from '../layouts/ScenarioLayout.vue'
import TagCapsule from "../components/TagCapsule.vue"
import ReviewCard from "../components/ReviewCard.vue";
import ReviewForm from "../components/ReviewForm.vue";

export default {
    name: "ScenarioView",
    components: {ScenarioLayout, TagCapsule, ReviewCard, ReviewForm},
    computed: {
        ...mapState(useScenariosStore, ['selectedScenario']),
        ...mapState(useUserStore, ['username', 'authToken']),
        scenarioId() {
            return this.$route.params.id;
        }
    },

    methods: {
        ...mapActions(useScenariosStore, ['loadScenarioById', 'createScenarioReview']),
        PostScenarioReview: function (text) {
            this.createScenarioReview(text, this.scenarioId, this.authToken)
            this.loadScenarioById(this.scenarioId)
        },
    },

    mounted() {
        this.loadScenarioById(this.scenarioId)
    }
}
</script>

<style scoped>
.pre-formatted {
    white-space: pre-wrap;
}
</style>
