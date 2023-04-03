<template>
    <div>
        <v-card v-if="edit" class="elevation-4">
            <v-toolbar color="teal" dark>
                <v-toolbar-title>Edit Form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
                <v-form>
                    <v-text-field required v-model="name" name="Name" label="Name" type="text"></v-text-field>
                    <v-text-field required v-model="surname" name="Surname" label="Surname" type="text"></v-text-field>
                    <v-text-field required v-model="middlename" name="Middle name" label="Middle name" type="text"></v-text-field>
                    <v-text-field required v-model="passport_number" name="Passport" label="Passport" type="text"></v-text-field>
                    <v-text-field required v-model="from_location" name="Country" label="Country" type="text"></v-text-field>
                    <v-text-field required v-model="check_in_date" name="Check-in date" label="Check-in date" type="text"></v-text-field>
                    <v-text-field required v-model="check_out_date" name="Check-out date" label="Check-out date" type="text"></v-text-field>
                    <v-text-field required v-model="room" name="Room number" label="Room number" type="text"></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-btn color="teal" dark @click="edit=false">Close</v-btn>
                <v-btn color="teal" dark @click="editGuest">Submit Edit</v-btn>
            </v-card-actions>
        </v-card>

        <v-card v-if="del" class="elevation-4">
            <v-card-title>Are you sure?</v-card-title>
            <v-card-actions>
                <v-btn color="teal" dark @click="del=false">Close</v-btn>
                <v-btn color="teal" dark @click="deleteGuest">Delete</v-btn>
            </v-card-actions>
        </v-card>

        <v-card v-if="exist" elevation="6" shaped>
            <v-card-title>{{ guest.name }} {{guest.middlename}} {{guest.surname}}</v-card-title>
            <v-card-subtitle>Passport number: {{ guest.passport_number }}</v-card-subtitle>
            <v-card-text>Dates: {{ guest.check_in_date }} - {{ guest.check_out_date }} Room: {{ guest.room }}</v-card-text>
            <v-card-actions>

                <v-btn @click="edit = true">Edit</v-btn>
                <v-btn @click="del = true">Delete</v-btn>
            </v-card-actions>
        </v-card>
    </div>
</template>

<script>
export default {
  name: 'Guest',
  props: {
    guest: Object
  },
  data: () => ({
    exist: true,
    edit: false,
    del: false,
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
    editGuest () {
      const body = {
        passport_number: this.passport_number,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        from_location: this.from_location,
        check_in_date: this.check_in_date,
        check_out_date: this.check_in_date,
        room: this.room
      }

      this.axios
        .patch(this.$hostname + 'hotel/guests/' + this.guest.id + '/', body, {
          headers: {
            Authorization: 'Token ' + localStorage.getItem('auth_token')
          }
        })
        .then(response => {
          console.log(response)
          const updatedGuest = {
            passport_number: this.passport_number,
            name: this.name,
            surname: this.surname,
            middlename: this.middlename,
            from_location: this.from_location,
            check_in_date: this.check_in_date,
            check_out_date: this.check_out_date,
            room: this.room
          }
          this.$emit('update:guest', updatedGuest)
          this.edit = false
        })
        .catch(error => console.log(error))
    },

    deleteGuest () {
      this.axios
        .delete(this.$hostname + 'hotel/guests/' + this.guest.id + '/', {
          headers: { Authorization: 'Token ' + localStorage.getItem('auth_token') }
        })
        .then(response => {
          console.log(response)
          this.exist = false
          this.del = false
        })
        .catch(error => console.log(error))
    }
  }
}
</script>
