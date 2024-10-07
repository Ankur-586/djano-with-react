// In this we will define a Interceptor:
/* Interceptor: it will intercept any request that we are gonna send
                and it will automatically add the correct headers so
                we don't have to manually write it repeatedly in our 
                code.
axios is a Interceptor
*/
import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    console.log('mjfafojadhvoa',token)
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
