<template>
	<h1 class="custom-colored-h1 mx-5">Отдых, веселье, семья - это всё про нас</h1>
	<p class="fig"><img src="../assets/image/pngwing.com.png" class="img" alt="..."></p>
	<section class="filtration">
		<div class="container justify-content-start">
			<div class="row mt-5 row mx-auto">
				<div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
					<select class="form-select-sm event-type" aria-label=".form-select-lg example">
						<option value="ALL">Выберите, чем хотите заняться</option>
						<option value="Активный отдых">Активный отдых</option>
						<option value="Театр">Театр</option>
					</select>
					</div>
					<div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
						<select class="form-select-sm region-type" aria-label=".form-select-lg example">
							<option value="ALL">Выберите район город</option>
							<option value="Петроградский">Петроградский</option>
							<option value="Московский">Московский</option>
							<option value="Приморский">Приморский</option>
						</select>
					</div>
					<form class = "search-form d-flex justify-content-end col-12 col-sm-2 col-lg-4 col-xl-6" @submit.prevent="filter">
						<button type="submit" id="search" class="btn btn-info btn-sm" style="background-color:#fcc149">Поиск</button>
					</form>
				</div>
			</div>
	</section>
	<section class="color-main container pt-5  row mx-auto " >
		<div class="col-12 col-xl-3 col-md-5 col-lg-5 note card theatre petroga everything card-color" v-for="card in filteredCards" :key="card.id">
			<note-block :mero="card.mero" :text="card.text" :data="card.data" :address="card.address" :metro="card.metro" :img="card.img" :id="card.id"/>
		</div>
	</section>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useCardsStore from '@/stores/cards'

import NoteBlock from '@/components/note-card.vue'

export default {
	name: 'MainBlock',

	components: { NoteBlock },

	computed: {
		...mapState(useCardsStore, ['cards']),
		filteredCards() { 
			if (this.selectedCards.length) { 
				return this.selectedCards; 
			} else { 
				return this.cards 
			} 
		}
	},

	methods: {
		...mapActions(useCardsStore, ['loadCards']),
		async filter() { 
			const eventT = document.querySelector('.event-type') 
			const cityT = document.querySelector('.region-type') 
			this.selectedCards = [] 

			console.log(eventT.value, cityT.value) 
			this.cards.forEach((card) => { 
				if ((eventT.value === card.category && cityT.value === card.category2) || (eventT.value === "ALL" && cityT.value === card.category2) || (eventT.value === card.category && cityT.value === "ALL")) { 
					this.selectedCards.push(card); 
				} 
			}) 
		}
	},
	data() {
		return {
			selectedCards: []
		}
	},
	mounted() {
		this.loadCards();
	}
}
</script>

<style>
	.fig {
		text-align: center;
	}
</style>