<template>
    <v-data-table
            :items="work_history"
            :headers="headers"
            class="elevation-1">
        <template v-slot:item.spec="{ item }">
            {{ item.raw.spec ? getSpecializationName(item.raw.spec) : "Получение пособия" }}
        </template>
        <template v-slot:item.start_date="{ item }">
            {{ new Date(Date.parse(item.raw.start_date)).toUTCString() }}
        </template>
        <template v-slot:item.end_date="{ item }">
            {{ item.raw.end_date ? new Date(Date.parse(item.raw.end_date)).toUTCString() : "-" }}
        </template>
    </v-data-table>
</template>

<script setup>
import {computed} from "vue";
import {getSpecializationName} from "@/utils";

const props = defineProps(["work_history"]);
const work_history = computed(() => props["work_history"]);

const headers = [
	{title: "Специальность", key: "spec"},
	{title: "Зарплата", key: "salary"},
	{title: "Дата начала", key: "start_date"},
	{title: "Дата окончания", key: "end_date"},
]
</script>
