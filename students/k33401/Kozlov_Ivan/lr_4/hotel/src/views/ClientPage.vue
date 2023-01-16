<template>
    <BaseLayout>
        <div class="d-flex justify-content-end ">
            <button type="button" class="btn btn-dark p-2 flex-grow-1 rounded-0"
                    data-bs-target="#add_client" data-bs-toggle="modal">Добавить клиента</button>
        </div>

        <table class="table table-hover table-bordered" style="color: rgb(0, 0, 0)" id="myTable">
            <thead>
            <tr>
                <th scope="col">Паспорт</th>
                <th scope="col">Телефон</th>
                <th scope="col">Почта</th>
                <th scope="col">Имя</th>
                <th scope="col">Фамилия</th>
                <th scope="col">Отчество</th>
                <th scope="col">Адрес</th>
                <th scope="col">Действия</th>
            </tr>
            </thead>
            <client-table
            v-for="clients in clients.results"
                v-bind:passport="clients.passport"
                v-bind:phone_client="clients.phone_client"
                v-bind:email_client="clients.email_client"
                v-bind:name="clients.name"
                v-bind:last_name="clients.last_name"
                v-bind:father_name="clients.father_name"
                v-bind:address="clients.address"
            >

            </client-table>

        </table>

    </BaseLayout>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import BaseLayout from "@/layouts/BaseLayout.vue";
import clientTable from "@/components/clientTable.vue";
import useClientStore from "@/stores/client";

export default {
    name: "ClientPage",
    components: {BaseLayout, clientTable},

    computed: {
        ...mapState(useClientStore, ['clients']),
    },

    methods: {
        ...mapActions(useClientStore, ["getClients"]),
    },

    mounted() {
        this.getClients()
    }

}
</script>

