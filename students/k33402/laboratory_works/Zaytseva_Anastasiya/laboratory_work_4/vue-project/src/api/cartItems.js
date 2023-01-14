class CartItemsAPI {
 constructor(instance) {
    this.API = instance
 }

 fetchCartItems = async (token) => {
   return this.API({
     url: '/api/v1/cart-items',
     headers: {
       'Authorization': `Token ${token}`
     }
   })
 }

 createCartItem = async (data, token) => {
    return this.API({
      method: 'POST',
      url: '/api/v1/cart-items/create',
      data,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      }
    })
 }

 removeCartItem = async (id, token) => {
   return this.API({
     method: 'DELETE',
     url: `/api/v1/cart-items/${id}/remove`,
     headers: {
       'Content-Type': 'application/json',
       'Authorization': `Token ${token}`
     }
   })
}

}

export default CartItemsAPI