class OrdersAPI {
 constructor(instance) {
    this.API = instance
 }

 fetchOrders = async (token) => {
    return this.API({
      url: '/api/v1/orders',
      headers: {
        'Authorization': `Token ${token}`
      }
    })
 }

 createOrder = async (token) => {
  return this.API({
    method: 'POST',
    url: '/api/v1/orders/create',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`
    }
  })
}

}

export default OrdersAPI