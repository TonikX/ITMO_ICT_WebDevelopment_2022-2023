export default {
    computed: {
        auth() {
            if (this.$store.getters.get_auth) return true
            else return false
        }
    },
}