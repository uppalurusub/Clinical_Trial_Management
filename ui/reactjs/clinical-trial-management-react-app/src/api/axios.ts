import axios from "axios";

import type {
  AxiosError,
  AxiosInstance,
  AxiosResponse,
  InternalAxiosRequestConfig,
} from "axios";

/**
 * Base URL
 * Use VITE_API_BASE_URL from .env
 */
const BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1";

/**
 * Axios Instance
 */
const api: AxiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 3000000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

/**
 * Request Interceptor
 */
api.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    console.log(
      `🚀 ${config.method?.toUpperCase()} ${config.baseURL}${config.url}`
    );

    // Example:
    // const token = localStorage.getItem("access_token");
    // if (token) {
    //     config.headers.Authorization = `Bearer ${token}`;
    // }

    return config;
  },
  (error: AxiosError) => {
    console.error("Request Error:", error);
    return Promise.reject(error);
  }
);

/**
 * Response Interceptor
 */
api.interceptors.response.use(
  (response: AxiosResponse) => {
    console.log(
      `✅ ${response.status} ${response.config.method?.toUpperCase()} ${response.config.url}`
    );

    return response;
  },
  (error: AxiosError) => {
    if (error.response) {
      console.error("API Error");

      console.error("Status :", error.response.status);
      console.error("Message:", error.response.data);

      switch (error.response.status) {
        case 400:
          alert("Bad Request");
          break;

        case 401:
          alert("Unauthorized");
          break;

        case 403:
          alert("Forbidden");
          break;

        case 404:
          alert("Resource Not Found");
          break;

        case 500:
          alert("Internal Server Error");
          break;

        default:
          alert("Unexpected Server Error");
      }
    } else if (error.request) {
      alert("Unable to connect to server.");
    } else {
      alert(error.message);
    }

    return Promise.reject(error);
  }
);

export default api;