<template>

    <base-layout>
        <div v-if="!chechkAuth">
            <div class="d-flex justify-content-end ">
                <button type="button" class="btn btn-dark p-2 flex-grow-1 rounded-0"
                        data-bs-target="#add_workers" data-bs-toggle="modal">Добавить сотрудника</button>
            </div>
            <form ref="deleteWorkerForm" @submit.prevent="deleteWorkerPage">
            <table class="table table-hover table-bordered" style="color: rgb(0, 0, 0)" id="myTable">
                <thead>
                <tr>
                    <th scope="col">Табельный номер</th>
                    <th scope="col">
                        <input class="form-control me-2" type="search" placeholder="Поиск по ФИО"
                               id="myInput" @keypress.enter.prevent="findPosition">
                        ФИО</th>
                    <th scope="col">Телефон</th>

                    <th scope="col">Действия</th>
                </tr>
                </thead>
                    <worker-card v-for="worker in workers.results"
                                 v-bind:key="worker.table_number"
                                 v-bind:fio="worker.fio"
                                 v-bind:phone_worker="worker.phone_worker"
                                 v-bind:table_number="worker.table_number">
                    </worker-card>
            </table>
            </form>
        </div>

        <div v-if="chechkAuth" class="d-flex justify-content-center my-2">
            <h1> У вас нет доступа к этой странце</h1>
        </div>

        <div class="modal fade" id="edit_workers" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Изменить сотрудника</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <article class="card-body">
                            <div>
                                <button class="btn btn-info" @click="getCurrWorker">Получить текущие данные работника</button>
                            </div>
                            <form ref="changeWorkerForm" @submit.prevent="changeWorkerPage">
                                <modal-for-edit
                                   fio=""
                                   phone_worker="">

                                </modal-for-edit>


                            </form>
                        </article> <!-- card-body end .// -->
                    </div>

                </div>
            </div>
        </div>

        <div class=" modal fade" id="add_workers" tabindex="-1"
             role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Добавить сотрудника</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <article class="card-body">
                            <form ref="createWorkerForm" @submit.prevent="createWorkerPage">
                                <label>ФИО </label>
                                <input v-model="form_create.fio" type="text" class="form-control" placeholder="" name="name" id="name">

                                <label>Телефон</label>
                                <input v-model="form_create.phone_worker" required type="text"
                                       class="form-control" name="phone" id="phone">

                                <label>Табельный</label>
                                <input v-model="form_create.table_number" required type="text"
                                       class="form-control" name="phone" id="phone">

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


    </base-layout>
</template>

<script>
import WorkerCard from '@/components/workersCard.vue'
import BaseLayout from '@/layouts/BaseLayout.vue'
import modalForEdit from "@/components/modalForEdit.vue";
import useWorkersStore from '@/stores/workers'
import {mapActions, mapState} from 'pinia'
import {checkTokenApi} from "@/api";

export default {
    name: 'WorkerPage',

    components: { BaseLayout, WorkerCard, modalForEdit },

    computed: {
        ...mapState(useWorkersStore, ['workers']),

        chechkAuth() {
            // eslint-disable-next-line vue/no-async-in-computed-properties
            checkTokenApi.checkToken().catch( function(error) { localStorage.setItem("status_answer1", error.response.status) });


            if ( localStorage.status_answer1 === '401'){
                localStorage.removeItem("status_answer1")
                return true
            }

            else{
                localStorage.removeItem("status_answer1")
                return false
            }

        },

    },

    methods: {
        ...mapActions(useWorkersStore, ['loadWorkers', 'createWorker', "getFIO", "changeWorker", "deleteWorker"]),

        findPosition() {
            var input, filter, table, tr, td, i;
            input = document.getElementById("myInput");
            filter = input.value.toUpperCase();
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[1];
                if (td) {
                    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }
        },

        getCurrWorker() {
            this.getFIO(localStorage.needed_table_number)
            document.getElementById("name").value = localStorage.currFIO
            document.getElementById("phone").value = localStorage.currPhone
        },

        async changeWorkerPage() {
            let form = {
                fio :  document.getElementById("name").value,
                phone_worker :   document.getElementById("phone").value,
                table_number: localStorage.needed_table_number
            }

            await this.changeWorker(form)
            window.location.reload()
        },

        async deleteWorkerPage(){
            if (confirm(`Вы уверены, что хотите удалить данного сотрудника(Табельный номер = ${localStorage.needed_table_number})?\nЭта операция не восстановима.`)){
                await this.deleteWorker()
                window.location.reload()
            }
        },

        async createWorkerPage(){
            await this.createWorker(this.form_create)
            window.location.reload()
        }

    },

    data() {
        return {
            form_create: {
                fio: '',
                phone_worker: '',
                table_number: ''
            }
        }
    },

    mounted() {
        this.loadWorkers()
    }

}

</script>

