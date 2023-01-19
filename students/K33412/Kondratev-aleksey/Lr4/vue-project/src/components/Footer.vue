<template>
	<footer class="container-fluid pt-5 colors">
		<div class="row justify-content-between p-2">
			<div class="col-2 text-color">
				<h3>Ваш аккаунт</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="./personal-area.html" class="nav-link p-0 text-color">Личный кабинет</a></li>
					<li class="nav-item mb-2"><a href="./entry.html" class="nav-link p-0 text-color">Вход</a></li>
					<li class="nav-item mb-2"><a href="./reqistration.html" class="nav-link p-0 text-color">Регистрация</a></li>
				</ul>
			</div>

			<div class="col-2 text-color">
				<h3>Найти</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="./calendar.html" class="nav-link p-0 text-color">Календарь</a></li>
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">Поиск мероприятий</a></li>
				</ul>
			</div>

			<div class="col-2 text-color">
				<h3>О нас</h3>
				<ul class="nav flex-column">
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">ВКонтакте</a></li>
					<li class="nav-item mb-2"><a href="#" class="nav-link p-0 text-color">Телеграм</a></li>
				</ul>
			</div>

			<div class="col-4 offset-1">
				<form>
					<h3 class="text-color">Подпишись на нас, чтобы не пропустить ничего интересного</h3>
					<div class="d-flex w-100 gap-2">
						<label for="newsletter1" class="visually-hidden">Ваша почта</label>
						<input id="newsletter1" type="text" class="form-control" placeholder="example@email.com">
						<button class="btn btn-primary" type="button">Подписаться</button>
					</div>
				</form>
			</div>
		</div>

		<div class="d-flex justify-content-between py-4 my-4 mb-0 border-top text-color">
			<p>&copy 2022, Кондратьев Алексей</p>
		</div>
	</footer>
</template>

<script>
export default{
	name: 'FooterBlock',
}

</script>
