<template>
<div class="container py-5 ">
    <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col col-lg-9 col-xl-12">
            <div class="profile d-flex">
                <div class="rounded-top text-white">
                    <div class="ms-4 mt-2" style="width: 150px;" id="userProfileImage">
                        <img :src="user.user_image"
                            alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
                            style="width: 150px; z-index: 1">
                    </div>
                </div>
                <div class="ms-5 mt-5" id="userShortInfo">
                    <h5>{{user.first_name}} {{user.last_name}}</h5>
                    <p>{{user.email}}</p>
                    <p>+{{ user.phone }}</p>
                </div>
            </div>
            <div class="mt-5">
                <p class="lead fw-semibold mb-0 text-center">Мои мероприятия</p>
            </div>
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="myenrollments col-xl-10 mt-4" id="enrollmentsContainer">
                    <Enrollment v-for="(enrollment) in enrollments"
                                        :id="enrollment.id"
                                        :name="enrollment.event.name"
                                        :date="enrollment.event.date"
                                        :intro="enrollment.event.intro"
                                        :category_name="enrollment.event.category.name"/>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    import { mapActions, mapState } from 'pinia'
    import userStore from '@/store/user_store'
    import Enrollment from '@/components/Enrollment.vue'
    import enrollmentStore from '@/store/enrollment_store'


    export default {
        name: "ProfileAbout",
        components: {Enrollment},

        computed: {
            ...mapState(userStore, ['user']),
            ...mapState(enrollmentStore,['enrollments']),
            getUser() {
                return this.user
            },
            getEnrollments() {
                return this.enrollments
            }
        },

        methods: {
            ...mapActions(enrollmentStore,['getUserEnrollments']),
            ...mapActions(userStore, ['get_user_info'])
        },
        mounted() {
            this.enrollments = []
            this.enrollment = {}
            this.get_user_info(localStorage.user)
            this.getUserEnrollments(localStorage.user)
        }
    }
</script>