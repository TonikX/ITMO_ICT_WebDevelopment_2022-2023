<template>
    <div class="form-check">
        <input class="form-check-input" type="checkbox" :id="id" @change="SelectOption">
        <label class="form-check-label" :for="id"> {{ name }} </label>
    </div>
</template>

<script>
export default {
    name: "FilterCheckbox",
    props: {
        name: {
            type: String
        },
        id: {
            type: String
        }
    },
    methods: {
        SelectOption: function () {
            this.$emit('SelectOption', 1, this.id)
        }
    }
}
</script>

<style scoped>

</style>
