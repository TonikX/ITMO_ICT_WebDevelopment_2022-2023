<template>
    <v-data-table
            :items="education"
            :headers="headers"
            class="elevation-1">
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

const props = defineProps(["education"]);
const education = computed(() => props["education"]);

const headers = [
	{title: "Уровень образования", key: "education_level"},
	{title: "Описание", key: "description"},
	{title: "Дата начала", key: "start_date"},
	{title: "Дата окончания", key: "end_date"},
]
</script>
