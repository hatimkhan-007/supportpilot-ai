import { useEffect, useState } from "react";
import API from "./services/api";

function App() {
    const [backendStatus, setBackendStatus] = useState("Checking...");
    const [backendData, setBackendData] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {

        const checkBackend = async () => {

            try {

                const response = await API.get("/api/v1/health");

                setBackendData(response.data);
                setBackendStatus("Connected");

            } catch (err) {

                console.error("Backend Error:", err);

                setBackendStatus("Disconnected");
                setError("Unable to connect to FastAPI backend.");

            }

        };

        checkBackend();

    }, []);

    return (
        <div style={{
            fontFamily: "Arial",
            padding: "40px",
            textAlign: "center"
        }}>

            <h1>SupportPilot AI</h1>

            <p>Intelligent Customer Support Platform</p>

            <hr />

            <h2>Backend Connection</h2>

            <h3>
                Status: {backendStatus}
            </h3>

            {backendData && (
                <div>
                    <p>{backendData.application}</p>
                    <p>{backendData.backend}</p>
                    <p>{backendData.status}</p>
                </div>
            )}

            {error && (
                <p style={{ color: "red" }}>
                    {error}
                </p>
            )}

        </div>
    );
}

export default App;
