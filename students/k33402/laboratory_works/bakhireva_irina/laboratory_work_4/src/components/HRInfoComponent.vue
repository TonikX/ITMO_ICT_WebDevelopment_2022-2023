<template>
    <v-row v-for="header in headers" v-bind:key="header.key" class="border-t">
        <v-col class="font-weight-bold">{{ header.title }}</v-col>
        <v-col>{{ hr[header.key] }}</v-col>
    </v-row>
</template>

<script setup>
import {computed} from "vue";

const props = defineProps(["hr"]);
const hr = computed(() => props["hr"]);
const headers = [
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
]
</script>
