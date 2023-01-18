<template>
    <div class="form-check">
        <input class="form-check-input" type="checkbox" :id="id" @change="SelectGameSystem">
        <label class="form-check-label" :for="id"> {{ name }}</label>
    </div>
</template>

<script>
export default {

    name: "GameSystemButton",

    props: {
        name: {
            type: String
        },
        id: {
            type: Number
        }
    },

    methods: {
        SelectGameSystem: function () {
            this.$emit('SelectGameSystem', this.id, 'game_system')
        }
    }
}
</script>

<style scoped>

</style>
