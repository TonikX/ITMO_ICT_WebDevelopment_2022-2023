## Описание работы
Создать программную систему, предназначенную для администратора гостиницы. 
С преподавателем по дисциплине "Web-программирование" утвердили список интерфейсов для взаимодействия с серверной частью:

1. Интерфейс просмотра доступных комнат

2. Интерфейс просмотра одной комнаты + просмотра истории бронирования комнаты + кнопка "заселить" и тд

3. Интерфейс создания гостя + список гостей + просмотр гостя и его бронирований и возможность выселить гостя (либо выселить можно через интерфейс списка комнат)

4. Список уборок + создание уборки

## Основные файлы с кодом 

* `AboutRooms.vue` - интерфейс просмотра доступных комнат
```vue
<template>
  <div class="mb-5">
    <h1 class="has-text-centered">This is page about available rooms</h1>
  </div>
  <div class="container">
    <div class="columns is-multiline">
      
      <RoomList v-for="room in rooms" :key="room.id" :room="room" class="column is-one-third"/>
    
    </div>
  </div>
</template>

<script>
import RoomList from '@/components/RoomList.vue';
import axios from 'axios'

export default {
  name: "Rooms",
  data() {
    return {
      rooms: []
    }
  },
  mounted() {
    this.getRooms()
  },
  components: {RoomList},
  methods: {
    async getRooms() {
      axios
        .get('/hotel/rooms/')
        .then(response => {
            this.rooms = response.data
        })
        .catch(error => {
            console.log(error)
        })
    }
  }
}
</script>
```

