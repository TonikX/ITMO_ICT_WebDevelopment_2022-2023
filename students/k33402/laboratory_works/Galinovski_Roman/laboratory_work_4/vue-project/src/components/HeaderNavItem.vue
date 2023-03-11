<template>
    <b-nav-item class="px-3" :to="navLink">
      {{ navText }}
    </b-nav-item>
  </template>
  
  <script>
  export default {
    name: "HeaderNavItem",
    props: {
      navLink: String,
      navText: String
    }
  }
  </script>
  <style>
  .nav-link {
    color: var(--text-color) !important;
  }
  </style>