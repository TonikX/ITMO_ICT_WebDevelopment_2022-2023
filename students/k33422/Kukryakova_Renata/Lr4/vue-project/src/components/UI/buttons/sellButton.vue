<template>
  <button type="button"
          class="btn btn-danger btn-link rounded-pill h-25 text-white bg-danger text-decoration-none">
    Продать
  </button>
</template>

<script>
export default {
  name: 'sell-button'
}
</script>

<style >
.btn-danger {
  width: 100px;
  background-color: var(--btn-color);
}

.btn-danger:hover {
  background-color: red;
  border-color: red;
  box-shadow: 0 0 10px red;
}
</style>