import instance from "@/api/instance.js";
import CoinsAPI from "@/api/coins.js";
import UsersAPI from "@/api/users.js";
import ChartsAPI from "@/api/charts.js";

const coinsAPI = new CoinsAPI(instance);
const usersAPI = new UsersAPI(instance);
const chartsAPI = new ChartsAPI(instance);

export {
    coinsAPI,
    usersAPI,
    chartsAPI
}