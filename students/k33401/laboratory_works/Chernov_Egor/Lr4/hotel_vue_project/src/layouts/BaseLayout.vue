<template>
  <!--  <main>-->
  <!--    <slot />-->
  <!--  </main>-->
  <div class="background">
    <div class="blur">
      <slot/>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseLayout"
}
</script>

<style scoped>
.background {
  background-image: url(public/paco.jpg);
}

.blur {
  background: rgba(108, 122, 137, 0.2);
  backdrop-filter: blur(8px);
}
</style>