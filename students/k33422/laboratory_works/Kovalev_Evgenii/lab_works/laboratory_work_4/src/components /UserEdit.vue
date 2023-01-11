<template>
  <div v-if="userModel" class="mt-16 user-info">
    <h1>Изменить свою информацию</h1>
    <v-text-field
        v-model="password"
        label="Password"
        required
        variant="underlined"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        @click:append="showPassword = !showPassword"
        :type="showPassword ? 'text' : 'password'"
    ></v-text-field>
    <v-text-field
        v-model="userModel.email"
        label="E-mail"
        type="email"
        required
        variant="underlined"
    ></v-text-field>
    <v-text-field
        v-model="userModel.phone"
        counter="11"
        type="number"
        label="Phone number"
        required
        variant="underlined"
    ></v-text-field>
    <v-btn
        color="primary"
        class="ml-4 mt-4"
        @click="saveUser"
        elevation="1"
    >
      Сохранить информацию
    </v-btn>
  </div>
  <v-row v-else class="justify-center align-center mt-8 empty">
    <p>Не найдено информации о пользователе</p>
  </v-row>
</template>

<script setup>
import { computed, reactive, ref, onMounted } from 'vue';
import { useAppStore } from '@/store/app';
const store = useAppStore();

const password = ref('');
const user = computed(() => store.user);
const userModel = reactive(JSON.parse(JSON.stringify(user.value)));
const showPassword = ref(false);

const saveUser = async () => {
  await store.saveUserInfo({
    ...userModel,
    password: password
  });
}
</script>

<style scoped>
.empty {
  min-height: 176px;
}

.user-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.v-input {
  width: 50%;
}
</style>