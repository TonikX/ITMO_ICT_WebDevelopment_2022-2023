<template>
	<main class="row mx-auto d-flex pt-5 color-main pb-5">
		<section class="note container row mx-auto" data-event-id="1">
		<h1 class="help mb-5 mero text-card" name="mero">Мюзик Холл</h1>
			<div class="row d-flex col-md-3 col-lg-2 col-sm-3 col-4 col-xl-2 col-2">
					<h2 class="information h5 text-card">Адрес:</h2>
					<h2 class="information mt-5 h5 text-card">Рйон:</h2>
					<h2 class="information mt-5 h5 text-card">Метро:</h2>
					<h2 class="information mt-5 h5 text-card">Дата:</h2>
					<h2 class="information mt-5 h5 text-card">Сайт:</h2>
					<h2 class="information mt-5 h5 text-card">Часы работы:</h2>
			</div>
			<div class=" row d-flex col-md-9 col-lg-6 col-sm-9 col-9 col-xl-5">
					<h2 class="text address h5 text-card" name="address">Парк Александровский, д. 4</h2>
					<h2 class="text mt-5 h5 text-card">Петроградский район</h2>
					<h2 class="text mt-5 h5 metro text-card" name="metro">Горьковская (409 м)</h2>
					<h2 class="text mt-5 h5 data text-card" name="data">01.12.2022</h2>
					<h2 class="text mt-5 h5 text-card"><a href="http://www.musichallspb.ru">http://www.musichallspb.ru</a></h2>
					<h2 class="text mt-5 h5 text-card">кассы: пн-вс: с 12:00 до 19:15</h2>
			</div>
			<div class="row d-flex justify-content-lg-center col-md-12 col-lg-12 col-xl-5">
				<img src="../assets/image/музик холл1.jpg" class="musicimg" alt="..." width="431">
				<div class="container d-flex justify-center-between">
				<img src="../assets/image/мх1 (1)_0.jpg" class="musicimg" style="width: 25%" alt="..." width="101.75">
				<img src="../assets/image/мх2 (3)_0.jpg" class="musicimg" style="width: 25%" alt="..." width="101.75">
				<img src="../assets/image/мх3 (5).jpg" class="musicimg" style="width: 25%" alt="..." width="101.75">
				<img src="../assets/image/мх4.jpg" class="musicimg" style="width: 25%" alt="..." width="101.75">
				</div>
			</div>
		</section>
		<section class="container row mx-auto pt-5">
		<h3 class="colored-h3 text-card">Пойдешь с нами?)</h3>
			<form onsubmit="addNote()">
				<div class="pt-3">
					<button type="submit" class="btn btn-light button-color">Записаться</button>
				</div>
			</form>
		</section>
		<section class="container row mx-auto pt-5">
			<div class="container">
				<div class="accordion" id="accordionExample">
					<div class="accordion-item">
						<h2 class="accordion-header" id="headingOne">
							<button class="accordion-button card-color text-card" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
								Описание
							</button>
						</h2>
						<div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
							<div class="accordion-body card-color text-card">
								<p>Санкт-Петербургский Мюзик-холл - уникальный театр по своей жанровой природе и сегодня единственный в России. Украшение всех постановок коллектива - балетная труппа. Каждый новый спектакль - это всегда совершенно оригинальное произведение,в котором использованы хореография, вокал, оригинальные номера самого высокого класса и все это - единый и ни на что не похожий сплав искусств, созданный с оригинальным образным решением в сочетании великолепных красок, костюмов, декораций и световых решений.</p>
								<p>Создал театр народный артист России И.Рахлин - известный режиссер театра и эстрады. Сегодня репертуар театра необычайно широк и богат - от ревю, шоу до мюзикла и даже оперы.</p>
								<p>Каждые пятницу, субботу и воскресенье новая площадка Мюзик-Холла, театр-бар "Синий БАРхат" представляет спектакли в жанре кабаре, варьете и мюзикла. "Синий БАРхат" - уютное двухэтажное пространство, где объединены сценическая площадка и театральный буфет.</p>
							</div>
						</div>
					</div>
					<div class="accordion-item">
						<h2 class="accordion-header" id="headingTwo">
							<button class="accordion-button collapsed card-color text-card" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
								Отзывы
							</button>
						</h2>
						<div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
							<div class="accordion-body card-color text-card">
								<strong>Оценка: 4/10</strong>
								<p>7 января 2020 г. 20:22</p>
								<p>Насчёт обслуживания : не знаю кто виноват в том, что покупая билеты на ряд перед проходом, рассчитывая что переплатил за билеты и получил хорошие места, в итоге перед тобой оказывается ещё один ряд. Удивительно. Весь спектакль перед нами вставали и садились люди, удтверждая, что они из руководства. Отвратительное отношение к зрителю , купившему билет. Интерьер бедноватый. Ремонта видимо не было давно. Обшарпанные стены и разломанные музыкальные инструменты в вестибюле.Добираться удобно. От метро в шаговой доступности.Мюзикл «Сказ о серебряных крыльях» очень понравился, детям было интересно.Волк в исполнении Андрея Гульнева просто очаровал.</p>
								<strong>Оценка: 8/10</strong>
								<p>3 сентября 2018 г. 20:02</p>
								<p>Обслуживание как обслуживание: ничего особенного.</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section> 
	</main>
</template>

<script>
export default {
	name: 'MusBlock'
}
</script>