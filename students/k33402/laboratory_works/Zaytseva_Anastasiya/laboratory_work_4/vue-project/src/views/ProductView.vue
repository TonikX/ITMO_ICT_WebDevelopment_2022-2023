<script>
import { mapState, mapActions } from 'pinia'
import useUsersStore from '@/stores/users'
import useProductsStore from '@/stores/products'
import useOrdersStore from '@/stores/orders'
import { COLORS } from '@/const/lang'

export default {
  name: 'ProductView',
  data() {
    return {
      COLORS,
      cartCount: 1
    }
  },
  computed: {
    ...mapState(useProductsStore, ['product', 'products']),
    ...mapState(useUsersStore, ['token']),
    recommendedProducts() {
      return this.products
        .filter((p) => p.id !== this.product.id)
        .slice(0, 8);
    }
  },
  mounted() {
    this.fetchProduct(this.$route.params.id)
    this.$watch(
      () => this.$route.params,
      (toParams) => {
        this.fetchProduct(toParams.id)
      }
    )
  },
  methods: {
    ...mapActions(useProductsStore, ['fetchProduct']),
    ...mapActions(useOrdersStore, ['createCartItem']),
    plusOne() {
      this.cartCount += 1;
    },
    minusOne() {
      if (this.cartCount > 1) {
        this.cartCount -= 1;
      }
    },
    addToCart() {
      this.createCartItem(this.product.id, this.cartCount, this.token).then(() => {
        document.querySelector('.cart-icon-button').dispatchEvent(new Event('click'))
      })
    }
  }
}
</script>

<template>
<main class="container">
  <nav class="mt-4" aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><RouterLink to="/" class="link-dark">Главная</RouterLink></li>
      <li class="breadcrumb-item"><RouterLink to="/" class="link-dark">Одежда</RouterLink></li>
      <li class="breadcrumb-item"><RouterLink to="/" class="link-dark">Basic collection</RouterLink></li>
      <li class="breadcrumb-item active" aria-current="page">Бархатное платье</li>
    </ol>
  </nav>
  <div
    v-if="product.id"
    class="row mt-4"
  >
    <div class="col-12 col-sm-6">
      <img
        :src="product.photo"
        :alt="product.name"
        width="760"
        height="800"
        class="img-fluid"
      >
    </div>
    <form class="col-12 col-sm-6 mt-4 mt-sm-0">
      <h1>{{ product.name }}</h1>
      <h2>{{ product.price }}</h2>
      <p class="text-muted">
        Лаконичный дизайн, полуприлегающий крой. Платье-рубашка из бархата с оборками по низу является воплощением непринужденной элегантности и современности. Модель для удобных образов на каждый день.
      </p>
      <div class="row">
        <div class="col-auto">
          <strong>РАЗМЕР</strong>
        </div>
        <div class="col">
          <a href="#" class="text-muted">Таблица размеров</a>
        </div>
      </div>
      <div class="mt-2 mb-3">
        <input type="radio" class="btn-check" name="size" id="size-xs" autocomplete="off" checked>
        <label class="btn btn-outline-dark" for="size-xs">XS</label>

        <input type="radio" class="btn-check" name="size" id="size-s" autocomplete="off">
        <label class="btn btn-outline-dark" for="size-s">S</label>

        <input type="radio" class="btn-check" name="size" id="size-m" autocomplete="off">
        <label class="btn btn-outline-dark" for="size-m">M</label>

        <input type="radio" class="btn-check" name="size" id="size-l" autocomplete="off">
        <label class="btn btn-outline-dark" for="size-l">L</label>

        <input type="radio" class="btn-check" name="size" id="size-xl" autocomplete="off">
        <label class="btn btn-outline-dark" for="size-xl">XL</label>
      </div>
      <div class="row">
        <div class="col-auto">
          <strong>ЦВЕТ:</strong>
        </div>
        <div class="col">
          {{ COLORS[product.color] }}
        </div>
      </div>
      <div class="mt-2 mb-3">
        <input type="radio" class="btn-check" name="color" id="color-jut" autocomplete="off" checked>
        <label class="btn btn-outline-warning" for="color-jut">ЭКРЮ</label>

        <input type="radio" class="btn-check" name="color" id="color-gray" autocomplete="off">
        <label class="btn btn-outline-secondary" for="color-gray">СЕРЫЙ</label>

        <input type="radio" class="btn-check" name="color" id="color-black" autocomplete="off">
        <label class="btn btn-outline-dark" for="color-black">ЧЁРНЫЙ</label>
      </div>
      <div class="row mt-5">
        <div class="col-12 col-sm-auto">
          <div class="btn-group btn-group-lg" role="group" aria-label="amount">
            <button type="button" class="btn btn-outline-dark" @click="minusOne">-</button>
            <button type="button" class="btn btn-outline-dark" disabled>{{ cartCount }}</button>
            <button type="button" class="btn btn-outline-dark" @click="plusOne">+</button>
          </div>
        </div>
        <div class="col-12 col-sm mt-sm-0 mt-4">
          <button
            type="button"
            class="btn btn-outline-dark btn-lg"
            @click="addToCart"
          >ДОБАВИТЬ В КОРЗИНУ</button>
        </div>
      </div>
    </form>
  </div>



  <div class="row mt-5">
    <div
      v-for="p in recommendedProducts"
      :key="p.id"
      class="col-12 col-sm-3"
    >
      <RouterLink
        :to="`/products/${p.id}`"
        class="text-black nav-link"
      >
        <div class="card border border-0">
          <img
            :src="p.photo"
            class="card-img-top"
            :alt="p.name"
          >
          <div class="card-body px-0">
            <div class="row justify-content-between">
              <h6 class="col card-title">{{ p.name }}</h6>
              <h6 class="col card-title text-end text-muted">{{ p.price }}</h6>
            </div>
          </div>
        </div>
      </RouterLink>
    </div>
  </div>

</main>
</template>
