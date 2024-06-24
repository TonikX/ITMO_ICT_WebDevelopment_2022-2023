import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000",
});

axiosInstance.interceptors.request.use(
  (config) => {
    const token = sessionStorage.getItem("authToken");
    config.headers.common["Authorization"] = token ? `Token ${token}` : "";
    return config;
  },
  (error) => {
    console.log(error.response);
    return Promise.reject(error);
  }
);

export default axiosInstance;
