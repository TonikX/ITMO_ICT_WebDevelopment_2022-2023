# Views

## BooksView
``` javascript
<template>
  <section>
    <v-app>
      <bar-layout>
        <DefaultNavigationBar/>
      </bar-layout>

      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
        <v-row class="mx-3.5">
          <v-col cols="4" class="mx-auto">
            <br><br>

            <div>
              <h2>Каталог библиотеки</h2>

              <v-flex d-flex flex-column md-6>
                <v-flex v-for="book in books" :key="book.id">
                  <v-card-text
                    elevation="2"
                    outlined
                    class="my-2"
                  >
                    <p>Название: {{ book.title }} </p>
                    <p>Автор: {{ book.author }} </p>
                    <p>Издательство: {{ book.publisher }}</p>
                    <p>Год издания: {{ book.year_of_publishing }}</p>

                    <v-col cols="3">
                      <v-btn variant="text" color="blue" light @click.prevent="goBook(book.id)">Подробнее</v-btn>
                    </v-col>
                  </v-card-text>
                </v-flex>
              </v-flex>
            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'BooksView',
  data() { return { books: Object } },
  created() { this.loadBooks() },
  components: {BarLayout, DefaultNavigationBar},
  methods: {
    async loadBooks() {
      const response = await axios.get('http://127.0.0.1:8000/library/books/all')
      this.books = response.data
    },
    goBook(bookID) {
      this.$router.push({name: 'Book', params: {id: bookID}})
    },
  }
}
</script>

```

## BookView
``` jsvascript
<template>
  <section>
    <v-app>
      <bar-layout>
        <DefaultNavigationBar/>
      </bar-layout>

      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
        <v-row class="mx-3.5">
          <v-col cols="5" class="mx-auto">
            <br><br>
            <div>
              <v-card
                elevation="2"
                outlined
                class="my-5"
              >
                <v-card-title>
                  <h2>{{ this.book.title }}</h2>
                </v-card-title>

                <v-card-text>
                  <div class="text--primary">
                    <b>Автор:</b> {{ this.book.author }}<br>
                    <b>Год издания:</b> {{ this.book.year_of_publishing }} <br>
                    <b>Издательство:</b> {{ this.book.publisher }} <br>
                    <ul>
                      <li v-for="hall in this.book.book_hall" v-bind:key="hall" v-bind:hall="hall">
                        {{ hall.title }}
                      </li>
                    </ul>
                  </div>
                </v-card-text>
              </v-card>

              <v-btn
                v-if="(!this.is_book_on_hold && this.book_instances.length > 0)"
                color="primary"
                light @click="takeBook">Взять книгу
              </v-btn>

              <a v-if="!this.is_book_on_hold && this.book_instances.length == 0">
                К сожалению, свободных экземпляров книги нет
              </a>

              <v-card
                v-if="this.is_book_on_hold"
                elevation="2"
                outlined
                class="my-2"
              >
                <v-card-text>
                  <div class="text--primary">Вы сейчас читаете эту книгу</div>
                </v-card-text>
                <v-spacer></v-spacer>
                <v-btn block color="red" light @click="returnBook">Вернуть книгу в библиотеку</v-btn>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
</template>


<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'BookView',
  data() {
    return {
      book: Object,
      user_book_instance: Object,
      book_instances: Object,
      reader: Object,
      is_book_on_hold: false,
      bookReaderID: ''
    }
  },
  created() {
    this.loadBook()
    this.loadReader()
  },
  components: {BarLayout, DefaultNavigationBar},

  methods: {
    async loadBook() {
      this.book_url = 'http://127.0.0.1:8000/library/books/' + this.$route.params.id
      const response = await axios.get(this.book_url)
      this.book = response.data

      this.loadBookInstances()
    },

    async loadBookInstances() {
      const get_book_instances_request_url = 'http://127.0.0.1:8000/library/book_instances/free/by_book_id/' + this.book.id
      const get_book_instances_response = await axios.get(get_book_instances_request_url)

      this.book_instances = get_book_instances_response.data
    },

    async loadReader() {
      const get_user_response_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: { Authorization: `Token ${localStorage.auth_token}` }
        })
      const user = get_user_response_response.data
      const get_userreader_request_url = "http://127.0.0.1:8000/library/userreaders/" + user.id
      const get_userreader_response = await axios.get(get_userreader_request_url)
      const userreader = get_userreader_response.data
      const get_reader_request_url = "http://127.0.0.1:8000/library/readers/" + userreader.reader
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data

      this.reader = reader

      await this.checkIsOnHold()
    },

    async checkIsOnHold() {
      const get_reader_books_url = 'http://127.0.0.1:8000/library/readerbooks/by_reader/' + this.reader.ticket
      const get_reader_books_response = await axios.get(get_reader_books_url)
      const readers_book = get_reader_books_response.data

      // eslint-disable-next-line no-unused-vars
      for (const [key, value] of Object.entries(readers_book)) {
        if (value.book_instance.book.id === this.book.id) {
          this.is_book_on_hold = true
          this.user_book_instance = value.book_instance
          break
        }
      }
    },

    async takeBook() {
      const free_book_instance = this.book_instances[Math.floor(Math.random()*this.book_instances.length)]
      await axios.post(
        'http://127.0.0.1:8000/library/readerbooks/create/',
        {
          reader: this.reader.ticket,
          book_instance: free_book_instance.id
        }
      )

      this.$router.push({name: 'Reader'})
    },

    async returnBook() {
      const delete_reader_book_request_url = "http://127.0.0.1:8000/library/readerbooks/by_instance/" + this.user_book_instance.id

      await axios.delete(delete_reader_book_request_url)

      this.$router.push({name: 'Books'})
    },
  }
}
</script>

```

