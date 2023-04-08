<template>
    <b-card no-body>
        <b-tabs lazy card style="width: 100%;">
            <div v-for="(el, index) in userCity" :key="el.index" class="display: flex; flex-direction: row;">
                <b-tab :title="el.city.name" :active="index === 0" style="width;">
                    
                    <div class="container" style="margin-bottom: 1.5rem;">
                        <CityWeather :id="el.id" :name="el.city.name" :description="el.city.description" :lat="el.city.lat" :lon="el.city.lon" />
                    </div>
                    <div class="d-flex justify-content-between mx-5">
                        <!-- <p class="mb-0">{{el.city.description}}</p> -->
                        <b-button class="buttom-my" v-on:click="removeCity(el.id)" variant="danger">Открепить город</b-button>
                    </div>
                </b-tab>
            </div>
        </b-tabs>
    </b-card>
</template>

<script>
    import {mapGetters} from "vuex";
    import CityWeather from "@/components/CityWeather";

    export default {
        name: "Tab",
        components: {CityWeather},
        computed: {
            ...mapGetters({
                userCity: 'userCity',
            })
        },
        mounted() {
            this.$store.dispatch('getUserCities')
        },
        methods: {
            removeCity(val) {
                this.$store.dispatch('delUserCity', val)
            }
        },
    }
</script>

<style scoped>
    .buttom-my {
        background-color: #DC143C !important;
        color: #000 !important;
        border:#DC143C !important;
    }
</style>