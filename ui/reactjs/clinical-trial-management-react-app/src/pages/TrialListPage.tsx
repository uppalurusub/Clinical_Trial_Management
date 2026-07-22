
import { useEffect, useState } from "react";

import TrialList from "../components/trial/TrialList";
import TrialService from "../services/TrialService";

const TrialListPage = () => {
  const [trials, setTrials] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    loadTrials();
  }, []);

  const loadTrials = async () => {
    try {
      setLoading(true);

      const response = await TrialService.getAllTrials();

      setTrials(response.data);

      setError("");
    } catch (err) {
      console.error(err);

      setError("Unable to load clinical trials.");
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (protocolId: string) => {
    const confirmed = window.confirm(
      `Are you sure you want to delete protocol ${protocolId}?`
    );

    if (!confirmed) {
      return;
    }

    try {
      await TrialService.deleteTrial(protocolId);

      await loadTrials();

      alert("Trial deleted successfully.");
    } catch (err) {
      console.error(err);

      alert("Failed to delete trial.");
    }
  };

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div
          className="spinner-border text-primary"
          role="status"
        >
          <span className="visually-hidden">
            Loading...
          </span>
        </div>

        <p className="mt-3">
          Loading Clinical Trials...
        </p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="alert alert-danger">
        {error}
      </div>
    );
  }

  return (
    <div className="container-fluid">

      {/* Page Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">

        <div>
          <h2 className="fw-bold text-primary">
            Clinical Trial Repository
          </h2>

          <p className="text-muted">
            Browse, search, and manage all registered
            clinical trials.
          </p>
        </div>

      </div>

      {/* Trial List */}
      <TrialList
        trials={trials}
        onDelete={handleDelete}
      />

    </div>
  );
};

export default TrialListPage;

