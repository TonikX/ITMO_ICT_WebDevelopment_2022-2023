<template>
    <div class="col col-xl-7">
        <div class="card mb-5" style="border-radius: 15px;">
            <div class="card-body p-4">
                
                    <h4 class="mb-3 col-6 text-start">{{ name }}</h4>
                    
                <p class="small mb-0 text-start"><i class="far fa-star fa-lg"></i>{{ date }}</p>
                <p class="about mt-4">{{ intro }}</p>
                <hr class="my-4">
                <div class="d-flex justify-content-between align-items-center">
                    <p class="mb-0 text-uppercase"><i class="fas fa-cog me-2"></i> <span class="text-muted small">{{ category_name }}</span></p>
                    <button @click='certain_event()' class="btn btn-dark" value="{{ id }}val" id="infoButton">Подробнее</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: "EventElement",

        props: {
            id: {type: Number, required: true},
            category_name: {type: String, required: true},
            intro: {type: String, required: true},
            date: {type: String, required: true},
            reg: {type: String, required:false},
            name: {type: String, required:true}
        },

        methods: {
            certain_event() {
                this.$router.push(`events/${this.id}`)
            }
        }
    }
</script>