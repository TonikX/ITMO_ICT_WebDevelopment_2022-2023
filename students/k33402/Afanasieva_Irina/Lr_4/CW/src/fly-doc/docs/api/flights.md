## Список Рейсов

Страница содержит данные о рейсах с возможность фильтрации по пункту отправления.
Доступно изменение и удаление существующих записей, а также добавление новых.

**URL** : `/flight`

**Methods** : `GET`, `POST`, `PUT`, `DELETE`

**Success Code** : `200 OK`

```
<template>
  <section>
    <place-form :from="savedPlace" />
    <v-row>
      <v-form @submit.prevent="submitPlace" ref="form" class="my-2">
        <v-row>
          <v-col cols="3" class="mx-auto">
            <v-text-field
              label="Введите пункт вылета"
              v-model="from"
              name="from"
              placeholder="Spb"
            />
          </v-col>
        </v-row>
      </v-form>
      <v-col cols="6" class="mx-auto">
        <flight-item-card
          v-for="flightItem in flightItems"
          :key="flightItem.identifier"
          :flight-item="flightItem"
          class="my-2"
        />
        <v-btn
          color="#3f57c4bb"
          class="mb-3 mr-3"
          @click="$router.push('/flight/create/')"
          >Добавить рейс</v-btn
        >
        <br />
        <v-btn color="#3f57c4bb" class="mb-3 mr-3" @click="$router.push(`/`)"
          >На главную</v-btn
        >
      </v-col>
    </v-row>
  </section>
</template>
 
<script>
import FlightItemCard from "@/components/FlightItemCard.vue";
import PlaceForm from "@/components/PlaceForm";

export default {
  components: { FlightItemCard, PlaceForm },
  name: "Flight",

  data: () => ({
    flightItems: [],
    from: "",
  }),

  methods: {
    submitPlace() {
      localStorage.setItem("from", this.from);
      this.savedPlace = this.from;

      this.$refs.form.reset();
      this.getFlightItems();
    },
    async getFlightItems() {
      try {
        const response = await this.axios.get(
          `http://127.0.0.1:8000/flights/all?from=${this.savedPlace}`
        );

        if (response.status !== 200) {
          throw new Error(response.error);
        }

        const flightItems = response.data.map((flightItem) => {
          let date = new Date(flightItem.departure);

          let year = date.getFullYear();

          let month =
            String(date.getMonth() + 1).length > 1
              ? date.getMonth() + 1
              : `0${date.getMonth() + 1}`;

          let day =
            String(date.getDate()).length > 1
              ? date.getDate()
              : `0${date.getDate()}`;
          let hour =
            String(date.getHours()).length > 1
              ? date.getHours()
              : `0${date.getHours()}`;
          let min =
            String(date.getMinutes()).length > 1
              ? date.getMinutes()
              : `0${date.getMinutes()}`;

          flightItem.departure = `${year}/${month}/${day} ${hour}:${min}`;

          date = new Date(flightItem.arrival);

          year = date.getFullYear();

          month =
            String(date.getMonth() + 1).length > 1
              ? date.getMonth() + 1
              : `0${date.getMonth() + 1}`;

          day =
            String(date.getDate()).length > 1
              ? date.getDate()
              : `0${date.getDate()}`;
          hour =
            String(date.getHours()).length > 1
              ? date.getHours()
              : `0${date.getHours()}`;
          min =
            String(date.getMinutes()).length > 1
              ? date.getMinutes()
              : `0${date.getMinutes()}`;

          flightItem.arrival = `${year}/${month}/${day} ${hour}:${min}`;

          return flightItem;
        });

        this.flightItems = flightItems;
      } catch (e) {
        console.error("AN API ERROR", e);
      }
    },
  },

  created() {
    if (localStorage.getItem("from")) this.from = localStorage.getItem("from");
    this.savedPlace = this.from;
    this.getFlightItems();
  },
};
</script>
 
