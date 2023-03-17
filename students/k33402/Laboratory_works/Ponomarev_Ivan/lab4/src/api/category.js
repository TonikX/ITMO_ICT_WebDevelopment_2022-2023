class categoriesApi{
    constructor(instance) {
        this.API = instance
    }

    getCategories = async () => {
        return this.API({
            url:`/api/categories/all`,
            method: 'GET'
        })
    }
}
export default categoriesApi