export function getError(error) {
	console.log(error);

	let e = error.response?.data;
	if (typeof e === "string")
		return e;
	else if (typeof e === "object")
		return JSON.stringify(e)
	else
		return "Неизвестная ошибка"
}

export function getSpecializationName(specialization) {
	let name = specialization.name;
	if(specialization.level_name)
		name += ` (${specialization.level_name})`;
	return name;
}
