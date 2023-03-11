<template>
    <div id="app">
      <router-view />
    </div>
  </template>
  <style>
  :root {
    --accent-color: #efd67d;
    --button-color: #2a7aab;
    --accent-on-hover: #24398e;
    --background-color: #f5f5f5;
    --nav-link-on-hover: #000000;
    --text-color: #212529;
    --accent-text: white;
    --form-background: white;
    --form-border-color: #86b7fe;
  }
  body {
    background-color: var(--background-color);
    color: var(--text-color);
  }
  .text-black {
    color: var(--text-color) !important;
  }
  .form-control {
    background-color: var(--form-background);
    color: var(--text-color);
  }
  .form-control:focus {
    background-color: var(--form-background);
    color: var(--text-color);
  }
  .btn {
    background-color: var(--button-color);
    color: var(--accent-text);
    margin: 10px auto;
    font-size: calc(1.3rem + 0.6vw);
    border-radius: 10px;
    padding: 5px 40px;
  }
  .btn:hover {
    background-color: var(--accent-on-hover);
    color: var(--accent-text);
  }
  .link-primary {
    color: var(--link-color);
  }
  .nav-link:hover {
    border-bottom: 2px solid black;
}
  </style>
<script></script>