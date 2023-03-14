class ChartsAPI {
    constructor(instance) {
        this.API = instance
    }

    getCharts = async () => {
        return this.API({
            url: '/charts'
        })
    }
}

export default ChartsAPI