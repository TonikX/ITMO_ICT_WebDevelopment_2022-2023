<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cleanings</h1>

                <router-link to="/cleanings/create">Add cleaning</router-link>
                
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Clean room</th>
                            <th>Cleaner</th>
                            <th>Date time</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="cleaning in cleanings"
                            v-bind:key="cleaning.id">
                                <td>{{ cleaning.clean_room }}</td>
                                <td>{{ cleaning.cleaner_id }}</td>
                                <td>{{ cleaning.date_time }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Cleaning',
        data() {
            return {
                cleanings: []
            }
        },
        mounted() {
            this.getCleanings()
        },
        methods: {
            async getCleanings() {
                axios
                    .get('/hotel/cleanings/')
                    .then(response => {
                        this.cleanings = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>