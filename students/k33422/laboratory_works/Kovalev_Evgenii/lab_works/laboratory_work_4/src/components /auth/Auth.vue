<template>
  <v-sheet
      elevation="1"
      rounded="xl"
      class="pa-8"
  >
    <h1>Авторизация</h1>
    <v-form class="auth-form" ref="form">
      <v-text-field
          v-model="username"
          label="Имя пользователя"
          :rules="[v => !!v || 'Не заполнено']"
          required
          variant="underlined"
      ></v-text-field>
      <v-text-field
          v-model="password"
          label="Пароль"
          :rules="[v => !!v || 'Не заполнено']"
          required
          variant="underlined"
          :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="showPassword = !showPassword"
          :type="showPassword ? 'text' : 'password'"
          @keyup.enter="authorize"
      ></v-text-field>

      <v-btn
          color="success"
          class="mr-4 mt-8"
          @click="authorize"
          elevation="1"
      >
        Авторизоваться
      </v-btn>
      <v-btn
          color="primary"
          class="ml-4 mt-8"
          @click="switchMode"
          elevation="1"
      >
        Не зарегистрирован? Создать аккаунт
      </v-btn>
    </v-form>
  </v-sheet>

</template>

<script setup>
import { ref } from 'vue';
import { useAppStore } from '@/store/app';
const emit = defineEmits(['switchMode']);
const store = useAppStore();

const form = ref();
const password = ref('');
const username = ref('');
const showPassword = ref(false);

const authorize = async () => {
  const { valid } = await form.value.validate();
  if (!valid) {
    store.addNotification('error', 'Не все поля заполены правильно');
    return;
  }
  await store.userAuth(username.value, password.value);
}

const switchMode = () => {
  emit('switchMode');
}
</script>

<style>
</style>