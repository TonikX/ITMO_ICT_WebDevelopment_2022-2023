<template>
    <AuthenticatedWrapComponent>
        <v-alert v-if="error" :text="error" type="error"></v-alert>
        <v-progress-circular
                v-if="!loaded"
                color="primary"
                indeterminate/>
        <div v-if="loaded">
            <h1>Товары</h1>
            <v-text-field
                    v-model="product_search"
                    class="mt-3"
                    label="Поиск товара"
                    name="search"
            ></v-text-field>
            <v-data-table
                    :headers="headers"
                    :items="products"
                    :items-per-page="5"
                    class="elevation-1">
                <template v-slot:item.image_name="{ item }">
                    <img :src="`http://localhost:8000/static/${item.raw.image_name}`" height="200" width="200"/>
                </template>
            </v-data-table>
        </div>
    </AuthenticatedWrapComponent>
</template>

<script>
import AuthenticatedWrapComponent from "@/components/AuthenticatedWrapComponent.vue";
import {mapStores} from "pinia";
import {useAuthStore} from "@/store/auth";
import axios from "axios";

export default {
	name: "Products",
	components: {AuthenticatedWrapComponent},
	computed: {
		...mapStores(useAuthStore),
		products() {
			if (this.product_search)
				return this.products_raw.filter(product => product.name.toLowerCase().includes(this.product_search.toLowerCase()));
			return this.products_raw;
		}
	},
	created() {
		this.authStore.init();
	},
	data: () => ({
		error: "",
		loaded: false,
		product_search: "",
		products_raw: [],
		headers: [
			{title: "id", key: "id"},
			{title: "Изображение", key: "image_name", sortable: false},
			{title: "Наименование", key: "name"},
			{title: "Количество", key: "quantity"},
			{title: "Цена", key: "price"},
		]
	}),
	mounted() {
		axios
			.get("/products")
			.then(response => {
				this.products_raw = response.data;
				console.log("response", this.products_raw);
			})
			.catch(error => {
				if (error.response.status === 401) { // unauthorized
					this.authStore.resetToken();
					this.$router.push({name: "SignIn"});
				} else {
					this.error = error.response?.data || error.message || "Что-то пошло не так";
					console.log(error)
				}
			})
			.finally(() => {
				this.loaded = true;
			})
	},
}
</script>
