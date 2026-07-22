import { formatDateTime } from "../../utils/helpers";

interface TrialHistoryItem {
  id?: number;
  timestamp: string;
  action: string;
  performed_by: string;
  status: string;
  comments?: string;
}

interface TrialHistoryProps {
  protocolId: string;
  history: TrialHistoryItem[];
}

const TrialHistory = ({
  protocolId,
  history,
}: TrialHistoryProps) => {

  if (!history || history.length === 0) {
    return (
      <div className="alert alert-info">
        No history available for protocol:
        <strong> {protocolId}</strong>
      </div>
    );
  }

  return (
    <div className="card shadow-sm">

      <div className="card-header bg-primary text-white">

        <div className="d-flex justify-content-between">

          <h5 className="mb-0">
            Trial History
          </h5>

          <div className="d-flex align-items-center gap-2">

            <label className="fw-bold mb-0">
                Protocol ID
            </label>

            <input
                type="text"
                className="form-control"
                style={{ width: "250px" }}
                value={protocolId}
                readOnly
            />

          </div>

        </div>

      </div>

      <div className="card-body">

        <div className="table-responsive">

          <table className="table table-hover table-bordered">

            <thead className="table-light">

              <tr>
                <th>#</th>
                <th>Date / Time</th>
                <th>Action</th>
                <th>Status</th>
                <th>Performed By</th>
                <th>Comments</th>
              </tr>

            </thead>

            <tbody>

              {(Array.isArray(history) ? history : []).map((item, index) => (

                <tr key={item.id ?? index}>

                  <td>{index + 1}</td>

                  <td>
                    {formatDateTime(
                      item.timestamp
                    )}
                  </td>

                  <td>{item.action}</td>

                  <td>

                    <span
                      className={`badge bg-${
                        item.status === "Completed"
                          ? "success"
                          : item.status === "Approved"
                          ? "primary"
                          : item.status === "Pending"
                          ? "warning"
                          : item.status === "Rejected"
                          ? "danger"
                          : "secondary"
                      }`}
                    >
                      {item.status}
                    </span>

                  </td>

                  <td>
                    {item.performed_by}
                  </td>

                  <td>
                    {item.comments ??
                      "-"}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

      <div className="card-footer text-muted">

        Total Records :
        {" "}
        <strong>
          {history.length}
        </strong>

      </div>

    </div>
  );
};

export default TrialHistory;

