import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CalendarView from '@/views/CalendarView.vue'
import PersonalView from '@/views/PersonalView.vue'
import EntryView from '@/views/EntryView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import EventView from '@/views/EventView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: MainView
		},
		{
			path: '/calendar/',
			name: 'calendar',
			component: CalendarView
		},
		{
			path: '/personal/',
			name: 'personal',
			component: PersonalView
		},
		{
			path: '/entry/',
			name: 'entry',
			component: EntryView
		},
		{
			path: '/registration/',
			name: 'registration',
			component: RegistrationView
		},
		{
			path: '/event/',
			name: 'event',
			component: EventView
		},
	]
})

export default router
