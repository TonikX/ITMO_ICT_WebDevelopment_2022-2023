<template>
	<div class="card card-color" data-card-id=${id} style="width: 18rem;">
		<div class="card-body">
			<h5 class="card-title text-card">{{ mero }}</h5>
			<p class="card-text text-card">{{ data }}</p>
			<p class="card-text text-card">
				<svg class="icon-main">
					<use xlink:href="#addr"></use>
				</svg>
				{{ address }}</p>
			<p class="card-text text-card">
				<svg class="icon-main">
					<use xlink:href="#metro"></use>
				</svg>
				{{ metro }}</p>
		<form action="" @submit.prevent="deleteCard(primaryId)"> 
			<button type="submit" class="btn btn-primary button-color">
				Отписаться
			</button> 
		</form>
		</div>
	</div>
</template>

<script> 
import { mapActions, mapState } from "pinia"; 

import useUserEventsStore from "@/stores/userEvents.js" 

export default { 
	name: 'PersonalCards', 

	computed: { 
		...mapState(useUserEventsStore, ['userEvents']), 
	}, 

	methods: {
		...mapActions(useUserEventsStore, ['addUserEvents', 'deleteCardById']),

		async deleteCard(id) {
			console.log('vbnm')
			this.deleteCardById(id)

			location.reload()
		}
	},

	props: {
		mero: {
			type: String,
			required: true
		},
		metro: {
			type: String,
			required: true
		},
		data: {
			type: String,
			required: true
		},
		address: {
			type: String,
			required: true
		},
		primaryId: {
			type: Number,
			required: true
		}
	}
}
</script>