## EditReaderView
``` jsvascript
<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <DefaultNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Информация о читателе </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер телефона"
                v-model="form.phone_number"
                name="phone_number"
                placeholder="+79516571701"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Адрес"
                v-model="form.address"
                name="address"
                placeholder="Russia, Saint-Petersburg, Bolshaya Moskovskaya 1-3"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-select
                v-model="form.education"
                :items="educationOptions"
                label="Образование"
                name="education"
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="4" class="mx-auto"></v-col>
            <v-checkbox
              v-model="form.is_has_academic_degree"
              name="is_has_academic_degree"
              :label="'Наличие учёной степени'"
            ></v-checkbox>
          </v-row>

          <v-col cols="5" class="mx-auto">
            <v-btn block color="blue" @click.prevent="saveChanges()"> Обновить</v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
      <br><br>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'EditReaderView',
  components: {BarLayout, DefaultNavigationBar},
  data: () => ({
    reader_old: Object,
    form: {
      phone_number: '',
      address: '',
      education: '',
      is_has_academic_degree: ''
    },
    educationOptions: ['primary', 'secondary', 'higher']
  }),
  created() {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData() {
      const get_user_response_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {Authorization: `Token ${localStorage.auth_token}`}
        })
      const user = get_user_response_response.data
      const get_userreader_request_url = "http://127.0.0.1:8000/library/userreaders/" + user.id
      const get_userreader_response = await axios.get(get_userreader_request_url)
      const userreader = get_userreader_response.data
      const get_reader_request_url = "http://127.0.0.1:8000/library/readers/" + userreader.reader
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data

      this.reader_old = reader
      this.form.phone_number = reader.phone_number
      this.form.address = reader.address
      this.form.education = reader.education
      this.form.is_has_academic_degree = reader.is_has_academic_degree
    },

    async saveChanges() {
      try {
        const patch_reader_request_url = "http://127.0.0.1:8000/library/readers/" + this.reader_old.ticket

        await axios.patch(patch_reader_request_url, this.form)
        await this.$router.push({name: 'Reader'})
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.is_has_academic_degree) {
          alert('Учёная степень: ' + e.response.data.is_has_academic_degree)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          alert(e.message)
        }
      }
    }
  }
}
</script>

```

