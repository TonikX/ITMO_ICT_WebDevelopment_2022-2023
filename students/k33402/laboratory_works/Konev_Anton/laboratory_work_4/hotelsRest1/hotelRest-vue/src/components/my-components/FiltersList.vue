<template>
    <select :value="modelValue" @change="changeOption">
      <option disabled value="">Фильтры</option>
      <option v-for="option in options" :value="option.value">
        {{ option.name }}
      </option>
    </select>
</template>

<script>
export default {
  name: 'filters-list',
  props: {
    modelValue: {
      type: String,
    },
    options: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    changeOption(event) {
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style scoped>

</style>