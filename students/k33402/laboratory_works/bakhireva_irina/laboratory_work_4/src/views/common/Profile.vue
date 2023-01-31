<template>
    <v-alert :text="error" v-if="error" type="error"/>
    <v-progress-circular indeterminate color="primary" v-if="!loaded"></v-progress-circular>
    <div v-if="loaded">
        <h1>Профиль</h1>
        <v-container class="my-6">
            <UserInfoComponent :user="profile"/>
        </v-container>
    </div>
</template>

<script setup>
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user";
import axios from "axios";
import {getError} from "@/utils";
import UserInfoComponent from "@/components/UserInfoComponent.vue";

const loaded = ref(false);
const error = ref("");
const router = useRouter()
const user = useUserStore();
const profile = ref({});

onMounted(() => {
	if (!user.isAuth) {
		user.updateToken();
		router.push({name: "Login"});
	}

	axios
		.get("/user/")
		.then(response => {
			profile.value = response.data;
		})
		.catch(axiosError => {
			if (axiosError.response.status === 401) {
				user.updateToken();
				router.push({name: "Login"});
			} else {
				error.value = getError(axiosError)
			}
		}).finally(() => loaded.value = true)
})

</script>
