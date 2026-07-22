import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="container-fluid">

      {/* Welcome Section */}
      <div className="card shadow-sm border-0 mb-4">
        <div className="card-body">
          <h2 className="fw-bold text-primary">
            Clinical Trial Management System
          </h2>

          <p className="text-muted mt-3">
            Welcome to the Clinical Trial Management System (CTMS).
            This application enables clinical research teams to
            manage trial protocols, monitor study progress,
            review trial history, and visualize key performance
            indicators through interactive dashboards.
          </p>
        </div>
      </div>

      {/* Feature Cards */}
      <div className="row g-4">

        {/* Dashboard */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-primary">
                Dashboard
              </h4>

              <p>
                View protocol metrics, enrollment progress,
                adverse events, study status, and analytics.
              </p>

              <Link
                to="/dashboard/PROTOCOL001"
                className="btn btn-primary"
              >
                Open Dashboard
              </Link>

            </div>
          </div>
        </div>

        {/* Manage Trial */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-success">
                Manage Trial
              </h4>

              <p>
                Create, update, and maintain
                clinical trial information.
              </p>

              <Link
                to="/trial/manage"
                className="btn btn-success"
              >
                Manage Trial
              </Link>

            </div>
          </div>
        </div>

        {/* Trial History */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-warning">
                Trial History
              </h4>

              <p>
                Review protocol activities,
                audit history, and previous
                trial events.
              </p>

              <Link
                to="/trial/history/PROTOCOL001"
                className="btn btn-warning text-white"
              >
                View History
              </Link>

            </div>
          </div>
        </div>

        {/* Trial List */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-info">
                Trial Repository
              </h4>

              <p>
                Browse and search all
                registered clinical trials.
              </p>

              <Link
                to="/trial/list"
                className="btn btn-info text-white"
              >
                View Trials
              </Link>

            </div>
          </div>
        </div>

        {/* Health Check */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-danger">
                System Health
              </h4>

              <p>
                Verify backend service,
                API availability,
                and application status.
              </p>

              <Link
                to="/health"
                className="btn btn-danger"
              >
                Health Status
              </Link>

            </div>
          </div>
        </div>

        {/* Future Modules */}
        <div className="col-md-4">
          <div className="card shadow-sm h-100">
            <div className="card-body">

              <h4 className="text-secondary">
                Coming Soon
              </h4>

              <ul className="mb-3">
                <li>Patient Enrollment</li>
                <li>Site Management</li>
                <li>Study Documents</li>
                <li>Monitoring Visits</li>
                <li>Risk Dashboard</li>
              </ul>

              <button
                className="btn btn-secondary"
                disabled
              >
                Available Soon
              </button>

            </div>
          </div>
        </div>

      </div>

    </div>
  );
};

export default Home;

