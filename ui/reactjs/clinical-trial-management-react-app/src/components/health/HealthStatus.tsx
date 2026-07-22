import { useEffect, useState } from "react";

import TrialService from "../../services/TrialService";

interface HealthResponse {
  status: string;
  message: string;
  version?: string;
  timestamp?: string;
}

const HealthStatus = () => {
  const [health, setHealth] =
    useState<HealthResponse | null>(null);

  const [loading, setLoading] =
    useState<boolean>(true);

  const [error, setError] =
    useState<string>("");

  const loadHealth = async () => {
    try {
      setLoading(true);

      const response =
        await TrialService.health();

      setHealth(response.data);

      setError("");

    } catch (err: any) {

      console.error(err);

      setError(
        err?.response?.data?.detail ??
        "Backend service is unavailable."
      );

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {
    loadHealth();
  }, []);

  if (loading) {
    return (
      <div className="card shadow-sm">
        <div className="card-body text-center">

          <div
            className="spinner-border text-primary"
            role="status"
          >
            <span className="visually-hidden">
              Loading...
            </span>
          </div>

          <p className="mt-3 mb-0">
            Checking System Health...
          </p>

        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card border-danger shadow-sm">

        <div className="card-header bg-danger text-white">
          System Health
        </div>

        <div className="card-body">

          <h5 className="text-danger">
            Backend Offline
          </h5>

          <p>{error}</p>

          <button
            className="btn btn-danger"
            onClick={loadHealth}
          >
            Retry
          </button>

        </div>

      </div>
    );
  }

  return (
    <div className="card shadow-sm">

      <div className="card-header bg-success text-white">

        System Health

      </div>

      <div className="card-body">

        <div className="row">

          <div className="col-md-3 mb-3">

            <strong>Status</strong>

            <div>

              <span className="badge bg-success">
                {health?.status}
              </span>

            </div>

          </div>

          <div className="col-md-5 mb-3">

            <strong>Message</strong>

            <p className="mb-0">
              {health?.message}
            </p>

          </div>

          <div className="col-md-2 mb-3">

            <strong>Version</strong>

            <p className="mb-0">
              {health?.version ?? "N/A"}
            </p>

          </div>

          <div className="col-md-2 mb-3">

            <strong>Updated</strong>

            <p className="mb-0">
              {health?.timestamp ?? "-"}
            </p>

          </div>

        </div>

        <button
          className="btn btn-success"
          onClick={loadHealth}
        >
          Refresh
        </button>

      </div>

    </div>
  );
};

export default HealthStatus;