## FinishCompleteInfoView
``` jsvascript
<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <RegistrationNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Информация о читателе </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер читательского билета"
                v-model="form.ticket"
                name="ticket"
                placeholder="12345"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Серия и номер паспорта"
                v-model="form.passport_number"
                name="passport_number"
                placeholder="12345678910"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Дата рождения"
                v-model="form.birth_date"
                name="birth_date"
                placeholder="2002-07-31"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Номер телефона"
                v-model="form.phone_number"
                name="phone_number"
                placeholder="+79516571701"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Адрес"
                v-model="form.address"
                name="address"
                placeholder="Russia, Saint-Petersburg, Bolshaya Moskovskaya 1-3"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-select
                v-model="form.education"
                :items="educationOptions"
                label="Образование"
                name="education"
              ></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="4" class="mx-auto"></v-col>
            <v-checkbox
              v-model="form.is_has_academic_degree"
              name="is_has_academic_degree"
              :label="'Наличие учёной степени'"
            ></v-checkbox>
          </v-row>

          <v-col cols="5" class="mx-auto">
            <v-btn block color="blue" @click.prevent="finish()"> Завершить</v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
      <br><br>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationNavigationBar from '@/components/RegistrationNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'FinishCompleteInfoView',
  components: {BarLayout, RegistrationNavigationBar},
  data: () => ({
    form: {
      ticket: '',
      name: '',
      passport_number: '',
      birth_date: '',
      phone_number: '',
      address: '',
      education: '',
      is_has_academic_degree: ''
    },
    educationOptions: ['primary', 'secondary', 'higher']
  }),
  methods: {
    async finish() {
      try {
        const user_response = await axios.get(
          'http://127.0.0.1:8000/auth/users/me/',
          {
            headers: {Authorization: `Token ${localStorage.auth_token}`}
          }
        )
        const user = user_response.data

        this.form.name = user.first_name + user.last_name
        this.form.education = this.form.education[0]

        const reader_create_response = await axios.post('http://127.0.0.1:8000/library/readers/create', this.form)
        const reader = reader_create_response.data

        await axios.post(
          'http://127.0.0.1:8000/library/userreaders/create',
          {user: user.id, reader: reader.ticket}
        )

        window.location = '/home'

        this.$router.push({name: 'Home'})
      } catch (e) {
        console.log(e)
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.ticket) {
          alert('Номер билета: ' + e.response.data.ticket)
        } else if (e.response.data.birth_date) {
          alert('Дата рождения: ' + e.response.data.birth_date)
        } else if (e.response.data.education) {
          alert('Образование: ' + e.response.data.education)
        } else if (e.response.data.is_has_academic_degree) {
          alert('Учёная степень: ' + e.response.data.is_has_academic_degree)
        } else if (e.response.data.passport_number) {
          alert('Паспортные данные: ' + e.response.data.passport_number)
        } else if (e.response.data.address) {
          alert('Адрес: ' + e.response.data.address)
        } else if (e.response.data.phone_number) {
          alert('Телефон: ' + e.response.data.phone_number)
        } else {
          alert(e.error.message)
        }
      }
    }
  }
}
</script>

```

## HomeView
``` jsvascript
<template>
  <v-app>
    <bar-layout>
      <DefaultNavigationBar/>
    </bar-layout>
    <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <v-col cols="8" class="mx-auto">
        <br><br><br><br>

        <h1>Домашняя страница</h1>

        <br>

        <span>Возможности сайта:</span>

        <p>
          <br> 1. Редактирование личной информации
          <br> 2. Просмотр всех книг
          <br> 3. Бронирвоание/возврат книги
        </p>
      </v-col>
    </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'

export default {
  name: 'HomeView',
  components: {BarLayout, DefaultNavigationBar}
}
</script>

```

