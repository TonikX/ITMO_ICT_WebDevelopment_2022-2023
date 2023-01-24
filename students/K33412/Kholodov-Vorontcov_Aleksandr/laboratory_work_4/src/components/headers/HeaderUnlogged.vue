<template>
  <header class="d-flex justify-content-center px-10">
    <ul class="navigation-bar">
      <li class="nav-item">
        <a class="nav-link pt-1" href="#">
          <svg class="nav-logo" height="35px">
            <use xlink:href="#logo">
            </use>
          </svg>
        </a>
      </li>
      <li class="nav-item">
        <a href="/login" class="nav-link">Вход</a>
      </li>
    </ul>
  </header>
</template>

<script>
export default {
  name: 'HeaderUnlogged'
}
</script>

<style >
.navigation-bar {
  width: 100%;
  list-style-type: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 40px 8px 10px;
  margin: 0;
  border-bottom: 1px solid;
  border-bottom-color: var(--border-bottom);
}

.nav-link {
  font-family: Tahoma, sans-serif;
  font-weight: bolder;
  color: var(--link-color);
}

.nav-link:hover {
  color: var(--link-hover);
}

.nav-logo {
  width: 12%;
}
</style>
