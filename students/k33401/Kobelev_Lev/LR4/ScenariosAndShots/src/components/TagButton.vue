<template>
    <button type="button" class="btn btn-sm rounded-pill py-0 px-3" :class="{ active: selected, 'btn-secondary': selected, 'btn-light': !selected }" @click="SelectTag"> {{ name }} </button>
</template>

<script>
export default {
    name: "TagButton",
    data() {
        return {
            selected: false
        }
    },
    props: {
        name: {
            type: String
        },
        id: {
            type: Number
        }
    },
    methods: {
        SelectTag: function () {
            this.selected = !this.selected
            this.$emit('SelectTag', this.id, 'tag')
        }
    }
}
</script>

<style scoped>

</style>