## LoginView
``` jsvascript
<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <LoginNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Вход </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Логин"
                v-model="this.username"
                name="first_name"
                placeholder="SuperDeveloper3000"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="this.password"
                name="password"
                type=password
              />
            </v-col>
          </v-row>

          <v-col cols="7" class="mx-auto">
            <v-btn block color="blue" @click.prevent="login()"> Войти </v-btn>
          </v-col>

          <br>
        </v-card>
      </v-col>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import LoginNavigationBar from '@/components/LoginNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'LoginView',
  components: { BarLayout, LoginNavigationBar },
  data() { return { username: '', password: '' } },
  methods: {
    async login() {
      const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
        { username: this.username, password: this.password, }
      )

      if (response.data.auth_token) {
        localStorage.auth_token = response.data.auth_token
        window.location = '/home'
      }
    }
  }
}
</script>

```

## ReaderInfoView
``` jsvascript
<template>
  <v-app>
    <bar-layout>
      <DefaultNavigationBar/>
    </bar-layout>

    <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <v-row class="mx-3.5">
        <v-col cols="5" class="mx-auto">
          <br><br>
          <div>
            <v-card
              elevation="2"
              outlined
              class="my-2"
            >
              <br>
              <v-card-title><h2>Профиль</h2></v-card-title>

              <v-card-text>
                <div class="text--primary">
                  <b>Имя:</b> {{ this.user.first_name }} <br>
                  <b>Фамилия:</b> {{ this.user.last_name }} <br>
                  <b>Логин:</b> {{ this.user.username }} <br>
                  <b>Номер билета:</b> {{ this.reader.ticket }} <br>
                  <b>Дата рождения:</b> {{ this.reader.birth_date }} <br>
                  <b>Образование:</b> {{ this.reader.education }} <br>
                  <b>Ученая степень:</b> {{ this.reader.is_has_academic_degree ? 'да' : 'нет' }} <br>
                  <b>Паспортные данные:</b> {{ this.reader.passport_number }} <br>
                  <b>Адрес:</b> {{ this.reader.address }} <br>
                  <b>Телефон:</b> {{ this.reader.phone_number }} <br>
                  <b>Дата регистрации:</b> {{ this.reader.registration_date }} <br>
                </div>
              </v-card-text>
            </v-card>

            <v-col cols="7" class="mx-auto">
              <v-btn block color="blue" light @click.prevent="goEditReaderInfo">Редактировать профиль</v-btn>
            </v-col>

            <v-card
              elevation="2"
              outlined
              class="my-2"
            >
              <br>
              <v-card-title>
                <h2>
                  {{ reader_book_instances.length > 0 ? "Вы сейчас читаете:" : "У вас на руках нет книг" }}
                </h2>
              </v-card-title>

              <v-flex d-flex flex-column md-6>
                <v-flex v-for="book_instance in reader_book_instances" :key="book_instance.id">
                  <v-card-text
                    elevation="2"
                    outlined
                    class="my-2"
                  >
                    <p>Название: {{ book_instance.book_instance.book.title }} </p>
                    <p>Автор: {{ book_instance.book_instance.book.author }} </p>
                    <p>Дата начала бронирования: {{ book_instance.start_date }} </p>
                    <p>Дата конца бронирования: {{ book_instance.end_date }} </p>

                    <v-col cols="3">
                      <v-btn
                        variant="text"
                        color="blue"
                        light @click.prevent="returnBook(book_instance.book_instance.id)"
                      >
                        Сдать
                      </v-btn>
                    </v-col>

                  </v-card-text>
                </v-flex>
              </v-flex>
            </v-card>
          </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import DefaultNavigationBar from '@/components/DefaultNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'ReaderInfoView',
  components: {BarLayout, DefaultNavigationBar},
  data() {
    return {
      reader_book_instances: Object,
      reader: Object,
      user: Object
    }
  },
  created() {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData() {
      const get_user_response = await axios
        .get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {Authorization: `Token ${localStorage.auth_token}`}
        })
      const user = get_user_response.data
      const get_user_reader_request_url = 'http://127.0.0.1:8000/library/userreaders/' + user.id
      const get_user_reader_response = await axios.get(get_user_reader_request_url)
      const user_reader = get_user_reader_response.data
      const reader_id = user_reader.reader
      const get_reader_request_url = 'http://127.0.0.1:8000/library/readers/' + reader_id
      const get_reader_response = await axios.get(get_reader_request_url)
      const reader = get_reader_response.data
      const get_reader_books_request_url = 'http://127.0.0.1:8000/library/readerbooks/by_reader/' + reader_id
      const get_reader_books_response = await axios.get(get_reader_books_request_url)
      const reader_book_instances = get_reader_books_response.data

      this.reader_book_instances = reader_book_instances
      this.reader = reader
      this.user = user
    },

    async returnBook(book_instance_id) {
      const delete_reader_book_request_url = "http://127.0.0.1:8000/library/readerbooks/by_instance/" + book_instance_id

      await axios.delete(delete_reader_book_request_url)

      this.$router.push({name: 'Books'})
    },
    goEditReaderInfo() {
      this.$router.push({name: 'EditReader'})
    }
  }
}
</script>

```

