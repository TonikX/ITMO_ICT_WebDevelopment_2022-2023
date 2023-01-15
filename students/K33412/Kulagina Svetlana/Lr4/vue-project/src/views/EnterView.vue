<template>
	<div>
		<header-block />
		<enter-block />
		<footer-block />
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useLoginStore from '../stores/login'

import HeaderBlock from '../components/Header.vue'
import EnterBlock from '../components/Enter.vue'
import FooterBlock from '../components/Footer.vue'

export default{
	name: 'EnterPage',
	components: {HeaderBlock, EnterBlock, FooterBlock},

	computed: {
		...mapState(useLoginStore, ['users'])
	}
}
</script>