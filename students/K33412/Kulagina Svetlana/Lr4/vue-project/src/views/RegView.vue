<template>
	<div>
		<reg-block />
	</div>
</template>

<script>
import {mapActions, mapState} from 'pinia'

import useRegisterStore from '../stores/register'
import RegBlock from '../components/Reg.vue'

export default{
	name: 'RegPage',
	components: { RegBlock},
	
	computed: {
		...mapState(useRegisterStore, ['users'])
	}
}
</script>