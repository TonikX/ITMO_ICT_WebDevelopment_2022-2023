<template>
<div class="container">
        <div class="row mt-4 col-xl-12" id="search_form">
            <div class="col-lg-6">
              <select class="form-select text-center" id="category_input" v-model="category_selected">
                <option value="none" selected>Категория</option>
                <option v-for="(cat) in categories" :value="cat.id">{{ cat.name }}</option>
              </select>
            </div>
            <div class="city-block col-lg-6">
              <select class="form-select text-center" id="city_input" v-model="city_selected">
                <option value="none" selected>Город</option>
                <option value="Moscow">Москва</option>
                <option value="Saint-Petersburg">Санкт-Петербург</option>
                <option value="Kazan">Казань</option>
              </select>
            </div>
            <div class="submit-block col-lg- text-center mt-3">
              <button @click="getFilteredEvents(this)" type="submit" class="btn btn-success submit-button" id="search_button">Поиск</button>
            </div>
          </div>

      <div class="row d-flex justify-content-center  h-100" id="eventsContainer" style="margin-top: 40px;">
        <EventElement v-for="(event) in events"
                        :id="event.id"
                        :category_name="event.category.name"
                        :intro="event.intro"
                        :date="event.date"
                        :reg="event.reg"
                        :name="event.name"
        />
      </div>
    </div>
</template>

<script>
import { mapActions, mapState } from 'pinia';
import eventsStore from "@/store/event_store"
import EventElement from "@/components/EventElement.vue"
import categoriesStore from "@/store/category_store"

export default {
    name: "EventList",
    components: {EventElement},
    computed: {
        ...mapState(eventsStore, ['events']),
        ...mapState(categoriesStore, ['categories']),
        Events() {
            return this.events
        },
        Categories() {
            return this.categories
        }
    },
    methods: {
        ...mapActions(eventsStore,['getEvents']),
        ...mapActions(eventsStore,['getFilteredEventsByCategory']),
        ...mapActions(eventsStore,['getFilteredEventsByCategoryAndCity']),
        ...mapActions(eventsStore,['getFilteredEventsByCity']),
        ...mapActions(categoriesStore, ['getCategories']),

        getFilteredEvents(event){
          
          if (this.category_selected!="none" || this.city_selected!="none"){
            if (this.category_selected!="none"&&this.city_selected!="none"){
               this.getFilteredEventsByCategoryAndCity(this.category_selected, this.city_selected)
            }
            if (this.city_selected!="none") {
                this.getFilteredEventsByCity(this.city_selected)
            } else {
                this.getFilteredEventsByCategory(this.category_selected)
            }
          }else {
            return this.getEvents()
          }
        }
    },
    mounted() {
        this.getEvents()
        this.getCategories()
        this.category_selected = "none"
        this.city_selected = "none"
    }
}


</script>