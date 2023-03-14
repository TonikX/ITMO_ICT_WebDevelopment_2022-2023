<template>
  <div class="container-fluid my-navbar sticky-top">
    <nav class="navbar navbar-light">
      <div class="d-flex">
        <router-link to="/" class="navbar-brand">
          <img
            src="@/assets/logo.png"
            width="30"
            height="30"
            class="d-inline-block align-top"
            alt=""
          />
          <span>Picterest</span>
        </router-link>

        <div class="input-group align-items-center search-input-group">
          <div class="input-group-prepend search-prepend">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-search"
              viewBox="0 0 16 16"
            >
              <path
                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
              />
            </svg>
          </div>
          <input
            @keyup.enter="searchPhotos"
            v-model="searchQuery"
            placeholder="Search"
            class="search-input"
            aria-label="search"
            aria-describedby="search-icon"
          />
        </div>
      </div>

      <div class="d-flex">
        <button
          v-b-toggle.collapse
          class="btn-secondary btn-sm">
          Filters
        </button>
        <ProfileBlock></ProfileBlock>
      </div>
    </nav>

    <b-collapse class="collapse filters mt-2 ml-4" id="collapse">
      <h5>Filters</h5>
      <div class="row mt-3">
        <div class="col-4">
          <h6>Order By</h6>
          <b-form-radio-group
            v-model="filters.order_by"
            :options="orderOptions"
            name="order options"
          >
          </b-form-radio-group>
        </div>

        <div class="col-4">
          <h6>Color</h6>
          <b-form-radio-group
            v-model="filters.color"
            :options="colorOptions"
            name="color options"
          >
          </b-form-radio-group>
        </div>

        <div class="col-4">
          <h6>Content Filter</h6>
          <b-form-radio-group
            v-model="filters.content_filter"
            :options="contentFilterOptions"
            name="safety options"
          >
          </b-form-radio-group>
        </div>
      </div>
    </b-collapse>
  </div>
</template>

<script>
import ProfileBlock from '@/components/ProfileBlock'

export default {
  name: 'TheNavbar',

  data () {
    return {
      searchQuery: null,
      orderOptions: [
        { text: 'Relevant', value: 'relevant' },
        { text: 'Latest', value: 'latest' }
      ],
      colorOptions: [
        { text: 'Any', value: null },
        { text: 'Black', value: 'black' },
        { text: 'Teal', value: 'teal' },
        { text: 'Green', value: 'green' },
        { text: 'Yellow', value: 'yellow' },
        { text: 'Black and White', value: 'black_and_white' },
        { text: 'Red', value: 'red' }
      ],
      contentFilterOptions: [
        { text: 'Low', value: 'low' },
        { text: 'High', value: 'high' }
      ],
      filters: {
        color: null,
        order_by: 'relevant',
        content_filter: 'low'
      }
    }
  },

  methods: {
    searchPhotos () {
      this.$store.dispatch('searchPhotos', { query: this.searchQuery, filters: this.filters })
    }
  },

  components: {
    ProfileBlock
  }
}
</script>

<style scoped></style>
