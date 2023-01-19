<template>
  <v-app :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }" :dark="true">
    <v-container>
      <v-data-table
        :headers="headers"
        :items="riders"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Riders list</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="primary"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
                >
                  New rider
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">New rider</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="12">
                        <v-text-field
                          v-model="editedRider.name"
                          label="Name"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="12">
                        <v-text-field
                          v-model="editedRider.description"
                          label="Description"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="12">
                        <v-text-field
                          v-model="editedRider.car_description"
                          label="Car description"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="12">
                        <v-select
                          v-model="editedRider.team_id"
                          :items="teamsOptions"
                          item-text="name"
                          item-value="id"
                          label="Team"
                        ></v-select>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDialog">
                    Cancel
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="saveNewRider"
                    :disabled="
                      editedRider.name.length < 3 ||
                      editedRider.description.length < 3 ||
                      editedRider.team_id === null
                    "
                  >
                    Save
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
      </v-data-table>
    </v-container>
  </v-app>
</template>

<script>
import axiosInstance from "@/utils/axios";
import { getCreatorName } from "@/utils";

export default {
  name: "RidersList",
  components: {},
  data() {
    return {
      teamsOptions: [],
      riders: [],
      headers: [
        { text: "#", value: "id" },
        { text: "Name", value: "name" },
        { text: "description", value: "description" },
        { text: "car_description", value: "car_description" },
        { text: "Team", value: "team_name" },
        { text: "Creator", value: "creator_name" },
        { text: "created at", value: "created_at" },
      ],
      dialog: false,
      defaultRider: {
        name: "",
        description: "",
        car_description: "",
        team_id: 1,
      },
      editedRider: {
        name: "",
        description: "",
        car_description: "",
        team_id: 1,
      },
    };
  },
  watch: {
    dialog(val) {
      val || this.closeDialog();
    },
  },
  methods: {
    closeDialog() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedRider = Object.assign({}, this.defaultRider);
      });
    },
    saveNewRider() {
      axiosInstance
        .post(`/api/riders`, this.editedRider)
        .then((response) => {
          if (response) {
            this.loadRiders();
            this.closeDialog();
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(
            `Error creating the rider, try again - ${
              err?.response?.data ? JSON.stringify(err.response.data) : err
            }`
          );
        });
    },
    loadRiders() {
      axiosInstance
        .get(`/api/riders`)
        .then((response) => {
          if (response.status === 200) {
            this.riders = response.data.map((item) => ({
              ...item,
              creator_name: getCreatorName(item.creator),
              team_name: item.team.name,
            }));
          } else throw new Error("Error");
        })
        .catch((err) => {
          alert(`Error loading the riders, try again - ${err}`);
        });
    },
  },
  mounted() {
    this.loadRiders();
    axiosInstance
      .get(`/api/teams`)
      .then((response) => {
        if (response.status === 200) {
          this.teamsOptions = response.data;
        } else throw new Error("Error");
      })
      .catch((err) => {
        alert(`Error loading the teams, try again - ${err}`);
      });
  },
};
</script>

<style scoped></style>
