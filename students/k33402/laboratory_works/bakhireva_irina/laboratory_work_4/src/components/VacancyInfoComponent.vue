<template>
    <v-row v-for="header in headers" v-bind:key="header.key" class="border-t">
        <v-col class="font-weight-bold">{{ header.title }}</v-col>
        <v-col>{{
                header.key === "created_date"
                        ? new Date(Date.parse(vacancy.created_date)).toUTCString()
                        : vacancy[header.key]
            }}
        </v-col>
    </v-row>
</template>

<script setup>
import {computed} from "vue";

const props = defineProps(["vacancy"]);
const vacancy = computed(() => props["vacancy"]);

const headers = [
	{title: "ID", key: "id"},
	{title: "Требуемое образование", key: "education_level"},
	{title: "Стаж", key: "seniority"},
	{title: "Заработная плата", key: "salary"},
	{title: "Описание", key: "description"},
	{title: "Добавлена", key: "created_date"},
].filter(header => vacancy.value[header.key] !== undefined);
</script>
