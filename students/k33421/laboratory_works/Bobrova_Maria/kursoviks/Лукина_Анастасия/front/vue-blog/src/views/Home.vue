<template>
    <div class="home">
        <Tweets :tweet="tweets" @reload="loadTweets"></Tweets>
    </div>
</template>

<script>
    import Tweets from '@/components/Tweets'

    export default {
        name: 'home',
        components: {
            Exhibition
        },
        data() {
            return {
                tweets: "",
                url: 'api/v1/app/',
            }
        },
        watch: {
            '$route.name'() {
                if (this.$route.name === 'home') {
                    this.url = 'api/v1/app/'
                } else if (this.$route.name === 'my_tweets') {
                    this.url = 'api/v1/app/my/'
                } else if (this.$route.name === 'exhibition') {
                    this.url = 'api/v1/exhibition/'
                } else if (this.$route.name === 'my_follow_tweets') {
                    this.url = 'api/v1/app/favorites/'
                }
                this.loadTweets()
            }
        },
        created() {
            this.loadTweets()
        },
        methods: {
            loadTweets() {
                $.ajax({
                    url: this.$store.getters.get_url_server + this.url,
                    type: "GET",
                    success: (response) => {
                        this.tweets = response
                    }
                })
            }
        }
    }
</script>
