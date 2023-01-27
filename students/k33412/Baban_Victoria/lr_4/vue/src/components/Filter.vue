<!--
<template>
<div class="container d-flex p-3 justify-content-center h2">Найди подходящее мероприятие</div>
    <div class="container d-grid gap-2 d-md-flex justify-content-center">
        <div class="row">
            <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
                <select class="form-select event-region" aria-label=".form-select-lg example" id="district">
                    <option value="all-district">Район</option>
                    <option value="admiral">Адмиралтейский</option>
                    <option value="vasileostrov">Василеостровский</option>
                    <option value="vyborg">Выборгский</option>
                    <option value="kalininsk">Калининский</option>
                    <option value="kirov">Кировский</option>
                    <option value="krasnogvard">Красногвардейский</option>
                    <option value="krasnosel">Красносельский</option>
                    <option value="kronshtad">Кронштадский</option>
                    <option value="moskov">Московский</option>
                    <option value="nevsk">Невский</option>
                    <option value="petrograd">Петроградский</option>
                    <option value="center">Центральный</option>
                </select>
            </div>
            <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
                <select class="form-select event-category" aria-label=".form-select-lg example" id="category">
                    <option value="all-category">Категория</option>
                    <option value="theatre" @click="fetchEventsByCategory(value)">Театры</option>
                    <option value="concert" @click="fetchEventsByCategory(value)">Концерты</option>
                    <option value="games" @click="fetchEventsByCategory(value)">Игры</option>
                    <option value="sport" @click="fetchEventsByCategory(value)">Спорт и фитнес</option>
                    <option value="art" @click="fetchEventsByCategory(value)">Исскуство и культура</option>
                    <option value="career" @click="fetchEventsByCategory(value)">Карьера</option>
                </select>
            </div>
            <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
                <select class="form-select type-event" aria-label=".form-select-lg example" id="type-event">
                    <option value="all-type">Любой тип</option>
                    <option value="offline">Очно</option>
                    <option value="online">Онлайн</option>
                </select>
            </div>
            <form class="d-flex justify-content-end col input-group mb-3 search-form">
                <button class="btn btn-outline-secondary search-btn" type="submit" id="button-search">Поиск</button>
            </form>
        </div>
    </div>
</template>
-->

<template>
  <div class="container d-flex p-3 justify-content-center h2">Найди подходящее мероприятие</div>
  <div class="container d-grid gap-2 d-md-flex justify-content-center">
    <div class="row">
      <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
        <select class="form-select event-region" aria-label=".form-select-lg example" id="district" v-model="district">
          <option value="" >Район</option>
          <option value="admiral">Адмиралтейский</option>
          <option value="vasileostrov">Василеостровский</option>
          <option value="vyborg">Выборгский</option>
          <option value="kalininsk">Калининский</option>
          <option value="kirov">Кировский</option>
          <option value="krasnogvard">Красногвардейский</option>
          <option value="krasnosel">Красносельский</option>
          <option value="kronshtad">Кронштадский</option>
          <option value="moskov">Московский</option>
          <option value="nevsk">Невский</option>
          <option value="petrograd">Петроградский</option>
          <option value="center">Центральный</option>
        </select>
      </div>
      <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
        <select class="form-select event-category" aria-label=".form-select-lg example" id="category" v-model="category">
          <option value="">Категория</option>
          <option value="Театры" >Театры</option>
          <option value="Концерты" >Концерты</option>
          <option value="Игры" >Игры</option>
          <option value="Спорт и фитнес" >Спорт и фитнес</option>
          <option value="Исскуство и культура" >Исскуство и культура</option>
          <option value="Карьера и образование" >Карьера и образование</option>
        </select>
      </div>
      <div class="form col-12 col-sm-6 col-lg-4 col-md-5 col-xl-3">
        <select class="form-select type-event" aria-label=".form-select-lg example" id="type-event" v-model="type_event">
          <option value="">Любой тип</option>
          <option value="offline">Очно</option>
          <option value="online">Онлайн</option>
        </select>
      </div>
      <form class="d-flex justify-content-end col input-group mb-3 search-form">
        <button class="btn btn-outline-secondary search-btn" type="button" id="button-search" @click="filterEvents">Поиск</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'pinia';
import useEventsStore from '@/stores/event'

export default {
  name: "Filter",
  data() {
    return {
      category: '',
      district: '',
      type_event: ''
    }
  },
  computed: {
    ...mapState(useEventsStore, ['events', 'categoryFilter', 'districtFilter', 'typeFilter']),
  },
  methods: {
    ...mapActions(useEventsStore, ['fetchEventsByCategoryDistrictType']),

    filterEvents() {
      this.fetchEventsByCategoryDistrictType(this.category, this.district, this.type_event)
    }
  }


}
</script>

<style scoped>

</style>