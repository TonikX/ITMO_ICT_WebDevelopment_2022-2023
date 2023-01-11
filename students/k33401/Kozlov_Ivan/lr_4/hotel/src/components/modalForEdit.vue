<template>
    <label>ФИО </label>
    <input type="text" class="form-control" placeholder="" name="name" id="name" v-bind:value="fio">

    <label>Телефон</label>
    <input required type="text" class="form-control" name="phone" id="phone"
            v-bind:value="phone_worker">

    <div class="modal-footer">

        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
        <button type="submit" class="btn btn-primary">Сохранить изменения</button>
    </div>

</template>

<script>
export default {
    name: "modalForEdit",
    props: {
        fio: {
            type: String,
            required: true
        },
        phone_worker: {
            type: String,
            required: true
        }
    },

}
</script>
