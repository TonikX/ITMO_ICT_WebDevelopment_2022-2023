<template>
	<div>
		<header-block />
		<lk-block />
		<footer-block />
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import HeaderBlock from '../components/Header.vue'
import LkBlock from '../components/Lk.vue'
import FooterBlock from '../components/Footer.vue'

export default{
	name: 'LkPage',
	components: {HeaderBlock, LkBlock, FooterBlock}
}
</script>