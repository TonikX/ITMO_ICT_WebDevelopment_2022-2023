<template>
    <main>
       <div class="justify-content-center row">
        <div class="justify-content-center row">
            <div class="justify-content-center col-sm-5 my-3 mx-5 ">
                <LoginForm />
            </div>
        </div>
        <div class="col-sm-5 my-3 mx-5 justify-content-center row">
            <img src="../assets/img21.jpg" class="card-img-top" alt="...">
        </div>
    
     </div>
    </main>
</template>

<script>
    import LoginForm from "@/components/LoginForm";
    export default {
        name: "Login",
        components: {LoginForm}
    }
</script>

<style scoped>

</style>