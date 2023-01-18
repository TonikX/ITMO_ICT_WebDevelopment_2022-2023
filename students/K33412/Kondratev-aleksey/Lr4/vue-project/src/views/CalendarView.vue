<template>
  <header-block />
  <base-layout>
    <h1>Календарь событий</h1>

    <full-calendar
      :options="{
        events: calendarEvents,
        eventChange: handleEventChange,
        dateClick: handleDateClick,
        eventClick: handleEventClick
      }"
    />

    <!-- Modal -->
    <div class="modal fade" ref="detailEvent" tabindex="-1" aria-labelledby="detailEventLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="detailEventLabel">{{ selectedEvent.title }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p><strong>Описание:</strong> {{ selectedEvent.description }}</p>

            <p>{{ selectedEvent.formattedDate() }}</p>
          </div>
          <div class="modal-footer">
            <form action="" @submit.prevent="deleteMero(selectedEvent.id)">
              <button type="submit" class="btn btn-danger">Удалить</button>
            </form>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" ref="eventCreate" tabindex="-1" aria-labelledby="eventCreateLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="eventCreateLabel">Добавить событие</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm" class="d-flex flex-column" ref="eventForm">
              <input type="text" v-model="form.title" class="my-1">
              <input type="date" v-model="form.date" class="my-1">
              <textarea cols="30" rows="10" v-model="form.description" class="my-1" />

              <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </base-layout>
  <footer-block />
</template>

<script>
import { mapActions, mapState } from 'pinia'
import { Modal } from 'bootstrap'

import useCalendarEventsStore from '@/stores/calendarEvents'

import BaseLayout from '@/layouts/BaseLayout.vue'
import HeaderBlock from '@/components/Header.vue'
import FullCalendar from '@/components/FullCalendar.vue'
import FooterBlock from '@/components/Footer.vue'

export default {
  name: 'CalendarPage',

  components: { BaseLayout, FullCalendar, HeaderBlock, FooterBlock},

  computed: {
    ...mapState(useCalendarEventsStore, {
      calendarEvents: 'calendarEvents',
      selectedEvent: (state) => {
        return {
          ...state.selectedEvent,
          formattedDate: () => {
            const date = state.selectedEvent.date
            return new Date(date).toLocaleDateString('ru-RU')
          }
        }
      }
    })
  },

  data() {
    return {
      form: {
        title: '',
        description: '',
        date: ''
      },

      eventCreateModal: null
    }
  },

  methods: {
    ...mapActions(useCalendarEventsStore, ['loadCalendarEvents', 'loadEventById', 'createEvent', 'deleteEvent']),

    handleEventChange(payload) {
      console.log('event change', payload)
    },

    handleDateClick(payload) {
      console.log('date clicked', payload)

      const { dateStr } = payload
      this.form.date = dateStr

      this.eventCreateModal = new Modal(this.$refs.eventCreate)
      this.eventCreateModal.show()
    },

    async handleEventClick(payload) {
      await this.loadEventById(payload.event._def.publicId)

      const eventModal = new Modal(this.$refs.detailEvent)
      eventModal.show()
    },

    async submitForm() {
      await this.createEvent(this.form)

      this.$refs.eventForm.reset()
      this.eventCreateModal.hide()

      await this.loadCalendarEvents()
    },

    async deleteMero(id) {
      this.deleteEvent(id);

      location.reload();
    }
  },

  mounted() {
    this.loadCalendarEvents()
  }
}
</script>