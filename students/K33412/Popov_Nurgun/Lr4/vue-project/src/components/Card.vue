<template>
  <section>
    <div class="row">
      <div class="card mx-auto col-auto mt-4 px-0" v-for="info in cardInfo" style="width: 18rem;">
        <img class="card-img-top" :key="info.id" :src="info.img_src">
        <div class="card-body">
          <h5 class="card-title card-text-size">{{info.title}}</h5>
          <p class="pt-2">{{info.date}}</p>
          <p>{{info.location}}</p>
          <router-link :to="`/Description/${info.id}`">
            <button  class="btn btn-primary mt-3 w-100">Подробнее</button>
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Card",
    props:{
      cardInfo:{
        type: Object,
        required: true
      }
    },
    mounted() {
    }
  }
</script>

<style scoped>
  .card-img-top {
    height: 12rem;
  }
  .card-text-size {
    font-size: x-large;
    font-weight: 500;
  }
</style>