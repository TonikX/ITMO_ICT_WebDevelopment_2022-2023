<template>
    <BaseLayout>
        <div v-if="checkStstusBook()" class="alert alert-success rounded-0 row justify-content-center">
                Комната свободна:
            <div class="row justify-content-center">
                <button class="btn btn-success btn-sm w-auto"
                        data-bs-target="#createBook" data-bs-toggle="modal">
                    Заселить</button>
            </div>
        </div>

        <div v-if="!checkStstusBook()">
             <strong class="alert alert-danger rounded-0 row justify-content-center">
                 Комната занята
             </strong>
        </div>


        <table class="table table-hover table-bordered" style="color: rgb(0, 0, 0)" id="myTable">
            <thead>
            <tr>
                <th scope="col">Номер комнаты</th>
                <th scope="col">Номер договора</th>
                <th scope="col">Начало</th>
                <th scope="col">Конец</th>
                <th scope="col">Состояние</th>
                <th scope="col">Действия</th>
            </tr>
            </thead>

        <current-books
            v-for="book in books.results"
            v-bind:room_number="book.room"
            v-bind:number_contract="book.number_contract"
            v-bind:data_end_living="book.data_end_living"
            v-bind:data_start_living="book.data_start_living"
            v-bind:status_move="book.status_move">
        </current-books>
        </table>

        <div class="modal fade" id="createBook" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Заселить</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <article class="card-body">

                            <form ref="createBookForm" @submit.prevent="createBookPage()">

                                <label>Номер договора </label>
                                <input v-model="form.number_contract" type="text" class="form-control" placeholder="">

                                <label>Дата начала проживания</label>
                                <input v-model="form.data_start_living" type="date" class="form-control">

                                <label>Дата конца проживания</label>
                                <input v-model="form.data_end_living" type="date" class="form-control">

                                <label> Статус оплаты </label>
                                <div>
                                    <select v-model="form.status_payment"  id="paymentStatis" class="form-select">
                                        <option value="О">Оплачено</option>
                                        <option value="Н">Не оплачено</option>
                                    </select>
                                </div>

                                <label>Номер комнаты</label>
                                <input v-model="form.room" type="number" class="form-control">

                                <label>Паспорт</label>
                                <input v-model="form.passport_client"  type="text" class="form-control">

                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                                    <button type="submit" class="btn btn-primary">Создать</button>
                                </div>

                            </form>
                        </article> <!-- card-body end .// -->
                    </div>

                </div>
            </div>
        </div>

    </BaseLayout>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import BaseLayout from "@/layouts/BaseLayout.vue";
import CurrentBooks from "@/components/CurrentBooks.vue";
import useBooksStore from "@/stores/book";


export default {
    name: "CurrentBooksForRoom",
    components:{BaseLayout, CurrentBooks},

    computed: {
        ...mapState(useBooksStore, ['books']),
    },

    methods: {
        ...mapActions(useBooksStore, ["sortBooks", "createBook"]),

        checkStstusBook(){
            let currentDate = new Date();
            let split_date = currentDate.toLocaleDateString().split('.')
            let sep= '-'
            let newDate = split_date[2] + sep + split_date[1] + sep + split_date[0]

            if(this.books.results){

            for (const book of this.books.results) {
               if((newDate < book.data_end_living) && (book.status_move === "не выселен")){
                   return false
               }
            }
            return true
        }
            },

        currRoom(){
            return localStorage.current_room
        },

        async createBookPage(){
            await this.createBook(this.form)
            window.location.reload()
        },

    },

    data(){
        return{
            form:{
                number_contract: '',
                data_start_living: '',
                data_end_living: '',
                status_book: 'З',
                status_payment: '',
                room: '',
                identifier_worker: 7616,
                passport_client: '',
                status_move: 'не выселен',

            }
        }
    },

    mounted() {
        this.sortBooks(localStorage.current_room)
    }

}
</script>

