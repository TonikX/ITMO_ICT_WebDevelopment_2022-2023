<template>
  <div class="notification">
    <Transition name="slide-fade">
      <v-card v-if="notification" class="pa-4 ma-2" :class="notification.type">
        <p>{{ notification.msg }}</p>
      </v-card>
    </Transition>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useAppStore } from '@/store/app';
const store = useAppStore();

const notification = computed(() => store.notification);
</script>

<style scoped>
.notification {
  z-index: 9999;
  position: fixed;
  width: 100%;
  top: 10px;
  display: flex;
  justify-content: center;
  pointer-events: none;
}

.v-card {
  max-width: 400px;
}

.v-card.info {
  background: rgb(152, 192, 253);
}

.v-card.error {
  background: rgb(253, 152, 152);
}
.slide-fade-enter-active {
  transition: all 0.15s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.15s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-100%);
  opacity: 0;
}
</style>