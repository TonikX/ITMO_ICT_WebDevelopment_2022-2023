<template>
  <div class="sort-arrow">
    <svg style="width: 15px; height: 15px">
      <use xlink:href="#sort">
      </use>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'sort-button',

}
</script>

<style scoped>
.sort-arrow {
  border: none;
  background-color: white;
  display: inline-block;
}
</style>