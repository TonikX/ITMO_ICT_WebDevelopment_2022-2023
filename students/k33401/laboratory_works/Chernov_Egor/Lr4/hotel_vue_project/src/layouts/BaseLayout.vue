<template>
    <main class="background">
      <div class="blur">
        <slot />
      </div>
    </main>
<!--  <div class="background">-->
<!--    <div class="blur">-->
<!--      <slot/>-->
<!--    </div>-->
<!--  </div>-->
</template>

<script>
export default {
  name: "BaseLayout"
}
</script>

<style scoped>
/*main {*/
/*  height: 100%;*/
/*}*/

.background {
  background: url(public/hill.jpg) no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

.blur {
  background: rgba(243, 233, 221, 0.2);
  backdrop-filter: blur(8px);
  /*min-height: min-content;*/
}
</style>