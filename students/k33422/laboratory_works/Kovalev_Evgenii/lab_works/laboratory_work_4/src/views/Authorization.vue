<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center justify-center text-center fill-height pa-6">
      <Auth v-if="isAuth" @switch-mode="switchMode" />
      <Register v-else @switch-mode="switchMode" />
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Auth from '@/components/auth/Auth.vue';
import Register from '@/components/auth/Register.vue';
import router from '@/router';

onMounted(() => {
  const user = localStorage.getItem('LIBRARY_USERNAME');
  const token = localStorage.getItem('LIBRARY_AUTH_TOKEN');
  if (user && token) {
    router.push('/');
    return;
  }
})

const isAuth = ref(true);

const switchMode = () => {
  isAuth.value = !isAuth.value;
}
</script>
