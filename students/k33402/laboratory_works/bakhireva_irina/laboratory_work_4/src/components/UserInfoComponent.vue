<template>
    <v-row v-for="header in headers" v-bind:key="header.key" class="border-b">
        <v-col class="font-weight-bold">{{ header.title }}</v-col>
        <v-col>{{ user[header.key] }}</v-col>
    </v-row>
</template>

<script setup>
import {computed} from "vue";

const props = defineProps(["user"]);
const user = computed(() => props["user"]);
const headers = [
	{title: "ID", key: "id"},
	{title: "Имя", key: "first_name"},
	{title: "Фамилия", key: "last_name"},
	{title: "Телефон", key: "phone"},
	{title: "Почта", key: "email"},
	{title: "Роль", key: "role"}
].filter(header => user.value[header.key] !== undefined);
</script>
