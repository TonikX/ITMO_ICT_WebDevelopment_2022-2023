import { createRouter, createWebHistory} from 'vue-router'
import MainView from '@/views/MainView.vue'
import LkView from '@/views/LkView.vue'
import EnterView from '@/views/EnterView.vue'
import RegView from '@/views/RegView.vue'
import MusView from '@/views/MusView.vue'
import CalendarView from '@/views/CalendarView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: MainView
		},
		{
			path: '/lk/',
			name: 'lk',
			component: LkView
		},
		{
			path: '/enter/',
			name: 'enter',
			component: EnterView
		},
		{
			path: '/registration/',
			name: 'registration',
			component: RegView
		},
		{
			path: '/music/',
			name: 'music',
			component: MusView
		},
		{
			path: '/calendar/',
			name: 'calendar',
			component: CalendarView
		}
	]
})

export default router