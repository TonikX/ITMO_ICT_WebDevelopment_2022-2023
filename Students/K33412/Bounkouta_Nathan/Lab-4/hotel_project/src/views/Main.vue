<template>
  <div>
    <br>
    <slider :width="300" format="push" direction="right"
            :opacity="0.15"
            :links="[{'id': 1, 'text': 'Комнаты', 'url': '/rooms/'},
                     {'id': 2, 'text': 'Бронь', 'url': '/bookings/create/'},
                     {'id': 3, 'text': 'Гости', 'url': '/clients/'},
                     {'id': 4, 'text': 'Список бронирований', 'url': '/bookings/'},
                     {'id': 5, 'text': 'Наши сотрудники', 'url': '/employees/'},
                     {'id': 6, 'text': 'Выйти', 'url': '/logout/'}]"
    >
    </slider>
    <div class="text-center">
      <br>
      <v-img
          :src="require('../assets/hotel.jpg')"
          class="my-3"
          contain
          height="450"
        />
    </div>
    <br>
    <v-row>
      <v-col cols="12">
        <div style="text-align: center;">
          <center>
          <v-card color="white" width="1300px"
          elevation="10"
          outlined>
            <v-card-title>
            Поскольку большинство посетителей, которые останавливаются здесь, являются странствующими торговцами,
            гостиница предоставляет им место для торговли и установки киосков. Вид с вершины постоялого двора
            потрясающий - если позволяет погода, вдали можно увидеть Заоблачный предел и возвышающийся за ним пик
            Цинъюнь.
            </v-card-title>
          </v-card>
          <br>
          <v-card color="white" width="1310px"
          elevation="10"
          outlined>
            <v-card-title>
            Ходят слухи, что постоялый двор «Ваншу» хранит в себе тайну. Одна из легенд гласит, что госиница
            была построена для Алатуса, единственного выжившего Яксы. Некий агент Цисин в ходе неизвестного
            приказа построил постоялый двор, как прикрытие для поддержания жизни Адепта и его борьбы со злыми духами.
            </v-card-title>
          </v-card>
          </center>
          <br>
          <h2>Как нас найти:</h2></div>
        <v-img
          :src="require('../assets/map.jpg')"
          class="my-3"
          contain
          height="300"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Slider from '@jeremyhamm/vue-slider'
export default {
  name: 'Main',
  components: {
    slider: Slider
  }
}
</script>

<style>
</style>