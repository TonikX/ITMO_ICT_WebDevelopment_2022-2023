import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        url_server: "http://127.0.0.1:8000/",
        url_media: "http://127.0.0.1:8000",
        auth_user: false,
        user: '',
    },
    getters: {
        get_url_server(state) {
            return state.url_server
        },
        get_url_media(state) {
            return state.url_media
        },
        get_auth(state) {
            return state.auth_user
        },
        // Получаю инфу о юзере
        get_user_info(state) {
            return state.user
        },
    },
    mutations: {
        set_auth(state, value) {
            state.auth_user = value
        },
        // Записываю инфу о юзере
        set_user_info(state, value) {
            state.user = value
        }
    },
    actions: {
        user_info(context) {
            $.ajax({
                async: false,
                url: context.getters.get_url_server + "api/v1/profile/",
                type: "GET",
                success: (response) => {
                    context.commit('set_user_info', response)
                },
                error: (response) => {
                    if (response.status === 400) {

                    }
                }
            });
        }
    }
})
