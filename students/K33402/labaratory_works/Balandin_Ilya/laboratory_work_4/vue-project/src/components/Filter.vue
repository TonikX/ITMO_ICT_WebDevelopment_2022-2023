<template>
  <div class="bg-light row justify-content-evenly align-items-end p-3">
    <div class="col col-md-3">
      <label for="platform" class="form-label fw-bold">Platform</label>
      <select class="form-select  bg-main-own text-main-own" aria-label="Platform" id="platform" tabindex="0">
        <option>Any</option>
      </select>
    </div>
    <div class="col col-md-3">
      <label for="genre" class="form-label fw-bold">Genre</label>
      <select class="form-select  bg-main-own text-main-own" aria-label="Genre" id="genre" tabindex="0">
        <option>Any</option>

      </select>
    </div>
    <div class="col col-md-1">
      <button type="submit" class="btn btn-primary" v-on:click="filtergames()">Submit</button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'pinia'
import useBazzarStore from "@/stores/bazzar";

export default {
  name: "FilterProducts",
  computed: {
    ...mapState(useBazzarStore, ['genres', 'platforms'])
  },

  methods: {
    ...mapActions(useBazzarStore, ['loadGenres', 'loadPlatforms']),

    filtergames: function () {
      const params = new URLSearchParams()
      const genre = document.getElementById('genre').value
      const platform = document.getElementById('platform').value
      if (genre !== 'Any') {
        params.append('genre', genre)
      }
      if (platform !== 'Any') {
        params.append('platform', platform)
      }
      location.replace(document.location.origin + document.location.pathname + `?${params.toString()}`)
    }
  },
  data() {
    return {
      genres_inner: {}
    }
  },
  mounted() {
    this.loadGenres()
    this.loadPlatforms()
    for (const g in this.genres) {
      document.getElementById('genre').innerHTML += `<option value="${this.genres[g].id}">${this.genres[g].name}</option>`
    }
    for (const p in this.platforms) {
      document.getElementById('platform').innerHTML += `<option value="${this.platforms[p].id}">${this.platforms[p].name}</option>`
    }
  }
}
</script>

<style scoped>

</style>