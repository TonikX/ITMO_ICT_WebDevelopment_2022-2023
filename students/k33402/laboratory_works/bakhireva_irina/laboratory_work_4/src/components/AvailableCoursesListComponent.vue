<template>
    <v-data-table
            :items="courses"
            :headers="headers"
            class="elevation-1">
        <template v-slot:item.name="{ item }">
            {{ item.raw.course.name }}
        </template>
        <template v-slot:item.spec="{ item }">
            {{ getSpecializationName(item.raw.course.spec) }}
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

const props = defineProps(["courses"]);
const courses = computed(() => props["courses"]);

const headers = [
	{title: "Название", key: "name"},
	{title: "Специализация", key: "spec"},
	{title: "Дата начала", key: "start_date"},
	{title: "Дата окончания", key: "end_date"},
]
</script>
