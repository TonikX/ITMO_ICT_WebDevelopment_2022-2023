<template>
  <div>
    <v-card>
       <h1 class="headline"> Конструктор заявки</h1>
      <v-card-text>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="createRequest">Создать саму заявку</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="linkService">Выбрать услугу</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="linkMaterial">Выбрать материалы</v-btn></div><br>
           <div class="d-flex align-center flex-column flex-md-row">
             <v-btn variant="outlined" color="outline" rounded="lg" @click="linkWorkGroup">Выбрать рабочую группу</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="createPaymentOrder">Создать счёт на оплату</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined"  color="info" rounded="lg" @click="$router.push(`/`)">На главную</v-btn></div>

      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    createRequest () {
      this.$router.push({ name: 'addrequest'})
    },
    linkService () {
      this.$router.push({ name: 'addservice' })
    },
    linkMaterial () {
      this.$router.push({ name: 'addmaterial' })
    },
    linkWorkGroup () {
      this.$router.push({ name: 'addworkgroup' })
    },
    createPaymentOrder () {
      this.$router.push({ name: 'addPaymentOrder' })
    },
  }
}
</script>
