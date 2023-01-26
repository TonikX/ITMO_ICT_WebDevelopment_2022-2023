<template>
  <div class="row row-cols-1 g-4">
    <div class="col">
      <div v-for="ownership in ownerships" v-bind:key="ownership" class="card shadow-sm my-3">
        <router-link :to="'/currency/' + ownership.currency.id" class="btn btn-light card-bg-color text-left">
          <div class="row d-flex align-items-center px-4">

            <div class="col-5 col-sm-3 col-xl-1 col-lg-2 d-flex justify-content-center">
              <img :src="ownership.currency.image" style="max-height:100px; max-width:100px;" class="img rounded-start"
                   alt="{{ownership.currency.name}}">
            </div>

            <div class="col-7 col-sm-9 col-xl-11 col-lg-10">
              <div class="card-body">
                <h5 class="card-title card-main-color">{{ ownership.currency.name }}</h5>

                <div class="row row-cols-1 row-cols-lg-2 row-cols-xl-4 pb-3">
                  <div class="col">
                    <p class="card-main-color"><small class="card-muted-color">1 {{
                        ownership.currency.abbreviation
                      }}:</small>
                      ${{ parseFloat(ownership.currency.price) }}</p>
                  </div>
                  <div class="col">
                    <p class="card-main-color"><small class="card-muted-color">Всего в портфеле:</small>
                      {{ ownership.count }}</p>
                  </div>
                  <div class="col">
                    <p class="card-main-color"><small
                        class="card-muted-color">Цена в портфеле:</small>
                      ${{ parseFloat(ownership.currency.price * ownership.count) }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserCurrenciesList",
  props: {
    ownerships: Array
  },
}
</script>
