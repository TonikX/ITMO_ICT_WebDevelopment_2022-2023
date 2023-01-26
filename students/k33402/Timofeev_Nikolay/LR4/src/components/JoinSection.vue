<template>
    <section class="px-4 py-5 my-5 text-center">
        <img class="d-block mx-auto mb-4" src="img/unclesam.png" alt="" width="200" />
        <h1 class="display-5 fw-bold">New here?</h1>
        <div class="col-lg-6 mx-auto">
            <p class="lead mb-4">Take a quick tour into investment world</p>
            <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <button
                    type="button"
                    class="btn btn-primary btn-lg px-4 gap-3"
                    data-bs-toggle="modal"
                    data-bs-target="#loginModal"
                >
                    Join us now
                </button>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "JoinSection",
};
</script>

<style></style>
