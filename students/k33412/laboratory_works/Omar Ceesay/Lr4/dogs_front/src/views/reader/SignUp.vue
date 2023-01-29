<template>
  <article>
    <div class="container" :class="signup">
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-right wrapper">
            <div class="wrapperInner">
              <h2>Welcome!</h2>
              <p>Register to get started.</p>
              <form @submit.prevent="signUp"
                    ref="signUpForm"
                    class="my-2 signUp__wrapper">
                <v-text-field
                    type="text"
                    label="login"
                    v-model="login"
                    name="login"
                ></v-text-field>
                <v-text-field
                    label="password"
                    v-model="password"
                    name="password"
                    type="password"
                ></v-text-field>
                <!--                <input type="text"
                       label="login" placeholder="login" class='input' v-model="login" name="login">-->
                <!--                <input
                                    label="password" placeholder="password" class='input' v-model="password" name="password"
                                    type="password">-->
                <v-btn depressed elevation="2" type="submit">Register</v-btn>
              </form>
            </div>
          </div>
          <div class="overlay-left">
            <p class="mt-15">If you have already registered, please login with your personal info
              <router-link to="/show/signin" class="btn">Log in</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
// Create Vue instance we create the necessary routes and views to render the signup form in the browser.
//Create methods for handling user input and for submitting the form data to the API.
/* eslint-disable */
import $ from "jquery";

export default {
  name: 'SignUp',
  data() {
    // Define form steps. Form inputs
    return {
      login: '',
      password: '',
      telephone: '',
    }
  }, //create the API endpoint for the signup form using Django Rest Framework. This endpoint should accept the form data, validate it, and save it to the database.
  methods: {

    goProfile() {
      this.$router.push({name: 'profile'})
    },

    goLogOut() {
      this.$router.push({name: 'logout'})
    },

    goSignIn() {
      this.$router.push({name: 'signin'})
    },


    async signUp() {
      console.log("1")

      $.ajax({
        type: "POST",
        data: {
          username: this.login,
          password: this.password,
          telephone: this.telephone
        },
        url: "http://127.0.0.1:8000/auth/users/"  //API endpoint URL as the target for the form submission.
      }).done(() => {
        console.log(this.data)
        // alert("Thanks for your registration")
        this.$router.push({name: 'signin'})
        // console.log($router)
        // console.log(this.$router)

      });
    }
  }
}
</script>

<style>
.signUp__wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;

}

.wrapperInner {
  background: #fff;
  display: flex;
  align-items: center;
  flex-direction: column;
  row-gap: 12px;
  border-radius: 12px;
  padding: 12px;
}

h2 {
  font-size: 24px;
}

.wrapper {
  padding: 24px;
  background: rgb(211, 252, 255);
  border-radius: 12px;
}

.input {
  padding: 12px;
  border: 1px solid rgb(235, 235, 235);
  border-radius: 16px;
}

.btn {
  background-color: rgb(211, 252, 255);
  border: none;
  color: rgb(0, 0, 0);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
