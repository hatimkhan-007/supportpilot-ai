
import { useAuth } from "../context/AuthContext";
import API from "../services/api";

function Dashboard() {
    const { currentUser, logout } = useAuth();

    async function verifyBackend() {
        const { getAuth } = await import("firebase/auth");
        const auth = getAuth();
        const user = auth.currentUser;

        console.log("Firebase user:", user?.email);

        if (!user) {
            console.error("No authenticated Firebase user found.");
            return;
        }

        try {
            const token = await user.getIdToken();

            console.log("Firebase token retrieved:", !!token);

            const response = await API.get("/api/v1/auth/me", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            console.log("Backend response:", response.data);
            alert(`Authenticated as: ${response.data.email}`);

        } catch (error) {
            console.error("Backend error:", error.response?.data || error.message);
        }
    }

    async function handleLogout() {
        await logout();
    }

    return (
        <div style={{ padding: "40px", textAlign: "center" }}>
            <h1>Welcome to SupportPilot AI</h1>

            <h2>Dashboard</h2>

            <p>
                Logged in as: {currentUser?.email}
            </p>

            <button onClick={verifyBackend}>
                Verify Backend Authentication
            </button>

            <button onClick={handleLogout}>
                Logout
            </button>
        </div>
    );
}

export default Dashboard;
