<template>
 <v-container>
   <v-row>
     <v-col cols="2">
       <v-card>
         <nav-drawer/>
       </v-card>
     </v-col>
     <v-col cols="10">
       <AccountDetailsCard/>
     </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NavDrawer from '@/components/NavDrawer'
import AccountDetailsCard from '@/components/AccountDetailsCard'
export default {
  name: 'AccountDetails',
  components: {
    NavDrawer,
    AccountDetailsCard
  }
}
</script>
