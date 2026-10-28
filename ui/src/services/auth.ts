import { api } from "./api";
import axios from "axios";

export type User = {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  birth_date: string | null;
};

export type RegisterData = Omit<User, "id"> & { password: string };

export type LoginResult = {
  status: number;
  user: User | null;
}

export const auth = {
  csrf: () => api.get("/auth/csrf/"),
  register: (data: RegisterData) => api.post<User>("/auth/register/", data),
  logout: () => api.post("/auth/logout/"),
  user: () => api.get<User>("/auth/user/"),
  login: async (username: string, password: string): Promise<LoginResult> => {
    try {
      const res = await api.post<{ user: User }>("/auth/login/", { username, password });
      return { status: res.status, user: res.data.user }
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        return { status: error.response.status, user: null };
      }
      throw error;
    }
    
  },
};
