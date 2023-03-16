<template>
	<div>
		<header-block />
		<mus-block />
		<footer-block />
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import HeaderBlock from '../components/Header.vue'
import MusBlock from '../components/Mus.vue'
import FooterBlock from '../components/Footer.vue'

export default{
	name: 'MusicPage',
	components: {HeaderBlock, MusBlock, FooterBlock}
}
</script>