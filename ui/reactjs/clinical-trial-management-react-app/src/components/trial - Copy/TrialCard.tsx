
import { Link } from "react-router-dom";

import type { Trial } from "../../models/Trial";
import { getStatusBadge } from "../../utils/helpers";

interface TrialCardProps {
  trial: Trial;
  onDelete?: (protocolId: string) => void;
}

const TrialCard = ({
  trial,
  onDelete,
}: TrialCardProps) => {

  const enrollment =
    trial.planned_subjects > 0
      ? Math.round(
          (trial.enrolled_subjects /
            trial.planned_subjects) *
            100
        )
      : 0;

  return (
    <div className="card shadow-sm h-100">

      <div className="card-header d-flex justify-content-between align-items-center">

        <h5 className="mb-0">
          {trial.protocol_id}
        </h5>

        <span
          className={`badge bg-${getStatusBadge(
            trial.status
          )}`}
        >
          {trial.status}
        </span>

      </div>

      <div className="card-body">

        <h5 className="card-title text-primary">
          {trial.trial_name}
        </h5>

        <table className="table table-sm">

          <tbody>

            <tr>
              <th>Sponsor</th>
              <td>{trial.sponsor}</td>
            </tr>

            <tr>
              <th>Phase</th>
              <td>{trial.phase}</td>
            </tr>

            <tr>
              <th>Study Type</th>
              <td>{trial.study_type}</td>
            </tr>

            <tr>
              <th>Therapeutic Area</th>
              <td>{trial.therapeutic_area}</td>
            </tr>

            <tr>
              <th>Principal Investigator</th>
              <td>{trial.principal_investigator}</td>
            </tr>

            <tr>
              <th>Country</th>
              <td>{trial.country}</td>
            </tr>

          </tbody>

        </table>

        <div className="mt-3">

          <div className="d-flex justify-content-between">

            <span>Enrollment</span>

            <span>
              {trial.enrolled_subjects} /
              {" "}
              {trial.planned_subjects}
            </span>

          </div>

          <div className="progress mt-2">

            <div
              className="progress-bar"
              role="progressbar"
              style={{
                width: `${enrollment}%`,
              }}
            >
              {enrollment}%
            </div>

          </div>

        </div>

      </div>

      <div className="card-footer d-flex gap-2 flex-wrap">

        <Link
          to={`/dashboard/${trial.protocol_id}`}
          className="btn btn-primary btn-sm"
        >
          Dashboard
        </Link>

        <Link
          to={`/trial/history/${trial.protocol_id}`}
          className="btn btn-info btn-sm text-white"
        >
          History
        </Link>

        <Link
          to={`/trial/manage`}
          className="btn btn-warning btn-sm text-dark"
        >
          Edit
        </Link>

        {onDelete && (

          <button
            className="btn btn-danger btn-sm ms-auto"
            onClick={() =>
              onDelete(trial.protocol_id)
            }
          >
            Delete
          </button>

        )}

      </div>

    </div>
  );
};

export default TrialCard;

