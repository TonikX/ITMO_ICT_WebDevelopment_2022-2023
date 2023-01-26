<template>
    <button type="button" class="btn btn-light" @click="ChangeOrder"> {{ text }} </button>
</template>

<script>


export default {
    name: "OrderButton",

    data() {
        return {
            ascending: true
        }
    },

    computed: {
        text() {
            if (this.ascending) {
                return 'Ascending'
            }
            return 'Descending'
        }
    },

    methods: {
        ChangeOrder: function () {
            this.ascending = !this.ascending
            this.$emit('ChangeOrder', this.ascending)
        }
    }
}
</script>

<style scoped>

</style>
