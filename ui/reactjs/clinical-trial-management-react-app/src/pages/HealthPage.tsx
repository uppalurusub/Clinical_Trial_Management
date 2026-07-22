import { useEffect, useState } from "react";
import TrialService from "../services/TrialService";
import "../styles/HealthPage.css"

interface HealthResponse {
    success: boolean;
    service: string;
    status: string;
    version?: string;
}

function HealthPage() {

    const [health, setHealth] = useState<HealthResponse | null>(null);

    const [loading, setLoading] = useState(true);

    const loadHealth = async () => {

        try {

            setLoading(true);

            const response = await TrialService.health();

            setHealth(response.data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

    useEffect(() => {

        loadHealth();

    }, []);

    if (loading)
        return <h2>Loading...</h2>;

    return (

        <div className="health-page">

            <div className="page-header">

                <h1>🩺 System Health</h1>

                <button onClick={loadHealth}>
                    🔄 Refresh
                </button>

            </div>

            <div className="health-cards">

                <div className="card">

                    <h4>Backend</h4>

                    <span
                        className={
                            health?.status === "UP"
                                ? "status up"
                                : "status down"
                        }
                    >
                        {health?.status}
                    </span>

                </div>

                <div className="card">

                    <h4>Service</h4>

                    <p>{health?.service}</p>

                </div>

                <div className="card">

                    <h4>Version</h4>

                    <p>{health?.version ?? "1.0.0"}</p>

                </div>

            </div>

            

        </div>

    );

}

export default HealthPage;