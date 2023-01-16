<template>
    <v-container class="border my-6" v-for="vacancy in vacancys">
        <div class="header my-6">Вакансия</div>
        <VacancyInfoComponent :vacancy="vacancy"/>
        <div class="header my-6">Специализация</div>
        <v-list>
            <v-list-item v-for="spec in vacancy.specs" v-bind:key="spec.id">
                {{ getSpecializationName(spec) }}
            </v-list-item>
        </v-list>
        <div class="header my-6">Компания</div>
        <CompanyInfoComponent :company="vacancy.company"/>
        <div class="header my-6">HR</div>
        <HRInfoComponent :hr="vacancy.company.hr.user"/>
    </v-container>
</template>

<script setup>
import {computed} from "vue";
import CompanyInfoComponent from "@/components/CompanyInfoComponent.vue";
import HRInfoComponent from "@/components/HRInfoComponent.vue";
import VacancyInfoComponent from "@/components/VacancyInfoComponent.vue";
import {getSpecializationName} from "@/utils";

const props = defineProps(["vacancys"]);
const vacancys = computed(() => props["vacancys"]);

</script>

<style scoped>
.header {
    font-size: 18pt;
    font-weight: bold;
}
</style>
