<template>


    <tbody class="RoomsBooks">
    <tr>
        <td>{{ room_number }}</td>
        <td>{{ number_contract }}</td>
        <td>{{ data_start_living }}</td>
        <td>{{ data_end_living }}</td>
        <td>{{ status_move }}</td>
        <td class="d-flex justify-content-start gap-2">
            <button v-bind:id="number_contract" type="button" class="btn btn-warning">Редактировать</button>
            <button v-if="status_move === 'не выселен' " v-bind:id="number_contract" type="button" class="btn btn-danger"
                    @click.prevent="moveOutBookPage()">Выселить</button>
            <button v-else v-bind:id="number_contract" type="button" class="btn btn-danger"
                    @click.prevent="moveInBookPage()">Заселить</button>
        </td>

    </tr>
    </tbody>

</template>

<script>
import { mapActions } from 'pinia'
import useBooksStore from "@/stores/book";

export default {
    name: "CurrentBooks",
    props:{
        number_contract:{
            required: true,
        },
        data_start_living:{
            required: true,
        },
        data_end_living:{
            required: true,
        },
        room_number:{
            required: true,
        },
        status_move:{
            required: true,
        }

    },

    methods:{
        ...mapActions(useBooksStore, ['updateBook']),

        async moveOutBookPage(){
            let form = {
                status_move: 'выселен'
            }

            if (confirm(`Вы уверены, что хотите выселить данного гостя (Номер договора = ${this.$props.number_contract})?`)){
                await this.updateBook(this.$props.number_contract, form)
                window.location.reload()
            }

        },


        async moveInBookPage(){
            let form = {
                status_move: 'не выселен',
            }

            if (confirm(`Вы уверены, что хотите заселить данного гостя (Номер договора = ${this.$props.number_contract})?`)){
                await this.updateBook(this.$props.number_contract, form)
                window.location.reload()
            }

        },


    },
}
</script>
