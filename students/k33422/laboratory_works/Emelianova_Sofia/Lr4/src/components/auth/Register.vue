<template>
    <v-sheet
        elevation="1"
        rounded="xl"
        class="pa-8"
    >
        <h1>Регистрация</h1>
        <v-form class="auth-form" ref="form">
            <v-text-field
                v-model="username"
                :counter="15"
                :rules="[v => !!v || 'Не заполнено']"
                label="Имя пользователя"
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
            ></v-text-field>
            <v-row>
                <v-col
                    cols="12"
                    md="4"
                >

                    <v-text-field
                        v-model="name"
                        :counter="20"
                        label="Name"
                        :rules="[v => !!v || 'Не заполнено']"
                        required
                        variant="underlined"
                    ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                    md="4"
                >

                    <v-text-field
                        v-model="phone"
                        type="number"
                        label="Номер телефона"
                        :counter="11"
                        :rules="phoneRules"
                        required
                        variant="underlined"
                    ></v-text-field>
                </v-col>
                <v-col
                    cols="12"
                    md="4"
                >
                    <v-text-field
                        v-model="libraryNumber"
                        type="number"
                        label="Номер читательского билета"
                        readonly
                        required
                        variant="underlined"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row style="margin-top: 0;">
                <v-col
                    cols="12"
                    md="4"
                >
                    <v-select
                        label="Образование"
                        :items="['Нет образования','Среднее', 'Высшее']"
                        v-model="education"
                        variant="underlined"
                    ></v-select>
                </v-col>
                <v-col
                    cols="12"
                    md="4"
                >
                    <v-select
                        label="Читательный зал"
                        :items="[1, 2, 3]"
                        :rules="[v => !!v || 'Не выбрано']"
                        v-model="readerRoom"
                        variant="underlined"
                    ></v-select>
                </v-col>
                <v-col
                    cols="12"
                    md="4"
                >
                    <v-checkbox
                        v-model="degree"
                        label="У меня есть степень"
                    />
                </v-col>
            </v-row>

            <v-btn
                color="success"
                class="mr-4 mt-8"
                @click="register"
                elevation="1"
            >
                Зарегистрироваться
            </v-btn>
            <v-btn
                color="primary"
                class="ml-4 mt-8"
                @click="switchMode"
                elevation="1"
            >
                Я уже зарегистрирован
            </v-btn>
        </v-form>
    </v-sheet>
  
</template>

<script setup>
    import router from '@/router';
    import { ref, reactive } from 'vue';
    import { useAppStore } from '@/store/app';
    const emit = defineEmits(['switchMode']);
    const store = useAppStore();

    const form = ref();
    const name = ref('');
    const phone = ref('');
    const username = ref('');
    const password = ref('');
    const education = ref('Нет образования');
    const degree = ref(false);
    const readerRoom = ref(null);
    const libraryNumber = ref(Math.floor(100000000 + Math.random() * 900000000));
    const showPassword = ref(true);

    const phoneRules = [
        v => !!v || 'Не заполнен номер телефона',
        v => (v && v.length <= 11 && v.length >= 11) || 'Длина номера должна быть 11 символов',
    ];

    const educations = {
        'Высшее': 2,
        'Среднее': 1
    }

    const register = async () => {
        const { valid } = await form.value.validate()
        if (!valid) {
            store.addNotification('error', 'Не все поля заполены правильно');
            return;
        }

        await store.userRegister({
            name: name.value,
            phone: phone.value,
            username: username.value,
            password: password.value,
            education: educations[education.value] || null,
            is_have_degree: degree.value,
            reader_room: readerRoom.value,
            library_card_number: libraryNumber.value
        })
        //router.push('/')
    }

    const switchMode = () => {
        emit('switchMode');
    }
</script>

<style>
</style>