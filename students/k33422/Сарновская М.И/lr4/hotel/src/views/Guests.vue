<template>
  <v-main>
    <v-container fluid fill-height>
      <v-layout justify-center>
        <v-flex xs12 sm8 md4>
        <template>
          <v-row justify="center">
            <v-dialog v-model="dialog" persistent max-width="600px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="teal" dark v-bind="attrs" v-on="on">
                  Add Guest
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">Add Guest</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="6">
                        <v-text-field v-model="passport_number" label="Passport" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="name" label="Name" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="surname" label="Surname" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="middlename" label="Middle name" required></v-text-field>
                      </v-col>
                       <v-col cols="6">
                        <v-text-field v-model="from_location" label="Country" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="check_in_date" label="Check-in date" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="check_out_date" label="Check-out date" required></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field v-model="room" label="Room" required></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="green darken-1" text @click="dialog = false">
                    Close
                  </v-btn>
                  <v-btn color="green darken-1" text @click="addGuest">
                    Add Guest
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
        </template>
        <guest v-for="guest in guests" v-bind:key="guest.id" v-bind:guest="guest" style="margin-top: 25px"></guest>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import Guest from '@/components/Guest.vue'

export default {
  name: 'Guests',

  components: {
    Guest
  },

  data: () => ({
    guests: [],
    filter: false,
    dialog: false,
    passport_number: null,
    name: null,
    surname: null,
    middlename: null,
    from_location: null,
    check_in_date: null,
    check_out_date: null,
    room: null
  }),
  methods: {
    addGuest () {
      const body = {
        passport_number: this.passport_number,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        from_location: this.from_location,
        check_in_date: this.check_in_date,
        check_out_date: this.check_out_date,
        room: this.room
      }

      this.axios
        .post(this.$hostname + 'hotel/guests/', body, {
          headers: {
            Authorization: 'Token ' + localStorage.getItem('auth_token')
          }
        })
        .then(response => {
          if (response.status === 201) {
            this.guests.push(body)
          }
        })
        .catch(error => console.log(error))

      this.dialog = false
    }
  },
  created () {
    this.axios
      .get(this.$hostname + 'hotel/guests/', {
        headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') }
      })
      .then(response => {
        this.guests = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
