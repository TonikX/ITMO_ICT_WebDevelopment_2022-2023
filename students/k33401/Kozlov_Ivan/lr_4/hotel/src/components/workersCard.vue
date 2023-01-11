<template>
    <tbody class="workers">
    <tr>
        <td id="table_id" >{{ table_number }}</td>
        <td>{{ fio }}</td>
        <td>{{ phone_worker }}</td>
        <td class="d-flex justify-content-start gap-2">
            <button  v-bind:id="table_number" type="button" class="btn btn-warning"
                     data-bs-toggle="modal" data-bs-target="#edit_workers"
                     @click="getTableNumber"
                    >Редактировать</button>
            <button v-bind:id="table_number" type="submit" class="btn btn-danger"
                    @click="getTableNumber">Удалить</button>
        </td>
    </tr>
    </tbody>



</template>
    
<script>
import modalForEdit from "@/components/modalForEdit.vue";

export default {
    name: 'WorkerCard',
    components: modalForEdit,

    // свойства, которые принимает компонент
    props: {
        table_number: {
            type: Number,
            required: true
        },
        fio: {
            type: String,
            required: true
        },
        phone_worker: {
            type: String,
            required: true
        }
    },

    methods:{
        getTableNumber: function (event) {
            localStorage.needed_table_number = event.originalTarget.id
        },
    }
}
</script>
