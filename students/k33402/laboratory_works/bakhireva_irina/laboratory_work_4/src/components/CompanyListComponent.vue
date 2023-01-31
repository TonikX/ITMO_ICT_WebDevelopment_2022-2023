<template>
    <v-data-table
            :items="companys"
            :headers="headers"
            class="elevation-1">
        <template v-slot:item.info="{ item }">
            <v-btn
                    :to="{name: 'Company', params: { id: item.raw.id}}">
                Подробнее
            </v-btn>
        </template>
    </v-data-table>
</template>

<script setup>
import {computed} from "vue";

const props = defineProps(["companys"]);
const companys = computed(() => props["companys"]);

const headers = [
	{title: "ID", key: "id"},
	{title: "Название", key: "name"},
	{title: "", key: "info"}
]
</script>
