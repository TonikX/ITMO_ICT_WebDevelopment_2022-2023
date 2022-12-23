<template>
<div class="modal fade" id="cart" tabindex="-1" aria-labelledby="cartModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="cartModalLabel">Корзина</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="row justify-content-between align-items-stretch">
          <div class="col-auto">
            <img
              src="/img/cart.png"
              alt="Плащ из шерсти"
              width="140"
              height="140"
            >
          </div>
          <div class="col">
            <h5>ПЛАЩ ИЗ ШЕРСТИ</h5>
            <h6>XS / КРАСНЫЙ</h6>
            <div class="btn-group btn-group" role="group" aria-label="amount">
              <button type="button" class="btn btn-outline-dark">-</button>
              <button type="button" class="btn btn-outline-dark" disabled>1</button>
              <button type="button" class="btn btn-outline-dark">+</button>
            </div>
          </div>
          <div class="col-auto">
            <div class="d-flex justify-content-between align-items-end flex-column" style="height:100%">
              <button type="button" class="btn-close" aria-label="Close"></button>
              <small>140.000,00 RUB</small>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <div class="row justify-content-between" style="width: 100%">
          <div class="col-auto">
            <strong>ПРОМЕЖУТОЧНЫЙ ИТОГ</strong>
          </div>
          <div class="col-auto">
            <strong>140.000,00 RUB</strong>
          </div>
        </div>
        <div class="d-grid w-100">
          <button type="button" class="btn btn-dark btn-lg" data-bs-dismiss="modal">ПЕРЕЙТИ К ОФОРМЛЕНИЮ ЗАКАЗА</button>
        </div>
        <div class="row text-sm">
          <small class="col">
            Комиссия, доставка и скидки рассчитываются на шаге “Оформление заказа”.
          </small>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'CartModal',
}
</script>