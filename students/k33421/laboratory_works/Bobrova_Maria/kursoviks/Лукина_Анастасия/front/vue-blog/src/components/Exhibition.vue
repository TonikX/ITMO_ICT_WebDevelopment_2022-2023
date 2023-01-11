<template>
    <div class="main-tweet">
        <div class="row form-twit">
            <form action="" method="post">
                <button @click="sendExhibition" type="button" class="btn btn-tweet">
                    Отправить<button type="submit" class="btn btn-tweet waves-effect waves-light">
                        Отправить
                    </button>
                </button>
            </form>
        </div>
    </div>
</template>

<script>
    import auth from '@/mixins/computedAuth.js'
    import {mapGetters} from 'vuex'

    export default {
        name: "Exhibition",
        props: {
            exhibition: ''
        },
        mixins: [
            auth
        ],
        data() {
            return {
                exhibition: '',
                comment: '',
                showComments: false,
            }
        },
        computed: {
            ...mapGetters([
                'get_user_info'
            ])
        },
        methods: {
            like(id) {
                $.ajax({
                    url: this.$store.getters.get_url_server + "api/v1/app/like/",
                    type: "POST",
                    data: {
                        pk: id,
                    },
                    success: (response) => {
                        this.$emit("reload")
                    },
                    error: (response) => {
                        console.log("False")
                    }
                })
            },
            follow(id) {
                $.ajax({
                    url: this.$store.getters.get_url_server + "api/v1/profile/follow/",
                    type: "POST",
                    data: {
                        pk: id,
                    },
                    success: (response) => {
                        this.$emit("reload")
                    },
                    error: (response) => {
                        console.log("False")
                    }
                })
            },
            sendExhibition() {
                $.ajax({
                    url: this.$store.getters.get_url_server + "api/v1/exhibition/",
                    type: "POST",
                    data: {
                        text: this.exhibition,
                    },
                    success: (response) => {
                        this.$emit("reload")
                    },
                    error: (response) => {
                        console.log("False")
                    }
                })
            },
            sendComment(id) {
                $.ajax({
                    url: this.$store.getters.get_url_server + "api/v1/app/my/",
                    type: "POST",
                    data: {
                        id: id,
                        text: this.comment,
                    },
                    success: (response) => {
                        this.$emit("reload")
                    },
                    error: (response) => {
                        console.log("False")
                    }
                })
            },
            openForm(id) {
                this.showComments = id
            },
            closeForm() {
                this.showComments = false
            }
        },
        filters: {
            // Фильтр полной даты числами
            filterDateTime(item) {
                let old_date = new Date(item)
                return `
                 ${old_date.getDate()}.${old_date.getMonth()}.${old_date.getFullYear()} - ${old_date.getHours()}:${old_date.getMinutes()}`
            },
        }
    }
</script>

<style scoped>
    .main-tweet {
        margin: 0 auto;
        max-width: 700px;
        box-shadow: 0px 2px 20px 1px #cddae2
    }

    .tweet {
        padding: 10px;
        background: #fff;
        border-left: 1px solid #e6ecf0;
        border-right: 1px solid #e6ecf0;
        border-bottom: 1px solid #e6ecf0;
        margin-right: 0;
        margin-left: 0;
    }

    .tweet:hover {
        background: #f5f8fa;
        cursor: pointer;
    }

    .form-twit {
        width: 100%;
        height: auto;
        padding: 15px;
        margin: 15px auto;
        background: #fff;
        /* box-shadow: 1px 1px 16px 1px #cecece; */
    }

    .btn-tweet {
        border-radius: 100px;
        box-shadow: none;
        cursor: pointer;
        font-size: 14px;
        font-weight: bold;
        line-height: 20px;
        padding: 6px 16px;
        position: relative;
        text-align: center;
        white-space: nowrap;
        background: #46D89E;
    }

    .btn-follow {
        padding: 6px 16px;
        border-radius: 100px;
        background: #00acd8;
    }
</style>