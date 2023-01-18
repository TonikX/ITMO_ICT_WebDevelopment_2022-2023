class GameSystemsAPI {
    constructor(instance) {
        this.API = instance
    }

    getAllGameSystems = async () => {
        return this.API({
            method: 'GET',
            url: 'scenarios/game_systems'
        })
    }
}

export default GameSystemsAPI
