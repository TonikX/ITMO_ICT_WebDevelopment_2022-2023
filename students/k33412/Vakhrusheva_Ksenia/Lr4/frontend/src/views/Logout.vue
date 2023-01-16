<template>
    <AuthenticatedWrapComponent>
        <h1>Выход из аккаунта</h1>
    </AuthenticatedWrapComponent>
</template>

<script>
import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "Logout",
	components: {AuthenticatedWrapComponent},
	computed: {
		...mapStores(useAuthStore),
	},
	mounted() {
		axios
			.post("/auth/token/logout")
			.finally(() => {
				this.authStore.resetToken();
				this.$router.push({name: "SignIn"});
			})

	}
}
</script>
