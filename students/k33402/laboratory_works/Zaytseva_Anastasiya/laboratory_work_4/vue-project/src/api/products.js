class ProductsAPI {
 constructor(instance) {
    this.API = instance
 }

 fetchProductCount = async () => {
  return this.API({
    url: '/api/v1/product_count'
  })
}

fetchProduct = async (id) => {
  return this.API({
    url: `/api/v1/products/${id}`
  })
}

 fetchProducts = async (limit) => {
    return this.API({
      url: `/api/v1/products${limit ? `?limit=${limit}` : ''}`
    })
 }

 fetchProductsByColor = async (color) => {
    if (color === '') {
      return this.fetchProducts();
    }
    return this.API({
      url: `/api/v1/products?color=${color}`
    })
 }
}

export default ProductsAPI