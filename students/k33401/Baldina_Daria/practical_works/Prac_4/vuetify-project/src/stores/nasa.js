import { defineStore } from 'pinia'
import { nasaApi } from '@/api'

const useNasaStore = defineStore('photos', {
  state: () => ({
    photos: []
  }),

  actions: {
    async loadPhoto() {
      const response = await nasaApi.getPhoto()

      if (response.status !== 200) {
        throw new Error(response.error)
      }

      // пройдёмся по полученному массиву данных и
      // приведём его к тому виду, с которым будет
      // удобно работать
      const epicItems = response.data.map((epicItem) => {
        const date = new Date(epicItem.date)

        // собираем дату в нужном виде
        const year = date.getFullYear()

        const month = String(date.getMonth() + 1).length > 1
          ? date.getMonth() + 1
          : `0${date.getMonth() + 1}`

        const day = String(date.getDate()).length > 1
          ? date.getDate()
          : `0${date.getDate()}`

        epicItem.date = `${year}/${month}/${day}`

        // получаем картинку
        epicItem.image = 'https://api.nasa.gov/EPIC/archive/natural/${epicItem.date}/png/${epicItem.image}.png?api_key=pv7mgIb4MCWKU5a8q0Zm8phM3KZiCaKdOXA0Hmth'

        return epicItem
      })

      this.epicItems = epicItems
    }
  }
    }
  
)

export default useNasaStore