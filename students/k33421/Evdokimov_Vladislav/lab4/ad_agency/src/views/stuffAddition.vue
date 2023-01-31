<template>
  <div>
    <v-card>
       <h1 class="headline">  Добавление сущеностей</h1>
      <v-card-text>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="addClient">Создать клиента</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="createService">Создать услугу</v-btn></div><br>
            <div class="d-flex align-center flex-column flex-md-row">
              <v-btn variant="outlined" color="outline" rounded="lg" @click="createMaterial">Создать материал</v-btn></div><br>
           <div class="d-flex align-center flex-column flex-md-row">
             <v-btn variant="outlined" color="outline" rounded="lg" @click="createStaff">Создать сотрудника</v-btn></div><br>
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
    addClient () {
      this.$router.push({ name: 'addclient'})
    },
    createService () {
      this.$router.push({ name: 'createservice' })
    },
    createMaterial () {
      this.$router.push({ name: 'creatematerial' })
    },
    createStaff () {
      this.$router.push({ name: 'createstaff' })
    },
  }
}
</script>