* `AboutRooms.vue` - интерфейс просмотра гостя + просмотра бронирования комнаты

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ guest.first_name }} {{ guest.last_name }}</h1>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>
                    <p><strong>First Name: </strong>{{ guest.first_name }}</p>
                    <p><strong>Last Name: </strong>{{ guest.last_name }}</p>
                    <p><strong>City: </strong>{{ guest.city }}</p>
                    <p><strong>Passport: </strong>{{ guest.passport }}</p>
                    <div class="buttons mt-4">
                        <router-link v-if="typeof guest.id !== 'undefined'" 
                        :to="{ name: 'EditGuest', params: { id: guest.id }}" class="button is-light">Edit guest</router-link>
                    </div>
                </div>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Room book</h2>

                    <p><strong>Reserved room: </strong>{{ guest.room_book }}</p>
                    <p><strong>Check in: </strong>{{ booking.check_in }}</p>
                    <p><strong>Check out: </strong>{{ booking.check_out }}</p>
                    <div class="buttons mt-4">
                        <router-link v-if="typeof guest.id !== 'undefined'" 
                        :to="{ name: 'EditBook', params: { id: guest.id }}" class="button is-light">Edit booking</router-link>
                    </div>
                </div>
            </div>
            <!-- когда сделаешь букинги добавь в mounted getBook, дальше получи get данные о бронировании -->
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Guest',
        data() {
            return {
                guest: {},
                booking: {}
            }
        },
        mounted() {
            this.getGuest()
        },
        methods: {
            async getGuest() {
                this.$store.commit('setIsLoading', true)
                const guestID = this.$route.params.id
                await axios
                    .get(`/hotel/guests/${guestID}/`)
                    .then(response => {
                        this.guest = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                await axios
                    .get(`/hotel/bookings/${guestID}/`)
                    .then(response => {
                        this.booking = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>
``` 

* `AddGuest.vue` - интерфейс создания гостя 

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add guest</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="last_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Passport</label>
                        <div class="control">
                            <input type="text" class="input" v-model="passport">
                        </div>
                    </div>

                    <div class="field">
                        <label>City</label>
                        <div class="control">
                            <input type="text" class="input" v-model="city">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'AddGuest',
        data() {
            return {
                first_name: '',
                last_name: '',
                passport: '',
                city: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const guest = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    passport: this.passport,
                    city: this.city
                }
                await axios
                    .post('/hotel/guests/create/', guest)
                    .then(response => {
                        toast({
                            message: 'The guest was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/guests')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
```

* `Guests.vue` - список гостей 

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Guests</h1>

                <router-link to="/guests/create">Add guest</router-link>
                
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Passport</th>
                            <th>City</th>
                            <th>Reserved room</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="guest in guests"
                            v-bind:key="guest.id">
                                <td>{{ guest.first_name }}</td>
                                <td>{{ guest.last_name }}</td>
                                <td>{{ guest.passport }}</td>
                                <td>{{ guest.city }}</td>
                                <td>{{ guest.room_book }}</td>
                                <td>
                                    <router-link :to="{ name: 'Guest', params: { id: guest.id }}">Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Guest',
        data() {
            return {
                guests: []
            }
        },
        mounted() {
            this.getGuests()
        },
        methods: {
            async getGuests() {
                axios
                    .get('/hotel/guests/')
                    .then(response => {
                        this.guests = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>
```

* `EditBook.vue` - возможность выселить гостя

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit booking</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Room</label>
                        <div class="control">
                            <input type="text" class="input" v-model="booking.room">
                        </div>
                    </div>

                    <div class="field">
                        <label>Check in</label>
                        <div class="control">
                            <input type="date" class="input" v-model="booking.check_in">
                        </div>
                    </div>

                    <div class="field">
                        <label>Check out</label>
                        <div class="control">
                            <input type="date" class="input" v-model="booking.check_out">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'EditBook',
        data() {
            return {
                booking: {}
            }
        },
        mounted() {
            this.getBooking()
        },
        methods: {
            async getBooking() {
                this.$store.commit('setIsLoading', true)
                const bookingID = this.$route.params.id
                await axios
                    .get(`/hotel/bookings/${bookingID}/`)
                    .then(response => {
                        this.booking = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                this.$store.commit('setIsLoading', false)
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)
                const bookingID = this.$route.params.id
                await axios
                    .patch(`/hotel/bookings/update/${bookingID}/`, this.booking)
                    .then(response => {
                        toast({
                            message: 'The booking was updated',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push(`/guests/${bookingID}`)
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
        }
    }
</script>
```

* `Cleaners.vue` - cписок уборок 

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cleanings</h1>

                <router-link to="/cleanings/create">Add cleaning</router-link>
                
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Clean room</th>
                            <th>Cleaner</th>
                            <th>Date time</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="cleaning in cleanings"
                            v-bind:key="cleaning.id">
                                <td>{{ cleaning.clean_room }}</td>
                                <td>{{ cleaning.cleaner_id }}</td>
                                <td>{{ cleaning.date_time }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Cleaning',
        data() {
            return {
                cleanings: []
            }
        },
        mounted() {
            this.getCleanings()
        },
        methods: {
            async getCleanings() {
                axios
                    .get('/hotel/cleanings/')
                    .then(response => {
                        this.cleanings = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>
```

* `AddCleaning.vue` - создание уборки

```vue
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add cleaning</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Room</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="clean_room">
                                
                                <option v-for="clean_room in rooms" :value="clean_room.id"
                                >{{ clean_room.id }}
                                </option>
                                   
                            </select>
                        </div>
                    </div>

                    <div class="field">
                        <label>Cleaner</label>
                        <br>
                        <div class="select is-primary">
                            <select v-model="cleaner_id">
                                <option v-for="cleaner_id in cleaners"
                                    :value="cleaner_id.cleaner_id">
                                    {{ cleaner_id.cleaner_id }} 
                                </option>
                            </select>
                        </div>
                        
                    </div>

                    <div class="field">
                        <label>Date</label>
                        <div class="control">
                            <input type="date" class="input" v-model="date_time">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    export default {
        name: 'AddCleaning',
        data() {
            return {
                
                cleaner_id: '',
                clean_room: '',
                date_time: '',
                cleaners: [],
                rooms: []
            }
        },
        mounted() {
            this.getCleaners(),
            this.getRooms()
        },
        methods: {
            async getCleaners() {
                await axios
                    .get('/hotel/cleaners/')
                    .then(response => {
                        this.cleaners = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async getRooms() {
                await axios
                    .get('/hotel/rooms/')
                    .then(response => {
                        this.rooms = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const cleaning = {
                    cleaner_id: this.cleaner_id,
                    clean_room: this.clean_room,
                    date_time: this.date_time,
                }
                
                await axios
                    .post('/hotel/cleanings/create/', cleaning)
                    .then(response => {
                        toast({
                            message: 'The cleaning was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/cleanings')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            
            
        }
    }
</script>
```




