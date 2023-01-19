<template>
  <section>
    <div class="container">
      <div class="row d-flex align-items-center">
        <div class="col-12 col-lg-6">
          <div class="menu-image h-100 d-flex align-items-start">
            <img src="@/assets/crypto-currency-isometric-design.png" class="img-fluid" alt="menu image">
          </div>
        </div>

        <div class="col-12 col-lg-6">
          <div class="menu-text flex-grow-1 py-2 px-5">
            <div class="py-4">
              <h2 class="text-left">Создайте свой криптопортфель</h2>
              <p class="fw-lighter fs-4">За три простых шага</p>
            </div>

            <div class="menu-content">
              <h3 class="h3-text-color py-2">1. Пополните кошелек</h3>
              <p class="fw-lighter">Пополните свой криптовалютный кошелек и начните торговать криптовалютой. Вы можете
                пополнить кошелек различными способами.</p>
            </div>

            <div class="menu-content">
              <h3 class="h3-text-color py-2">2. Пройдите верификацию</h3>
              <p class="fw-lighter">Пройдите верификацию личности, чтобы защитить свой аккаунт и транзакции.</p>
            </div>

            <div class="menu-content">
              <h3 class="h3-text-color py-2">3. Начинайте</h3>
              <p class="fw-lighter">Все готово! Покупайте/продавайте криптовалюту, настраивайте регулярные покупки для
                инвестиций.</p>
            </div>
          </div>

          <button @click="checkAuthForStart" type="button" class="btn btn-lg btn-main my-5 mx-5">
            Начать!
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "WelcomeSection",
  methods: {
    checkAuthForStart() {
      if (localStorage.getItem("auth_token")) {
        this.$router.push({name: "market"})
      } else {
        this.$router.push({name: "login"})
      }
    }
  }
}
</script>

<style scoped>

</style>