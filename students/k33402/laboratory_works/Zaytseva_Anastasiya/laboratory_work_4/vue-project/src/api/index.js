import instance from "@/api/instance"
import ProductsAPI from "@/api/products"
import UsersAPI from "@/api/users"

const productsAPI = new ProductsAPI(instance)
const usersAPI = new UsersAPI(instance)

export {
  productsAPI,
  usersAPI
}

