<template>
  <section>
    <footer>
      <div class="bg-dark text-white">
        <div class="container pt-5 pb-3">
          <div class="row">
            <div class="col-12 col-xl-6 col-md-12 mb-3">
              <form>
                <p>Подписка на новостную рассылку</p>
                <div class="d-flex flex-column flex-sm-row w-100 gap-2">
                  <label for="newsletter1" class="visually-hidden">Enter your email</label>
                  <input id="newsletter1" type="text" class="form-control" placeholder="Enter your email">
                </div>
              </form>
            </div>
            <div class="col-12 col-xl-6 col-md-12 mb-3">
              <div class="row">
                <div class="d-flex justify-content-end">
                    <ul class="nav flex-column ms-5">
                      <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">О компании</a></li>
                      <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Правовая информация</a></li>
                      <li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-white">Помощь</a></li>
                    </ul>
                    <ul class="nav flex-column ms-5">
                      <li class="nav-item mb-2">
                        <a href="#" class="nav-link p-0 text-white">
                          <svg display="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                            <symbol id="contacts" viewBox="0 0 16 16">
                              <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-5 6s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zM11 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zm.5 2.5a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4zm2 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2zm0 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2z"/>
                            </symbol>
                          </svg>

                          <svg class="icon">
                            <use xlink:href="#contacts"></use>
                          </svg>
                          Контакты
                        </a>
                      </li>
                      <li class="nav-item mb-2">
                        <a href="#" class="nav-link p-0 text-white">
                          <svg display="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                            <symbol id="map" viewBox="0 0 16 16">
                              <path fill-rule="evenodd" d="M15.817.113A.5.5 0 0 1 16 .5v14a.5.5 0 0 1-.402.49l-5 1a.502.502 0 0 1-.196 0L5.5 15.01l-4.902.98A.5.5 0 0 1 0 15.5v-14a.5.5 0 0 1 .402-.49l5-1a.5.5 0 0 1 .196 0L10.5.99l4.902-.98a.5.5 0 0 1 .415.103zM10 1.91l-4-.8v12.98l4 .8V1.91zm1 12.98 4-.8V1.11l-4 .8v12.98zm-6-.8V1.11l-4 .8v12.98l4-.8z"/>
                            </symbol>
                          </svg>

                          <svg class="icon">
                            <use xlink:href="#map"></use>
                          </svg>
                          Найти нас
                        </a>
                      </li>
                    </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-end">
            <p>ⓒ 2022 Meetings</p>
          </div>
        </div>
      </div>
    </footer>
  </section>
</template>

<script>
  export default {
    name: "footer"
  }
</script>

<style scoped>
  .icon {
    width: 20px;
    height: 20px;
    fill: currentColor;
  }
</style>