<template>
    <div v-if="weatherApiData.length" style="display: flex; flex-direction: row; flex-wrap: wrap; gap: 1rem; justify-content: space-evenly;">
        <div style="display: flex; flex-direction: row; width: fit-content;" v-for="(el, index) in weatherApiData" :key="index">
            <div>
                <h5 class="card-title">{{ Intl.DateTimeFormat("default", { weekday: "short", day: "numeric", }).format(el.dt) }}</h5>
                <p class="card-text">{{  Intl.NumberFormat("default", {style: "unit", unit: "celsius", maximumFractionDigits: 0 }).format(el.temp.day) }}</p>
                <!-- <p class="card-text">Температура днем: {{ el.temp.max }}</p> -->
                <!-- <p class="card-text">Температура вечером: {{ el.temp.min }}</p> -->
                <p class="card-text">{{ Intl.NumberFormat("default", {style: "unit", unit: "celsius", maximumFractionDigits: 0 }).format(el.temp.night) }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import moment from "moment";
    import {mapGetters} from "vuex";

    export default {
        name: "CityWeather",
        props: ['id', 'name', 'description', 'lat', 'lon'],
        methods: {
            moment: function (date) {
                return moment.utc(date*1000).format('ddd DD MMM');
            },
            getText: function (temp, description) {
                if (temp < 0) {
                    return `На улице ${description}, прохладно, одевайтесь теплее`
                } else {
                    return `На улице ${description}, довольно тепло`
                }
            }
        },
        computed: {
            ...mapGetters({
                weatherApiData: 'weatherApiData'}
                )
        },
        mounted() {
            this.$store.dispatch('getWeatherApiData', {name: this.name, lat: this.lat ,lon: this.lon})
        }
    }
</script>

<style scoped>
    .buttom-my {
        background-color: #DC143C !important;
        color: #000 !important;
        border:#DC143C !important;
    }
</style>
