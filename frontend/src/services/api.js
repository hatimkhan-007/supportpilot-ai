
import axios from "axios";
import { getAuth } from "firebase/auth";

const API = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 10000,
});

API.interceptors.request.use(
    async (config) => {
        const auth = getAuth();
        const user = auth.currentUser;

        console.log("Authenticated Firebase user:", user?.email);

        if (user) {
            const token = await user.getIdToken();

            config.headers.Authorization = `Bearer ${token}`;

            console.log("Firebase token attached successfully.");
        } else {
            console.warn("No Firebase user is logged in.");
        }

        return config;
    },
    (error) => Promise.reject(error)
);

export default API;
