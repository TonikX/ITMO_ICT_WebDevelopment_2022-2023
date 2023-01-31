<template>
    <v-app>
        <MenuComponent/>
        <v-main class="d-flex justify-center py-6">
            <div class="middle-block">
                <RouterView/>
            </div>
        </v-main>
    </v-app>
</template>

<style scoped>
.middle-block {
    width: 1000px;
}
</style>
<script setup>
import MenuComponent from "@/components/MenuComponent.vue";
</script>
