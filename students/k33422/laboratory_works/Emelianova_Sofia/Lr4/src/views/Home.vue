<template>
  <MyBooks />
  <UserEdit />
</template>

<script setup>
  import { ref, onMounted, reactive } from 'vue';
  import MyBooks from '@/components/books/MyBooks.vue';
  import UserEdit from '@/components/UserEdit.vue';
  import { useAppStore } from '@/store/app';
  const store = useAppStore();

  
  onMounted(async () => {
    await store.getUserInfo();
  })
</script>
