<template>
	<div>
		<header-block />
		<main class=" pt-5 color-main pb-5">
			<main-block />
		</main>
		<footer-block />
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useCardsStore from '@/stores/cards'

import HeaderBlock from '../components/Header.vue'
import MainBlock from '../components/Main.vue'
import FooterBlock from '../components/Footer.vue'

export default{
	name: 'MainPage',
	components: {HeaderBlock, MainBlock, FooterBlock},

	computed: {
		...mapState(useCardsStore, ['cards']),
	},
	methods: {
		...mapActions(useCardsStore, ['loadCards']),
	}
}
</script>