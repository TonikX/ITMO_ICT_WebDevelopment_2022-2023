<template>
    <button type="button" data-bs-toggle="button" class="btn btn-sm btn-outline-danger shadow-sm rounded" :class="{'active':liked}" v-on:click="SetLike" :disabled="clickable == 0">
        {{ fakeLikes }}
    </button>
</template>

<script>
export default {
    name: "LikeButton",

    props: {
        likes: {
            type: Number
        },
        username: {
            type: String
        },
        liked: {
            type: Boolean
        }
    },

    data() {
        return {
            fakeLikes: this.likes
        }
    },

    methods: {
        SetLike: function () {
            this.$emit('SetLike')
        }
    },

    computed: {
        clickable: function () {
            if (this.username) {
                return true
            }
            return false
        }
    }
}
</script>

<style scoped>

</style>
