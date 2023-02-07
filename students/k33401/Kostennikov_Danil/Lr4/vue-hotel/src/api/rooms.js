class RoomsApi {
  constructor(instance) {
    this.API = instance;
  }

  freeRooms = async (date) => {
    return this.API({
      url: `/free_rooms/${date}`,
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
}

export default RoomsApi;
