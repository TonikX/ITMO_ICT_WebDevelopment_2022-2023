<template>
	<div>
		<img :src="img" class="card-img-top" alt="..." width="354">
		<div class="card-body">
			<h2 class="card-title text-card">{{ mero }}</h2>
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
			<p class="card-text text-card">{{ text }}</p>
			<a href="#" @click="$router.push('/music/')" class="btn btn-dark button-color">Подробнее</a>
			<form @submit.prevent="addNote(id)">
				<button type="submit" class="btn btn-dark mt-3 button-color">
					<svg class="icon-main">
						<use xlink:href="#add"></use>
					</svg>
					Записаться
				</button>
			</form>
		</div>
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useUserEventsStore from '@/stores/userEvents'

export default {
	name: 'NoteBlock',

	props: {
    mero: {
      type: String,
      required: true
    },
    text: {
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
		id: {
			type: Number,
      required: true
		},
		img: {
			type: String,
      required: true
		},
  },

	computed: {
		...mapState(useUserEventsStore, ['userEvents']),
		
	},

	methods: {
		...mapActions(useUserEventsStore, ['addUserEvents']),
		async addNote(id) {
			const userEvents = {
				"userId": JSON.parse(localStorage.user).id,
				"eventId": id
			}
			console.log(userEvents)

			const response = await this.addUserEvents(userEvents);

			console.log(response)
		}
	}
}
</script>