<template>
    <TopBanner/>
    <AuthenticatedMenuComponent/>
    <v-main>
        <v-container class="fill-height">
            <slot/>
        </v-container>
    </v-main>
    <FooterComponent/>
</template>

<script>
import FooterComponent from "@/components/FooterComponent.vue";
import AuthenticatedMenuComponent from "@/components/AuthenticatedMenuComponent.vue";
import TopBanner from "@/components/TopBanner.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "AuthenticatedWrapComponent",
	components: {TopBanner, AuthenticatedMenuComponent, FooterComponent},
	computed: {
		...mapStores(useAuthStore),
	},
	created() {
		this.authStore.init();

		// Если авторизован, просто ставим заголовки. Иначе на авторизацию пускаем
		if (this.authStore.isAuthenticated) {
			axios.defaults.headers.common["Authorization"] = `Token ${this.authStore.token}`;
		} else {
			axios.defaults.headers.common["Authorization"] = "";
			this.$router.push({name: "SignIn"});
		}
	},
}
</script>
