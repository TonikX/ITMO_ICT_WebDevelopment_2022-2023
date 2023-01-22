<template>
  <button type="button"
          class="btn btn-primary btn-link rounded-pill h-25 text-white bg-primary text-decoration-none">
    Купить
  </button>
</template>

<script>
export default {
  name: 'buy-button'
}
</script>

<style scoped>
.btn-primary {
  width: 100px;
  background-color: var(--btn-color);
}

.btn-primary:hover {
  background-color: var(--btn-hover);
  border-color: var(--link-hover);
  box-shadow: 0 0 10px var(--btn-hover);
}
</style>