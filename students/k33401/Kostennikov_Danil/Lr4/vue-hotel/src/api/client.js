class ClientApi {
  constructor(instance) {
    this.API = instance;
  }

  clientCityCount = async (data) => {
    return this.API({
      url: `/client/${data}`,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
}

export default ClientApi;
