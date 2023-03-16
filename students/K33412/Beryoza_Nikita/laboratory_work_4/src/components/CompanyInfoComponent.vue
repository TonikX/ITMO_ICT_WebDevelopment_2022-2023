<template>
    <v-row v-for="header in headers" v-bind:key="header.key" class="border-t">
        <v-col class="font-weight-bold">{{ header.title }}</v-col>
        <v-col>{{ company[header.key] }}</v-col>
    </v-row>
</template>

<script setup>
import {computed} from "vue";

const props = defineProps(["company"]);
const company = computed(() => props["company"]);

const headers = [
	{title: "ID", key: "id"},
	{title: "Название", key: "name"},
	{title: "Адрес", key: "address"},
]
</script>
