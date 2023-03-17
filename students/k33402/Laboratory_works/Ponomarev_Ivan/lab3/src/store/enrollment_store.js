import { defineStore } from 'pinia'
import { enrollment_api } from '@/api'

const enrollmentStore = defineStore('enrollments',{
    state: () => ({
        enrollments: [],
        enrollment: {}
    }),
    
    actions: {
        async getUserEnrollments(id) {
            const response = await enrollment_api.getUserEnrollments(id)
            this.enrollments = response.data
            return response
        },

        async deleteUserEnrollment(id) {
            const response = await enrollment_api.deleteUserEnrollment(id)
            return response
        },

        async makeUserEnrollment(data) {
            const response = await enrollment_api.makeUserEnrollment(data)
            this.enrollment = response.data
            return response
        }
    }
})

export default enrollmentStore