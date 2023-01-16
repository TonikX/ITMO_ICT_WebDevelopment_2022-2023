class CLientApi {
    constructor(instance) {
        this.API = instance
    }

    getAllClients = async () => {
        return this.API({
            url: '/api/all_clients/'
        })
    }

}

export default CLientApi
