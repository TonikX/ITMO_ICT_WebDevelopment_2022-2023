<template>
    <RouterView/>
</template>

<script setup>

import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import {onMounted} from "vue";

const router = useRouter()
const user = useUserStore();

onMounted(() =>
{
	if (!user.isApplicant) {
		user.updateToken();
		router.push({name: "Login"});
	}
})

</script>
