class NasaApi {
    constructor(instance) {
      this.API = instance
    }
  
    getPhoto = async () => {
      return this.API({
        url: '/api/natural?api_key=yWVWXRqt1LwfUpXludkEavgeaDWqdMjyRFtRKZ9Y'
      })
    }
  }
  
  export default NasaApi