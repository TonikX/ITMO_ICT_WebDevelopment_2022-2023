<template>
  <v-card>
    <v-navigation-drawer
      floating
      permanent
      width="320"
    >
      <v-list
        dense
        rounded
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          @click=item.link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
           <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: 'NavDrawer',
  data () {
    return {
      items: [
        { title: 'Клиенты', icon: 'mdi-account', link: this.client },
        { title: 'Прайс-лист на услуги', icon: 'mdi-format-list-bulleted', link: this.servicePL },
        { title: 'Прайс-лист на материалы', icon: 'mdi-format-list-bulleted', link: this.materialsPL },
        { title: 'Исполнители', icon: 'mdi-account-tie', link: this.executor },
        { title: 'Заявки', icon: 'mdi-account-question', link: this.request },
        { title: 'Выбранные услуги', icon: 'mdi-cart-arrow-down', link: this.chosenServices },
        { title: 'Выбранные материалы', icon: 'mdi-cart-arrow-down', link: this.chosenMaterials },
        { title: 'Рабочие группы', icon: 'mdi-account-group', link: this.workGroup },
        { title: 'Счета на оплату', icon: 'mdi-cash', link: this.invoice },
        { title: 'Платежные поручения', icon: 'mdi-cash-check', link: this.paymentOrder }
      ]
    }
  },

  methods: {
    client () {
      this.$router.push({ name: 'client' })
    },
    servicePL () {
      this.$router.push({ name: 'servicepl' })
    },
    materialsPL () {
      this.$router.push({ name: 'materialspl' })
    },
    executor () {
      this.$router.push({ name: 'executor' })
    },
    request () {
      this.$router.push({ name: 'request' })
    },
    chosenServices () {
      this.$router.push({ name: 'chosenservices' })
    },
    chosenMaterials () {
      this.$router.push({ name: 'chosenmaterials' })
    },
    workGroup () {
      this.$router.push({ name: 'workgroup' })
    },
    invoice () {
      this.$router.push({ name: 'invoice' })
    },
    paymentOrder () {
      this.$router.push({ name: 'paymentorder' })
    }
  }
}

</script>

<style scoped>

</style>
