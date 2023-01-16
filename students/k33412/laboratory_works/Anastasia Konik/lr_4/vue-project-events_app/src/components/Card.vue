<template>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" display="none">
    <symbol id="ShowMore" viewBox="0 0 16 16">
      <path
          d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
    </symbol>
  </svg>
  <img :src="img_src" class="card-img-top mt-2" style="height: 210px" :alt="title">
  <div class="card-body d-flex flex-column">
    <p class="card-title" style="font-size:18pt"><b>{{ title }}</b></p>
    <p class="card-text">{{ address }}</p>
    <p class="card-text">{{ short_description }}</p>
    <button :id="'event_showmore_'+ id" aria-pressed="true" @click="goToEvent(id)"
            class="btn mt-auto btn-dark purple_button event_showmore_btn">Show more
      <svg class="icon">
        <use xlink:href="#ShowMore"></use>
      </svg>
    </button>
  </div>
</template>

<script>

export default {
  name: 'Event',
  props: {
    title: {
      type: String,
      required: true
    },
    address: {
      type: String,
      required: true
    },
    img_src: {
      type: String,
      required: true
    },
    short_description: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    goToEvent(event_id) {
      this.$router.push(`/event/${event_id}`)
    },
  },
}
</script>

<style scoped>

</style>