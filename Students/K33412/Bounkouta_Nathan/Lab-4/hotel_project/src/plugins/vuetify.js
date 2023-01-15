import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#4bb6b2',
        secondary: '#6ec6c9',
        accent: '#f16d56',
        error: '#FF5252',
        info: '#457e8f',
        success: '#4CAF50',
        warning: '#FFC107',
        lightblue: '#14c6FF',
        yellow: '#FFCF00',
        pink: '#FF1976',
        orange: '#FF8657',
        magenta: '#C33AFC',
        darkblue: '#1E2D56',
        gray: '#909090',
        neutralgray: '#e8f2f6',
        green: '#f5fde6',
        red: '#FF5c4E',
        darkblueshade: '#308DC2',
        lightgray: '#BDBDBD',
        lightpink: '#FFCFE3',
        white: '#FFFFFF'
      }
    }
  }
})