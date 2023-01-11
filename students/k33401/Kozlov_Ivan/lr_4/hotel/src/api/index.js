import instance from "@/api/instance"
import WorkersApi from "@/api/workers"
import LoginApi from "@/api/login"
import SingupApi from "@/api/singup";
import CheckTokenApi from "@/api/checkToken";
import RoomsApi from "@/api/rooms";
import BookApi from "@/api/book";
import CLientApi from "@/api/client";
 
const workersApi = new WorkersApi(instance)
const loginApi = new LoginApi(instance)
const singupApi = new SingupApi(instance)
const checkTokenApi = new CheckTokenApi(instance)
const roomsApi = new RoomsApi(instance)
const bookApi = new BookApi(instance)
const cLientApi = new CLientApi(instance)

 
export {
    workersApi,
    loginApi,
    singupApi,
    checkTokenApi,
    roomsApi,
    bookApi,
    cLientApi
}
