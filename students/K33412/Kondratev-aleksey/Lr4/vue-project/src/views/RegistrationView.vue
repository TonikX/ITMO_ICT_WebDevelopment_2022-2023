<template>
  <header-block />
  <registration-block />
  <footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'

import useRegisterStore from '../stores/register'

import HeaderBlock from '../components/Header.vue'
import RegistrationBlock from '../components/Registration.vue'
import FooterBlock from '../components/Footer.vue'

export default{
  name: 'RegistrationPage',

  components: { HeaderBlock, RegistrationBlock, FooterBlock },

  computed: {
    ...mapState(useRegisterStore, ['users'])
  }
}
</script>
