<template>
    <h1>Выход из аккаунта</h1>
</template>

<script setup>
import {onMounted} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import axios from "axios";

const router = useRouter()
const user = useUserStore();

onMounted(() => {
	if (user.isAuth) {
		axios
			.post("/auth/token/logout/")
			.finally(() => {
				user.updateToken();
				router.push({name: "Login"});
			});
	}
});

</script>

