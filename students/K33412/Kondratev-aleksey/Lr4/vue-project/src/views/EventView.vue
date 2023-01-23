<template>
	<header-block />
	<event-block />
	<footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import HeaderBlock from '../components/Header.vue'
import EventBlock from '../components/Event.vue'
import FooterBlock from '../components/Footer.vue'

export default{
	name: 'EventPage',

	components: { HeaderBlock, EventBlock, FooterBlock }
}
</script>
