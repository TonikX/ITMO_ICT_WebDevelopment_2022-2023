<template>
    <footer class="footer py-5">
        <div class="row">
            <div class="col-6 col-md-2 mb-3">
                <h5>TI LLC</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Home</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Stocks</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Crypto</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Legal</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">About</a></li>
                </ul>
            </div>

            <div class="col-6 col-md-2 mb-3">
                <h5>Buy Crypto</h5>
                <ul class="nav flex-column">
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy Ethereum</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy Bitcoin</a></li>
                    <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-muted">Buy USDT</a></li>
                </ul>
            </div>
            <div class="col-6 col-md-2 mb-3"></div>

            <div class="col-md-5 offset-md-1 mb-3">
                <form>
                    <h5>Subscribe to our newsletter</h5>
                    <p>Monthly digest of what's new and exciting from us.</p>
                    <div class="d-flex flex-column flex-sm-row w-100 gap-2">
                        <label for="newsletter1" class="visually-hidden">Email address</label>
                        <input id="newsletter1" type="text" class="form-control" placeholder="Email address" />
                        <button class="btn btn-primary" type="button">Subscribe</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
            <p>&copy; 2022 TimofeevInvest INC INT LTD. All rights reserved.</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: "PageFooter",
};
</script>

<style></style>