## RegistrationView
``` jsvascript
<template>
  <v-app style="background-color: hsl(0, 0%, 96%);">
    <bar-layout>
      <RegistrationNavigationBar/>
    </bar-layout>

    <main>
      <br><br><br><br><br>
      <h1 style="text-align: center;"> Регистрация </h1>
      <br>

      <v-col cols="4" class="mx-auto">

        <v-card max-width=700 color="#f7f4ef">
          <br><br>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Имя"
                v-model="form.first_name"
                name="first_name"
                placeholder="Ilia"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Фамилия"
                v-model="form.last_name"
                name="last_name"
                placeholder="Chub"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Логин"
                v-model="form.username"
                name="first_name"
                placeholder="SuperDeveloper3000"
              />
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="8" class="mx-auto">
              <v-text-field
                label="Password"
                v-model="form.password"
                name="password"
                type=password
              />
            </v-col>
          </v-row>

          <v-col cols="7" class="mx-auto">
            <v-btn block color="blue" @click.prevent="register()"> Зарегистрироваться </v-btn>
          </v-col>
          <br>
        </v-card>
      </v-col>
    </main>
  </v-app>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import RegistrationNavigationBar from '@/components/RegistrationNavigationBar.vue'
import axios from 'axios'

export default {
  name: 'RegistrationView',
  components: {BarLayout, RegistrationNavigationBar},
  data: () => ({
    form: {
      first_name: '',
      last_name: '',
      username: '',
      password: ''
    },
  }),
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/auth/users/', this.form)

        const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
          {
            username: this.form.username,
            password: this.form.password,
          })

        if (response.data.auth_token) {
          localStorage.auth_token = response.data.auth_token
          window.location = '/finish_complete_info'
        }

        this.$router.push({ name: 'FinishCompleteInfoView' })
      } catch (e) {
        if (e.response.data.non_field_errors) {
          alert(e.response.data.non_field_errors)
        } else if (e.response.data.username) {
          alert('Логин: ' + e.response.data.username)
        } else if (e.response.data.password) {
          alert('Пароль: ' + e.response.data.password)
        } else if (e.response.data.first_name) {
          alert('Имя: ' + e.response.data.first_name)
        } else if (e.response.data.last_name) {
          alert('Фамилия: ' + e.response.data.last_name)
        } else {
          alert(e.error.message)
        }
      }
    }
  }
}
</script>

```
