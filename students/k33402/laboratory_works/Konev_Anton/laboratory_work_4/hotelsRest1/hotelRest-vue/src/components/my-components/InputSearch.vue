<template>
  <div class="d-flex align-items-center">
    <font-awesome-icon icon="fa-solid fa-magnifying-glass"/>
    <input :value="modelValue"
           @input="updateInput"
           @change="sendSearch"
           class="form-control w-100 border-0 "
           type="text"
           placeholder="Поиск">
    <button class="btn btn-close" @click="clearInput"></button>
  </div>
</template>

<script>
export default {
  name: 'custom-input',
  props: {
    modelValue: String,
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value)
    },
    clearInput() {
      this.$emit('update:modelValue', '')
      this.sendSearch()
    },
    sendSearch(event) {
      if (event) {
        this.$emit('sendSearch', event.target.value)
      } else {
        this.$emit('sendSearch', '')
      }
    }
  }
}
</script>

<style scoped>
.form-control {
  border: none;
}

.form-control:focus {
  border: none;
  box-shadow: none;
}
</style>