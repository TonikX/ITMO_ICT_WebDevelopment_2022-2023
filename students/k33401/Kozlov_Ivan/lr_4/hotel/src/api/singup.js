class SingupApi {
    constructor(instance) {
        this.API = instance
    }

    getAll = async () => {
        return this.API({
            url: '/api/all_rooms/'
        })
    }
}

export default SingupApi
