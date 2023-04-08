<template>
    <main>
        <div class="justify-content-center row">
            <div class="col-sm-5 my-3 mx-5 justify-content-center row">
                <RegistrationForm />
            </div>
        </div>
        <div class="justify-content-center row">
        <div class="col-sm-5 my-3 mx-5 justify-content-center row">
            <img src="../assets/regist.jpg" class="card-img-top" alt="...">
        </div>
    </div>
    </main>
</template>

<script>
    import RegistrationForm from "@/components/RegistrationForm";
    export default {
        name: "Registration",
        components: {RegistrationForm}
    }
</script>

<style scoped>

</style>