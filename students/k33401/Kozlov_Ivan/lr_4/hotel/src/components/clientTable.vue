<template>
    <tbody class="Clients">
    <tr>
        <td>{{ passport }}</td>
        <td>{{ phone_client }}</td>
        <td>{{ email_client }}</td>
        <td>{{ name }}</td>
        <td>{{ last_name }}</td>
        <td>{{ father_name }}</td>
        <td>{{ address }}</td>
        <td class="d-flex justify-content-start gap-2">
            <button v-bind:id="passport" type="button" class="btn btn-warning">Редактировать</button>
            <button v-bind:id="passport" type="button" class="btn btn-info">История</button>
            <button v-bind:id="passport" type="button" class="btn btn-danger">Удалить</button>
        </td>

    </tr>
    </tbody>

</template>

<script>
export default {
    name: "clientTable",
    props:{
        passport:{},
        phone_client:{},
        email_client:{},
        name:{},
        last_name:{},
        father_name:{},
        address:{},
    }
}
</script>

<style scoped>

</style>
