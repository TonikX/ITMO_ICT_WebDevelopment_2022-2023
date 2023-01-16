<template>
</template>

<script setup>
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {onMounted} from "vue";

const router = useRouter()
const user = useUserStore();

onMounted(() => {
	if (user.isAuth) {
		switch (user.role) {
			case "Applicant":
				router.push({name: "Profile"});
				break;
			case "HR":
				router.push({name: "Profile"});
				break;
		}
	} else {
		user.updateToken();
		router.push({name: "Login"});
	}
})
</script>
