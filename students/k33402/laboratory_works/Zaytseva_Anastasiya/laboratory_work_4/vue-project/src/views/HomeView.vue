<script>
import { mapActions, mapState } from 'pinia';
import useProductsStore from '@/stores/products'
import ProductCard from '@/components/ProductCard.vue';
import FeaturesBanner from '@/components/FeaturesBanner.vue'
import { COLORS } from '@/const/lang';

export default {
  name: 'HomeView',
  components: { ProductCard, FeaturesBanner },
  data() {
    return {
      COLORS
    }
  },
  mounted() {
    this.fetchProductCount();
    this.fetchProducts(12);
  },
  computed: {
    ...mapState(useProductsStore, ['products', 'productCount', 'productColors', 'colorFilter']),
    productRows() {
      return this.getProductsRows(4)
    },
    isAllProductsListed() {
      return this.productCount === this.products.length
    }
  },
  methods: {
    ...mapActions(useProductsStore, ['fetchProducts', 'fetchProductCount', 'fetchProductsByColor']),
    getProductsRows(rowSize) {
      const productRows = [];
      for (let i = 0; i < this.products.length; i += rowSize) {
          const chunk = this.products.slice(i, i + rowSize);
          productRows.push(chunk);
      }
      return productRows;
    },
    showAllProducts() {
      this.fetchProductsByColor('')
    }
  }
}
</script>

<template>
  <main class="container">
    <nav class="mt-4" aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a class="link-dark" href="#">Главная</a></li>
        <li class="breadcrumb-item"><a class="link-dark" href="#">Одежда</a></li>
        <li class="breadcrumb-item active" aria-current="page">Basic collection</li>
      </ol>
    </nav>
    <div class="my-5">
      <div class="row align-items-center">
        <div class="col-auto">
          <h1 class="display-1"><strong>BASIC COLLECTION</strong></h1>
        </div>
        <div class="col text-secondary">
        </div>
      </div>
    </div>
    <div class="filters-row row mb-3">
      <div class="col d-flex justify-content-start">
        <div class="dropdown">
          <button class="btn btn-link dropdown-toggle link-dark nav-link" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            ФИЛЬТРЫ
          </button>
          <ul class="color-filter dropdown-menu">
            <p class="ps-4">Цвет</p>
            <li
              v-for="color in productColors"
              :key="color"
              @click="fetchProductsByColor(color)"
            >
              <button
                class="dropdown-item"
                :class="{ 'active': color === colorFilter }"
              >{{ COLORS[color] }}</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div
      v-for="(productRow, productRowIndex) in productRows"
      :key="`product-row-${productRowIndex}`"
      class="product-row row text-nowrap"
    >
      <ProductCard
        v-for="(product) in productRow"
        :key="`product-${product.id}`"
        :id="product.id"
        :photo="product.photo"
        :name="product.name"
        :price="product.price"
      />
    </div>
    <div class="row justify-content-center text-center mb-5 mt-3">
      <div class="col-auto">
        <p>ОТОБРАЖЕНО <span class="product-count-current">{{ products.length }}</span>
          ТОВАРОВ ИЗ <span class="product-count-total">{{ productCount }}</span></p>
        <button
          v-if="!isAllProductsListed"
          type="button"
          class="show-all-button btn btn-outline-dark"
          @click="showAllProducts"
        >ПОКАЗАТЬ ВСЕ</button>
      </div>
    </div>
    <FeaturesBanner />
  </main>
</template>
