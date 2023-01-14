import instance from "@/api/instance"
import ProductsAPI from "@/api/products"
import UsersAPI from "@/api/users"
import OrdersAPI from "@/api/orders"
import CartItemsAPI from "@/api/cartItems"

const productsAPI = new ProductsAPI(instance)
const usersAPI = new UsersAPI(instance)
const ordersAPI = new OrdersAPI(instance)
const cartItemsAPI = new CartItemsAPI(instance)

export {
  productsAPI,
  usersAPI,
  ordersAPI,
  cartItemsAPI
}