<style>
</style>
```

```
<template>
  <div class="add">
    <h1 style="margin:20px">Добавить рейс</h1>
    <v-form
      @submit.prevent="FlightCreate"
      ref="addForm"
      class="my-2"
    >
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Самолет"
            v-model="addForm.plane"
            :items="planes"
            item-text="model"
            item-value="id"
            >
          </v-select>
          <v-text-field
            v-model="addForm.number"
            label="Номер"
          ></v-text-field>
          <v-text-field
            v-model="addForm.gate"
            label="Гейт"
          ></v-text-field>
          <v-text-field
            v-model="addForm.wherefrom"
            label="Откуда"
          ></v-text-field>
          <v-text-field
            v-model="addForm.whereto"
            label="Куда"
          ></v-text-field>
          <v-text-field
            v-model="addForm.arrival"
            label="Отлет"
          ></v-text-field>
          <v-text-field
            v-model="addForm.departure"
            label="Прилет"
          ></v-text-field>
          <v-btn color="primary" type="submit">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>


<script>
import PlanesList from '@/components/PlanesList.vue'
import axios from 'axios'

export default {
  name: 'FlightCreate',
  components: {
   PlanesList,
 },
  data: () => ({
    planes: [],
    addForm: {
      number: '',
      departure: '',
      arrival: '',
      whereto:'',
      wherefrom:'',
      gate:'',
      plane: "",
    }
  }),
  async created () {
    this.PlanesList()
  },
  methods: {
      async PlanesList () {
      try {
        const response = await axios
            .get('http://127.0.0.1:8000/planes/all')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.planes = response.data

        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async FlightCreate() {
      try {
        
        const response = await this.axios
          .post('http://127.0.0.1:8000/flights/create/', this.addForm)
        
        console.log(response)
        this.$refs.addForm.reset()
        await this.$router.push('/flight/')
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  }
}
</script>
```

```
<template>
  <div class="add">
    <h1 style="margin: 20px">Редактировать рейс</h1>
    <v-form @submit.prevent="update" ref="addForm" class="my-2">
      <v-row>
        <v-col cols="3" class="mx-auto">
          <v-select
            label="Самолет"
            v-model="addForm.plane"
            :items="planes"
            item-text="model"
            item-value="id"
            return-object
            single-line
          >
          </v-select>
          <v-text-field
            v-model="addForm.number"
            item-text="this.flight_cur.number"
            label="Номер"
          ></v-text-field>
          <v-text-field
            v-model="addForm.gate"
            item-text="this.flight_cur.gate"
            label="Гейт"
          ></v-text-field>
          <v-text-field
            v-model="addForm.wherefrom"
            item-text="this.flight_cur.wherefrom"
            label="Откуда"
          ></v-text-field>
          <v-text-field
            v-model="addForm.whereto"
            item-text="this.flight_cur.whereto"
            label="Куда"
          ></v-text-field>
          <v-text-field
            v-model="addForm.arrival"
            item-text="this.flight_cur.arrival"
            label="Отлет"
          ></v-text-field>
          <v-text-field
            v-model="addForm.departure"
            item-text="this.flight_cur.departure"
            label="Прилет"
          ></v-text-field>
          <v-btn color="accent" type="submit" class="mb-6 mr-3">ОК</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FlightUpd",
  data: () => ({
    flight_id: 0,
    flight_cur: {
      number: "",
      departure: "",
      arrival: "",
      whereto: "",
      wherefrom: "",
      gate: "",
      plane: "",
    },
    addForm: {
      number: "",
      departure: "",
      arrival: "",
      whereto: "",
      wherefrom: "",
      gate: "",
      plane: "",
    },
  }),
  created() {
    this.PlanesList();
    this.flight_id = this.$route.params.flight_id;
    this.axios
      .get(`http://127.0.0.1:8000/flights/${this.flight_id}/`)
      .then((res) => {
        console.log(res);
        this.flight_cur = res.data;
        this.addForm.number = this.flight_cur.number;
        this.addForm.departure = this.flight_cur.departure;
        this.addForm.arrival = this.flight_cur.arrival;
        this.addForm.whereto = this.flight_cur.whereto;
        this.addForm.wherefrom = this.flight_cur.wherefrom;
        this.addForm.gate = this.flight_cur.gate;
        this.addForm.plane = this.flight_cur.plane;
        console.log(this.flight_cur);
      });
  },
  methods: {
    async PlanesList() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/planes/all");
        if (response.status !== 200) {
          throw new Error(response.status);
        }
        this.planes = response.data;

        return response.data;
      } catch (e) {
        console.error("AN API ERROR", e);
      }
    },
    async update() {
      await this.axios
        .put(`http://127.0.0.1:8000/flights/${this.flight_id}/`, this.addForm)
        .then((res) => {
          console.log(res);
          this.$refs.addForm.reset();
          this.$router.push("/flight/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
```