<template>
	<header-block />
	<personal-block />
	<footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import HeaderBlock from '../components/Header.vue'
import PersonalBlock from '../components/Personal.vue'
import FooterBlock from '../components/Footer.vue'

export default {
	name: 'PersonalPage',

	components: { HeaderBlock, PersonalBlock, FooterBlock }
}
</script>