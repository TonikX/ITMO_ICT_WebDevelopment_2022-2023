<template>
	<main class="row mx-auto d-flex pt-5 color-main">
		<section class="container row mx-auto">
			<div class="row d-flex justify-content-start col-md-5 col-lg-5 col-xl-3 col-12 col-sm-12">
				<img src="../assets/image/я.jpg" alt="..." style="padding: 0;">
			</div>
			<div class="row d-flex justify-content-start col-xl-6 col-lg-7 col-md-7 col-9 col-sm-12">
				<ul>
					<h1 class="text mt-1 custom-colored-h1">Светлана Кулагина</h1>
					<h2 class="text mt-2 h5 custom-colored-h1">Участник с Марта 2022г</h2>
					<h3 class="text mt-2 h4 custom-colored-h1">Предпочтения: театры/выставки/искусство</h3>
					<h3 class="text mt-4 h4 custom-colored-h1">Страница вк:<a href="https://vk.com/pacsvet">https://vk.com/pacsvet</a></h3>
					<button type="button" class="btn btn-primary mt-5 button-color">Редактировать профиль</button>
				</ul>
			</div>
		</section>
		<section class="container row mx-auto" id="container">
			<h3 class="text mt-5 h4 custom-colored-h1">Выбранные мероприятия:</h3>
			<div class="col-12 col-xl-3 col-md-5 col-lg-5 mb-5 pt-5" v-for="card in personalCards" :key="card.id">
				<personal-cards :mero="card.mero" :data="card.data" :address="card.address" :metro="card.metro" :primaryId="card.primaryId"/>
			</div>
		</section>
	</main>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useUserEventsStore from '@/stores/userEvents'
import useCardsStore from '@/stores/cards'
import PersonalCards from '@/components/PersonalCards.vue'

export default {
	name: 'LkBlock',

	components: {PersonalCards},

	computed: {
		...mapState(useUserEventsStore, ['userEvents']),
		...mapState(useCardsStore, ['personalCards']),
		
	},

	methods: {
		...mapActions(useUserEventsStore, ['getUserEventsById']),
		...mapActions(useCardsStore, ['loadCardById', 'doClear']),

		async loadPage() {
			const response = await this.getUserEventsById(JSON.parse(localStorage.user).id); 
			const result = Array.from(response.data);

			this.doClear(); 
			result.forEach((item) => { 
				this.loadCardById(item.eventId, item.id) 
			}) 
		}
		
	},

	mounted() {
		this.loadPage()
	}
}
</script>