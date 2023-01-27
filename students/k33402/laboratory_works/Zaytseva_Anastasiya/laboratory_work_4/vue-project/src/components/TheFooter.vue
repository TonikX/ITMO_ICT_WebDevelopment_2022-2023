<template>
<div class="bg-dark text-white mt-5">
  <footer class="container pt-5 pb-3">
    <div class="row">
      <div class="col-md-5 mb-3">
        <form>
          <h5>Подписка на новостную рассылку</h5>
          <div class="d-flex flex-column flex-sm-row w-100 gap-2">
            <label for="newsletter1" class="visually-hidden">EMAIL ADDRESS</label>
            <input id="newsletter1" type="text" class="form-control" placeholder="EMAIL ADDRESS">
            <button class="btn btn-link" type="button" aria-label="Продолжить">
              <svg width="25" height="14" viewBox="0 0 25 14" aria-label="Продолжить" fill="none" xmlns="http://www.w3.org/2000/svg">
                <use xlink:href="#icon-arrow"></use>
              </svg>
            </button>
          </div>
        </form>
      </div>

      <div class="col-6 offset-md-1 col-md-2 mb-3">
        <ul class="nav flex-column">
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Коллекции</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Правовая информация</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Помощь</a></li>
        </ul>
      </div>

      <div class="col-6 col-md-2 mb-3">
        <ul class="nav flex-column">
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">О доставке</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Об оплате</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">О возврате</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Отслеживание заказов</a></li>
        </ul>
      </div>

      <div class="col-6 col-md-2 mb-3">
        <ul class="nav flex-column">
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Контакты</a></li>
          <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Найти магазин</a></li>
        </ul>
      </div>
    </div>

    <div class="d-flex flex-column flex-sm-row justify-content-between pt-4 mt-4">
      <img
        src="/img/payments.png"
        alt="Payment methods: Visa, Mastercard, Apple pay, Paypal"
        width="164"
        height="21"
      >
      <p>ⓒ Fabiana Filippina. Все права защищены.</p>
    </div>
  </footer>
</div>
</template>

<script>
export default {
  name: 'TheFooter',
}
</script>