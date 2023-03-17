<template>
    <div class="eventInfo d-flex justify-content-center">
<div class="row me-3 mt-5 col-xl-8 d-flex text-end">
            <div class="col-lg-6 align-items-center d-flex mb-5 mb-lg-0">
                <div class="blockabout">
                    <div class="blockabout-inner text-center text-sm-start" id="certainEventText">
                        <div class="title-big pb-3 mb-2">
                            <h3>{{ name }}</h3>
                        </div>
                        <p class="description-p text-muted pe-0 pe-lg-0">
                            {{ about }}
                        </p>
                        <p class="description-p text-muted pe-0 pe-lg-0">
                           {{category_name}}
                        </p>
                        <button @click="enrollEvent()" class="btn btn-dark">Зарегистрироваться на мероприятие</button>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 mt-5 text-center" id="certainEventInfo">
                <h5 class="text-end">{{data}}</h5>
                <h5 class="text-end">{{time}}</h5>
                <h5 class="text-end">{{city}}</h5>
                <h5 class="text-end">{{place_name}}</h5>
                <h5 class="text-end">{{street}}</h5>
            <h5 class = "text-end">{{organizer}}</h5>
            </div>
</div></div>

</template>

<script>
import { mapActions, mapState } from 'pinia'
import enrollmentStore from '@/store/enrollment_store';

export default {
        name: "EventAbout",

        props: {
            id: {type: Number, required: true},
            category_name: {type: String, required: true},
            about: {type: String, required: true},
            date: {type: String, required: true},
            time: {type: String, required:true},
            city: {type: String, required:true},
            place_name: {type: String, required:true},
            street: {type:String, required:true},
            organizer: {type:String,required:true},
            name: {type: String, required:true},
        },

        methods: {
            ...mapActions(enrollmentStore,['makeUserEnrollment']),
            
            async enrollEvent(){
                if(localStorage.user!=null){
                    const userId = parseInt(localStorage.user)
                    const eventId = this.id
                    const data = {}
                    data['user'] = userId
                    data['event'] = eventId
                    const response = await this.makeUserEnrollment(data)
                    if (response.data.err){
                        alert("Вы уже зарегистрированы на данное мероприятие")
                    }else{
                        alert("Вы зарегистрировались на мероприятие")
                 }
                }
                 else {
                    alert("Вы не вошли в систему. Залогиньтесь/зарегистрируйтесь для регистрации на мероприятие")
                 }
            }
        }
    }
</script>