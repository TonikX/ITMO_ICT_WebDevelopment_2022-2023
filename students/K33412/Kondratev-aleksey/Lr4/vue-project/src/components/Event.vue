<template>
	<main class="container-fluid background-main">
		<section class="pt-5 pb-5 row row-cols-2 justify-content-center">
			<div class="d-flex flex-column">
				<div class="pb-5">
					<h1 class="h2 p-0 mb-4 text-color">Кто создал мероприятие</h1>
					<p class="p-0 m-0 text-color">Дата создания</p>
				</div>
				<div class="">
					<h2 class="text-color">Сведения о мероприятие</h2>
					<p class="text-color">Информация</p>
				</div>
				<div class="pt-5">
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
						Записаться
					</button>
					<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									<h3 class="modal-title" id="exampleModalLabel">Вы записаны</h3>
									<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
								</div>
								<div class="modal-body">
									Ждем вас на нашем мероприятие с хорошим настроением
								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<img class="w-25 text-color" src="../assets/image/event.png" alt="Ваше изображение">
		</section>
	</main>
</template>

<script>
export default {
	name: 'EventBlock'
}
</script>
