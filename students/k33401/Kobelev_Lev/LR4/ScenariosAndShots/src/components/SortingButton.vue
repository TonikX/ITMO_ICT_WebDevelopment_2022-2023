<template>
    <div class="container-fluid m-0 mb-1 p-0">
        <input type="radio" class="btn-check w-100" :id="id" autocomplete="off" name="sortingOption" @change="SelectSorting"/>
        <label class="btn btn-outline-primary w-100" :for="id"> {{ name }} </label>
    </div>
</template>

<script>
export default {
    name: "SortingButton",
    props: {
        name: {
            type: String
        },
        id: {
            type: String
        }
    },
    methods: {
        SelectSorting: function () {
            this.$emit('SelectSorting', this.id)
        }
    }
}
</script>

<style scoped>

</style>
