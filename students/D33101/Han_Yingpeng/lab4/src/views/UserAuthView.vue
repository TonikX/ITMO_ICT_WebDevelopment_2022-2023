<template>
  <v-app
    :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }"
    :dark="true"
    id="inspire"
  >
    <v-container>
      <v-layout wrap>
        <v-flex sm12 md6 offset-md3>
          <v-card elevation="4" light tag="section">
            <v-card-title>
              <v-layout align-center>
                <h3 class="headline">Races Scores</h3>
              </v-layout>
            </v-card-title>
            <v-divider></v-divider>
            <v-tabs fixed-tabs v-model="tabs">
              <v-tab :key="1" href="#tab-login">Log in</v-tab>
              <v-tab :key="2" href="#tab-register">Register</v-tab>
            </v-tabs>
            <v-tabs-items v-model="tabs">
              <v-tab-item :key="1" :value="'tab-login'">
                <v-card-text>
                  <p>Log in with your username and password:</p>
                  <v-form ref="loginRef">
                    <v-text-field
                      outline
                      label="Username"
                      type="text"
                      v-model="username"
                    />
                    <v-text-field
                      outline
                      hide-details
                      label="Password"
                      type="password"
                      v-model="password"
                    />
                  </v-form>
                </v-card-text>
                <v-divider />
                <v-card-actions
                  :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }"
                >
                  <v-spacer />
                  <v-btn
                    color="info"
                    :large="$vuetify.breakpoint.smAndUp"
                    @click="signIn"
                  >
                    Login
                  </v-btn>
                </v-card-actions>
              </v-tab-item>
              <v-tab-item :key="2" :value="'tab-register'">
                <v-card-text>
                  <v-form ref="registerRef">
                    <v-text-field
                      outline
                      label="Email"
                      type="email"
                      v-model="email"
                    />
                    <v-text-field
                      outline
                      label="Username"
                      type="text"
                      v-model="username"
                    />
                    <v-text-field
                      outline
                      hide-details
                      label="Password"
                      type="password"
                      v-model="password"
                    />
                  </v-form>
                </v-card-text>
                <v-divider />
                <v-card-actions
                  :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }"
                >
                  <v-spacer />
                  <v-btn
                    color="info"
                    :large="$vuetify.breakpoint.smAndUp"
                    @click="signUp"
                  >
                    Register
                  </v-btn>
                </v-card-actions>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import axiosInstance from "@/utils/axios";

export default {
  data() {
    return {
      tabs: null,
      email: "",
      username: "",
      password: "",
    };
  },
  methods: {
    signUp() {
      const formData = {
        email: this.email,
        username: this.username,
        password: this.password,
      };
      axiosInstance
        .post("/auth/users/", formData)
        .then((data) => {
          console.log("--SignInData--", data);
          alert(
            "Your account has been created. You will be signed in automatically"
          );
          this.signIn();
        })
        .catch((err) => {
          if (err?.response?.data) alert(JSON.stringify(err.response.data));
        });
    },
    signIn() {
      const credentials = { username: this.username, password: this.password };
      axiosInstance
        .post("/auth/token/login/", credentials)
        .then((response) => {
          sessionStorage.setItem("authToken", response.data.auth_token);
          sessionStorage.setItem("username", this.username);
          window.location.href = "/races";
        })
        .catch((err) => {
          if (err?.response?.data) alert(JSON.stringify(err.response.data));
        });
    },
  },
};
</script>

<style scoped>
#auth-container {
  margin-top: 50px;
}
</style>
