class HotelsApi {
    constructor(instance) {
        this.API = instance
    }

    getAll = async () => {
        return this.API({
            method: 'GET',
            url: '/hotel/'
        })
    }
}

export default HotelsApi
