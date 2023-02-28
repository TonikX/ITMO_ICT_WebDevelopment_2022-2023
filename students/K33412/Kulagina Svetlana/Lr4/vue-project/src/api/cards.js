export default class CardsApi {
	constructor (instance) {
		this.API = instance
	}

	getAll = async () => {
		return this.API({
			url: '/notes'
		})
	}
	getById = async (id) => { 
		return this.API({ 
			url: `/notes/${id}` 
		}) 
	}
}