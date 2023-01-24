class CoinsAPI {
    constructor(instance) {
        this.API = instance
    }

    getCoins = async (search, sort, order, page, limit) => {
        return this.API({
            url: `/coins?q=${search}&_sort=${sort}&_order=${order}&_limit=${limit}&_page=${page}`
        })
    }

    getCustomList = async () => {
        return this.API({
            url: `/coins`
        })
    }
}

export default CoinsAPI