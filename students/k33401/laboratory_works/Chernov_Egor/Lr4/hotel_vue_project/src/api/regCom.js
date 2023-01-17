class RegComApi {
    constructor(instance) {
        this.API = instance
    }

    getComments = async () => {
        return this.API({
            method: 'GET',
            url: "/act/com/"
        })
    }
}

export default RegComApi
