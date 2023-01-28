<template>
  <Notification />
  <router-view />  
</template>

<script setup>
  import Notification from './components/Notification.vue';
  import { ref, onMounted, reactive } from 'vue';
  import { useAppStore } from '@/store/app';
  import router from './router';
  const store = useAppStore();

  onMounted(async () => {
    const user = localStorage.getItem('LIBRARY_USERNAME');
    const token = localStorage.getItem('LIBRARY_AUTH_TOKEN')
    if (!user || !token) {
      router.push('/auth');
      return;
    }
    await store.getUserInfo();
  })
</script>
<style>
  #app {
    padding-top: 32px;
  }

  * {
    text-rendering: unset;
    -webkit-font-smoothing: unset;
  }
</style>
