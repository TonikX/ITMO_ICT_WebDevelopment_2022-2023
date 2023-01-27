<template>
  <div>
    <v-card v-if="edit" class="elevation-4">
      <v-toolbar color="teal" dark>
        <v-toolbar-title>Edit Form</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form>
          <v-text-field required v-model="roomPrice" name="Price" label="Price" type="text"></v-text-field>
          <v-text-field required v-model="roomType" name="Type" label="Type" type="text"></v-text-field>
          <v-text-field required v-model="roomFloor" name="Floor" label="Floor" type="text"></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn color="teal" dark @click="edit=false">Close</v-btn>
        <v-btn color="teal" dark @click="editRoom">Submit Edit</v-btn>
      </v-card-actions>
    </v-card>

    <v-card v-if="del" class="elevation-4">
      <v-card-title>Are you sure?</v-card-title>
      <v-card-actions>
        <v-btn color="teal" dark @click="del=false">Close</v-btn>
        <v-btn color="teal" dark @click="deleteRoom">Delete</v-btn>
      </v-card-actions>
    </v-card>

    <v-card v-if="exist" elevation="6" shaped>
      <v-card-title>{{ room.number }} Room</v-card-title>
      <v-card-subtitle>Amount of beds - {{ room.type }}</v-card-subtitle>
      <v-card-text>Price:{{ room.price }} Floor:{{ room.floor }}</v-card-text>
      <v-card-actions>
        <v-btn @click="edit = true">Edit</v-btn>
        <v-btn @click="del = true">Delete</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "RoomCard",
  props: {
    room: Object,
  },
  data: () => ({
    exist: true,
    edit: false,
    del: false,
    roomType: null,
    roomPrice: null,
    roomFloor: null,
  }),

  methods: {
    editRoom() {
      const body = {
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor,
      };

      this.axios
        .patch(this.$hostname + "hotel/rooms/" + this.room.number + "/", body, {
          headers: {
            Authorization: "Token " + localStorage.getItem("auth_token"),
          },
        })
        .then(response => {
          console.log(response);
          this.room.price = this.roomPrice;
          this.room.type = this.roomType;
          this.room.floor = this.roomFloor;
          this.edit = false;
        })
        .catch(error => console.log(error));

    },

    deleteRoom() {
      this.axios
        .delete(this.$hostname + "hotel/rooms/" + this.room.number + "/", {
          headers: { Authorization: "Token " + localStorage.getItem("auth_token") },
        })
        .then(response => {
          console.log(response);
          this.exist = false;
          this.del = false;
        })
        .catch(error => console.log(error));
    },
  },
};
</script>
