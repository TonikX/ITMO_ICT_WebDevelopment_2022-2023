<template>
    <div class="container-fluid my-2 px-3 px-sm-3 px-md-4 px-lg-5">
        <div>
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSorting"
                    aria-expanded="false" aria-controls="collapseSorting" aria-label="collapse sorting">
                Filter
            </button>
        </div>
        <div class="collapse" id="collapseSorting">
            <hr>
            <div class="row">
                <!-- Sorting -->
                <div class="col-6 col-sm-6 col-md-4 col-lg-2 d-flex flex-column">
                    <p class="mb-1"><b>Sort</b></p>
                    <div class="btn-group-vertical my-1" role="group" aria-label="Button group with nested dropdown">
                        <SortingButton v-on:SelectSorting="ChangeSortingKey" v-for="sortingOption in sortingOptions" :key="sortingOption.key" :name="sortingOption.name" :id="sortingOption.id"/>
                    </div>
                    <OrderButton v-on:ChangeOrder="ChangeOrder" />
                </div>
                <!-- Filtering -->
                <div class="col-6 col-sm-6 col-md-8 col-lg-10 border-start">
                    <p class="mb-1"><b>Filter</b></p>
                    <div class="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-1">
                        <!-- Systems -->
                        <div class="col col-md-12 col-lg-3">
                            <p class="mb-1">Game Systems</p>
                            <GameSystemButton v-on:SelectGameSystem="SelectOption" v-for="gameSystem in gameSystems"
                                              :key="gameSystem.id" :name="gameSystem.name" :id="gameSystem.id"/>
                        </div>
                        <!-- Checkboxes -->
                        <div class="col col-md-12 col-lg-3">
                            <p class="mb-1">Show or not</p>
                            <FilterCheckbox v-on:SelectOption="SelectOption" v-for="checkbox in flagOptions" :key="checkbox.id" :name="checkbox.name" :id="checkbox.id" />
                        </div>
                        <!-- Container with Tags-->
                        <div class="col col-md-12 col-lg-6 col-xl-6">
                            <p id="tagsHeader" class="mb-1">Tags</p>
                            <div class="d-flex flex-row justify-content-between align-content-around flex-wrap h-100">
                                <TagButton v-on:SelectTag="SelectOption" v-for="tag in tags" :key="tag.id" :name="tag.name" :id="tag.id"/>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Search and Random Buttons -->
                <div class="col-12 d-flex justify-content-between mt-3">
                    <button type="button" class="btn btn-primary" @click="FilterScenarios">Search</button>
                </div>
            </div>
            <hr>
        </div>
    </div>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";

import GameSystemButton from "./GameSystemButton.vue";
import TagButton from "./TagButton.vue"
import SortingButton from "./SortingButton.vue";
import FilterCheckbox from "./FilterCheckbox.vue";
import OrderButton from "./OrderButton.vue";

import useGameSystemsStore from "../stores/game-systems";
import useTagsStore from "../stores/tags"
import useScenariosStore from "../stores/scenarios";

export default {
    name: "FilterMenu",

    components: {SortingButton, GameSystemButton, TagButton, FilterCheckbox, OrderButton},

    data() {
        return {
            options: {},
            sortingOptions: [{
                name: 'Name',
                id: 'name'
            }, {
                name: 'Likes',
                id: 'likes'
            }, {
                name: 'Date',
                id: 'publish_date'
            }],
            flagOptions: [{
                name: 'Adult',
                id: 'adult'
            }, {
                name: 'Finished',
                id: 'finished'
            }],
            ascendingSorting: true,
            currentSortingKey: 'name',
        }
    },

    computed: {
        ...mapState(useGameSystemsStore, ['gameSystems']),
        ...mapState(useTagsStore, ['tags']),
    },

    methods: {
        ...mapActions(useGameSystemsStore, ['loadGameSystems']),
        ...mapActions(useTagsStore, ['loadTags']),
        ...mapActions(useScenariosStore, ['filterScenarios', 'sortScenarios']),
        SelectOption: function (value, key) {
            this.options[key] = this.options[key] || [];

            if (this.options[key].includes(value)) {
                const index = this.options[key].indexOf(value);
                this.options[key].splice(index, 1)
            } else {
                this.options[key].push(value)
            }
        },
        FilterScenarios: function () {
            this.filterScenarios(this.options).then(() => {
                this.SortScenarios()
            })
        },
        ChangeSortingKey: function(key) {
            this.currentSortingKey = key
            this.SortScenarios()
        },
        ChangeOrder: function (order) {
            this.ascendingSorting = order
            this.SortScenarios()
        },
        SortScenarios: function () {
            this.sortScenarios(this.currentSortingKey, this.ascendingSorting)
        },
    },

    mounted() {
        this.loadGameSystems()
        this.loadTags()
    }
}
</script>

<style scoped>

</style>
