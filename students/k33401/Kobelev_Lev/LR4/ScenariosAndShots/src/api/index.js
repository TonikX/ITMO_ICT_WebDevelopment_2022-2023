import instance from "./instance"
import ScenariosAPI from "./scenarios"
import TagsAPI from "./tags";
import GameSystemsAPI from "./game-system";
import AuthAPI from "./auth";

const scenariosAPI = new ScenariosAPI(instance)
const tagsAPI = new TagsAPI(instance)
const gameSystemsAPI = new GameSystemsAPI(instance)
const authAPI = new AuthAPI(instance)

export {
    scenariosAPI,
    tagsAPI,
    gameSystemsAPI,
    authAPI
}
