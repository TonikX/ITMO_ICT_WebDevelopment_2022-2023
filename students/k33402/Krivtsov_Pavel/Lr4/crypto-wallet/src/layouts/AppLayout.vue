<template>
  <component :is="layout">
    <slot />
  </component>
</template>

<script>
import DefaultLayout from "./DefaultLayout.vue";
import {shallowRef, watch} from 'vue'
import { useRoute } from 'vue-router'
export default {
  name: 'AppLayout',
  setup() {
    const layout = shallowRef(DefaultLayout)
    const route = useRoute()
    watch(
      () => route.meta,
      async meta => {
        try {
          const component = await import(`../layouts/${meta.layout}.vue`)
          layout.value = component?.default || DefaultLayout
        } catch (e) {
          layout.value = DefaultLayout
        }
      },
      { immediate: true }
    )
    return { layout }
  }
}
</script>
