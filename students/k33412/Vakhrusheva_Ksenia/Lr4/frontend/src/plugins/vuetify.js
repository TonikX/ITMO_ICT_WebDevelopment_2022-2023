import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

import {createVuetify} from 'vuetify'
import {VDataTable} from 'vuetify/labs/VDataTable'

export default createVuetify({
	components: {
		VDataTable,
	},
	theme: {
		themes: {
			light: {
				colors: {
					primary: '#804000',//'#1867C0',
					secondary: '#C9A079', // '#5CBBF6',
				},
			},
		},
	},
})
