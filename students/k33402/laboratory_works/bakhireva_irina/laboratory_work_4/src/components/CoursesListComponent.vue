<template>
    <v-data-table
            :items="courses"
            :headers="headers"
            class="elevation-1">
        <template v-slot:item.spec="{ item }">
            {{ getSpecializationName(item.raw.spec) }}
        </template>
        <template v-slot:item.required_spec="{ item }">
            {{ item.raw.required_spec ? getSpecializationName(item.raw.required_spec) : "-" }}
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
	{title: "Описание", key: "description"},
	{title: "Специализация", key: "spec"},
	{title: "Требуемая специализация", key: "required_spec"},
]
</script>
