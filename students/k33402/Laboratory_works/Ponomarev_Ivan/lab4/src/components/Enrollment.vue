<template>
    <div class="card mb-5" style="border-radius: 15px;">
        <div class="card-body p-4">
            <h3 class="mb-3">{{name}}</h3>
            <p class="small mb-0"><i class="far fa-star fa-lg"></i>{{date}}</p>
            <p class="about mt-4">{{intro}}</p>
            <hr class="my-4">
            <div class="d-flex justify-content-between align-items-center">
                <p class="mb-0 text-uppercase"><i class="fas fa-cog me-2"></i> <span
                class="text-muted small">{{category_name}}</span></p>
                <div class="buttons">
                    <button @click="deleteEnrollEvent()" class="btn btn-dark" >Отписаться</button>
        
                </div>
            </div>
         </div>
    </div>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import enrollmentStore from '@/store/enrollment_store';

export default {
    name: "Enrollment",

    props: {
        event_id: {type:Number,required:true},
        id: {type:Number,required:true},
        name: {type:String, required:true},
        date: {type:String, required:true},
        intro: {type: String, required:true},
        category_name: {type:String, required:true}
    },

    methods: {
        ...mapActions(enrollmentStore,['deleteUserEnrollment']),
        
        async deleteEnrollEvent(){
            const response = await this.deleteUserEnrollment(this.id)
            alert("Резервация удалена")
            this.$router.go()
        }
    }
}
</script>