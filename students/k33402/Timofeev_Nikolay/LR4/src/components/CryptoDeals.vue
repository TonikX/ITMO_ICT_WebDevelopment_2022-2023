<template>
    <section>
        <p class="text-center lead py-5">Deals</p>
        <span v-if="deals.length">
            <ul class="list-group list-group-flush">
                <li
                    v-for="deal in deals"
                    :key="deal"
                    class="mx-auto list-group-item d-flex justify-content-between col-6"
                >
                    <span>@{{ deal.seller }} {{deal.type_offer}} {{ deal.count }}</span>
                    <button
                        @click="cancelDeal(deal.id)"
                        v-if="deal.my_request"
                        class="text-white badge bg-danger rounded-pill"
                    >
                        Cancel
                    </button>
                    <button v-else @click="processDeal(deal)" class="text-white badge bg-success rounded-pill">
                        Buy for {{ deal.price }}$
                    </button>
                </li>
            </ul>
        </span>
        <span v-else>
            <p class="lead text-center">Seems that no one are selling {{ name }} now...</p>
        </span>
    </section>
</template>

<script>
import { useToast } from "vue-toastification";

export default {
    setup() {
        const toast = useToast();
        return { toast };
    },
    name: "CryptoDeals",
    props: ["deals", "name"],
    methods: {
        async cancelDeal(deal_id) {
            this.axios.delete(`http://localhost:8088/market-requests/${deal_id}/`, {
                headers: {
                    Authorization: `Token ` + localStorage.getItem("token"),
                },
            });
            this.toast.info("Canceled");
        },
        async processDeal(deal) {
            this.axios
                .patch(
                    `http://localhost:8088/market-requests/${deal.id}/`,
                    {},
                    {
                        headers: {
                            Authorization: `Token ` + localStorage.getItem("token"),
                        },
                    }
                )
                .then((res) => this.toast.success(`Order ${res.data.id} processed!`))
                .catch(() => this.toast.error('Insufficient balance!'));
        },
    },
};
</script>

<style></style>
