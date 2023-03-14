<template>
  <input type="text" class="input-group d-flex" placeholder="Поиск по названию"
         :value="modelValue" @input="updateInput" @change="sendSearch"
  >
  <span class="right-pan">
    <button class="bg-light clear" style="border: 1px solid lightgrey; width: 50px; height: 50px;"
            @click="clearInput"
    >
      <svg style="width: 30px; height: 30px;">
        <use xlink:href="#clear">
        </use>
      </svg>
    </button>
  </span>
</template>

<script>
export default {
  name: 'search-input',
  emits: ['sendSearch'],
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

<style>
.input-group {
  color: var(--text-color);
  border: 2px solid var(--border-input);
  border-radius: 5px;
  height: 50px !important;
  width: 300px !important;
  padding: 20px ;
}

.input-group:focus {
  background-color: var(--bg-color);
  border-color: var(--link-hover);
  color: var(--text-color)
}

.input-group:hover{
  transform: scale(0.99);
}

.clear {
  border-radius: 5px;
}

.clear:hover {
  transform: scale(0.98);
}
</style>