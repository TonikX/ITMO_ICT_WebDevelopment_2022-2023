import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const accessKey = '4WtZzqzkj1jpOdx3igqSGJuGBWg2gheh_QvIARzn40M'

export default new Vuex.Store({
  state: {
    photos: null,
    postPhoto: null,
    likedPhotos: null
  },

  getters: {
    photos (state) {
      return state.photos
    },

    postPhoto (state) {
      return state.postPhoto
    },

    likedPhotos (state) {
      return state.likedPhotos
    }
  },

  mutations: {
    setPhotos (state, payload) {
      state.photos = payload
    },

    setPostPhoto (state, payload) {
      state.postPhoto = payload
    },

    setLikedPhotos (state, payload) {
      state.likedPhotos = payload
    }
  },

  actions: {
    async searchPhotos (context, { query, filters }) {
      if (query == null) {
        return
      }

      if (filters.color === null) {
        delete filters.color
      }

      try {
        const response = await axios.get('https://api.unsplash.com/search/photos', {
          params: {
            client_id: accessKey,
            per_page: 20,
            query,
            ...filters
          }
        })

        if (response.status === 200) {
          context.commit('setPhotos', response.data.results)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async getPhotos (context) {
      try {
        const response = await axios.get('https://api.unsplash.com/photos', {
          params: {
            client_id: accessKey,
            order_by: 'popular',
            per_page: 20
          }
        })

        if (response.status === 200) {
          context.commit('setPhotos', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async loadPhoto (context, id) {
      try {
        const response = await axios.get('https://api.unsplash.com/photos/' + id, {
          params: {
            client_id: accessKey
          }
        })

        if (response.status === 200) {
          context.commit('setPostPhoto', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    },

    async getLikedPhotos (context, { accessToken, userId }) {
      try {
        const response = await axios.get('http://localhost:3000/600/likedPhotos?userId=' + userId, {
          headers: {
            Authorization: 'Bearer ' + accessToken
          }
        })

        if (response.status === 200) {
          context.commit('setLikedPhotos', response.data)
        }
      } catch (e) {
        console.log(e)
      }
    }
  }
})
