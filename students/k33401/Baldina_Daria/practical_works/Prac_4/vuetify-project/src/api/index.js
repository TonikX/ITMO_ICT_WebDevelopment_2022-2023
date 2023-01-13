import instance from "@/api/instance"
import NasaApi from "@/api/nasa"

const nasaApi = new NasaApi(instance)

export {
  nasaApi
}