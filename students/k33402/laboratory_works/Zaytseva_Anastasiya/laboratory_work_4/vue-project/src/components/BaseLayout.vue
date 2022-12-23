<template>
<div>
  <SvgSprite />
  <AuthModals />
  <CartModal />
  <TheHeader />
  <hr class="opacity-100 m-0" />
  <slot></slot>
  <TheFooter />
</div>
</template>

<script setup>
import SvgSprite from '@/components/SvgSprite.vue';
import AuthModals from '@/components/AuthModals.vue';
import CartModal from '@/components/CartModal.vue';
import TheFooter from '@/components/TheFooter.vue';
import TheHeader from '@/components/TheHeader.vue';
</script>