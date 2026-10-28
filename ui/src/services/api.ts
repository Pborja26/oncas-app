import axios, { AxiosError, type InternalAxiosRequestConfig} from "axios";

export const api = axios.create({
  baseURL: "/api",
  withCredentials: true,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
});

type RetryConfig = InternalAxiosRequestConfig & { _retry?: boolean };

let refreshing: Promise<unknown> | null = null;

api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const original = error.config as RetryConfig | undefined;

    const shouldRefresh = 
      error.response?.status === 401 &&
      original &&
      !original._retry &&
      !original.url?.startsWith("/auth/");
    
    if (!shouldRefresh) {
      return Promise.reject(error);
    }

    original._retry = true;
    refreshing ??=api.post("/auth/refresh/").finally(() => {
      refreshing = null;
    });

    try {
      await refreshing;
    } catch {
      window.location.href = "/login";
      return Promise.reject(error);
    }

    return api(original);
  }
)