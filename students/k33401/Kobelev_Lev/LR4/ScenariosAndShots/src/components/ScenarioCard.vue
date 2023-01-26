<template>
    <div class="card shadow-sm rounded d-flex flex-column h-100">
        <router-link :to="{name:'scenario', params:{ id: id }}" class="card-body row flex-grow-1 p-0">
            <div class="col-lg-4 d-none d-sm-none d-md-none d-lg-block">
                <img :src="image" class="card-img-top img-fluid text-center" alt="Scenario Image">
            </div>
            <div class="col-md-12 col-lg-8">
                <div class="d-block d-md-block d-lg-none">
                    <img :src="image" class="card-img-top-horizontal img-fluid text-center" alt="Scenario Image">
                </div>
                <h5 class="card-title mx-2 mt-2 mb-1"> {{ name }} </h5>
                <div class="d-flex flex-row flex-wrap my-1">
                    <TagCapsule v-for="tag in tags" :key="tag.id" :name="tag.name"/>
                </div>
                <p class="mx-2 my-1 lh-base">
                    <small> {{ description }} </small>
                </p>
            </div>
        </router-link>
        <div class="card-footer px-2 py-1 d-flex justify-content-between align-items-center">
            <LikeButton v-on:SetLike="SetLike" :likes="likes" :liked="liked" :username="username"/>
            <div class="author">
                <small class="fw-light"> {{ author }} </small>
            </div>
        </div>
    </div>
</template>

<script>
import LikeButton from "./LikeButton.vue";
import TagCapsule from "./TagCapsule.vue";

export default {
    name: "ScenarioCard",
    components: {LikeButton, TagCapsule},
    props: {
        name: {
            type: String
        },
        author: {
            type: String
        },
        description: {
            type: String
        },
        image: {
            type: String
        },
        likes: {
            type: Number
        },
        tags: {
            type: Array
        },
        id: {
            type: Number
        },
        username: {
            type: String
        },
        liked: {
            type: Boolean
        }
    },
    methods: {
        SetLike: function () {
            this.$emit('SetLike', this.id)
        },
    }
}
</script>

<style scoped>
.card-img-top {
    height: 100%;
    object-fit: cover;
}

.card-img-top-horizontal {
    width: 100%;
    height: 100%;
    max-height: 200px;
    object-fit: cover;
}

.card {
    min-height: 350px;
}

.card-footer {
    background-color: var(--bs-light);
}

a {
    text-decoration: none;
    color: inherit;
}
</style>
