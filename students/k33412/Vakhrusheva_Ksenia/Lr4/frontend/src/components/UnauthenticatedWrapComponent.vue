<template>
    <TopBanner/>
    <UnauthenticatedMenuComponent/>
    <v-main>
        <v-container class="fill-height">
            <slot/>
        </v-container>
    </v-main>
    <FooterComponent/>
</template>

<script>
import FooterComponent from "@/components/FooterComponent.vue";
import TopBanner from "@/components/TopBanner.vue";
import UnauthenticatedMenuComponent from "@/components/UnauthenticatedMenuComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "UnauthenticatedWrapComponent",
	components: {UnauthenticatedMenuComponent, TopBanner, FooterComponent},
	computed: {
		...mapStores(useAuthStore),
	},
	created() {
		this.authStore.init();

		// Если авторизован, на начальную страницу. Иначе стираем заголовки
		if (this.authStore.isAuthenticated) {
			axios.defaults.headers.common["Authorization"] = `Token ${this.authStore.token}`;
			this.$router.push({name: "Staff"});
		} else {
			axios.defaults.headers.common["Authorization"] = "";
		}
	},
}
</script>
