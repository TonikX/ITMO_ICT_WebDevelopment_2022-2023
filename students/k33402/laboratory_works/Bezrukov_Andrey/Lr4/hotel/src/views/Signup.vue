<template>
  <v-main class="d-flex align-center text-center">
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4 fill-height>
          <v-card class="elevation-12">
            <v-toolbar color="teal" dark>
              <v-toolbar-title>Signup form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field v-model="email" required name="email" label="Email" type="text"></v-text-field>
                <v-text-field v-model="username" required name="login" label="Login" type="text"></v-text-field>
                <v-text-field v-model="password" required id="password" name="password" label="Password" type="password"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="teal" dark @click="signup">Signup</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: "Signup",

  data: () => ({
    email: null,
    username: null,
    password: null,
  }),

  methods: {
    signup() {
      const body = {
        username: this.username,
        password: this.password,
        email: this.email,
      };

      this.axios
        .post(this.$hostname + "auth/users/", body)
        .then(response => {
          if (response.status === 201) {
            this.$router.push({ name: "Login" });
          } else {
            alert("Something went wrong");
          }
        })
        .catch(error => console.log(error));
    },
  },
};
</script>

