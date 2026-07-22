import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import TrialHistory from "../components/trial/TrialHistory";
import TrialService from "../services/TrialService";

const TrialHistoryPage = () => {

    const { protocolId } = useParams();

    const [protocol, setProtocol] =
        useState(protocolId ?? "");

    const [historyData, setHistoryData] =
        useState<any[]>([]);

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");



const loadHistory = async (

    id?: string

) => {

    const protocolValue = id ?? protocol;

    if (!protocolValue.trim()) {

        alert("Please enter Protocol ID");

        return;

    }

    try {

        setLoading(true);

        setError("");

        const response =
            await TrialService.getHistory(protocolValue);

        console.log(response.data);

        const apiData = response.data.data?.history;

        if (apiData) {

          const history = [

              {

                  timestamp: apiData.created_at,

                  action: "Trial Created",

                  performed_by: "Clinical Trial Operations Manager",

                  status: "Completed",

                  comments: apiData.data.study_name

              },

              {

                  timestamp: apiData.updated_at,

                  action: "Trial Updated",

                  performed_by: "System",

                  status: "Completed",

                  comments: "Latest Trial Configuration"

              }

          ];

          setHistoryData(history);
        }
        else{

          setHistoryData([]);

        } 

        

    }
    catch (err) {

        console.error(err);

        setError("Unable to load history");

    }
    finally {

        setLoading(false);

    }

};

useEffect(() => {

    if (protocolId) {

        setProtocol(protocolId);

        loadHistory(protocolId);

    }

}, [protocolId]);

return (

        <div className="container-fluid">

            <div className="mb-4">

                <h2 className="fw-bold text-primary">

                    Trial History

                </h2>

                <p className="text-muted">

                    Review protocol history, audit trail,
                    milestones and workflow.

                </p>

            </div>

            <div className="card shadow-sm mb-4">

                <div className="card-body">

                    <div className="row align-items-end">

                        <div className="col-md-8">

                            <label className="form-label">

                                Protocol ID

                            </label>

                            <input

                                type="text"

                                className="form-control"

                                placeholder="PROTO-DM-2026-001"

                                value={protocol}

                                onChange={(e)=>

                                    setProtocol(e.target.value)

                                }

                            />

                        </div>

                        <div className="col-md-4">

                            <button

                                className="btn btn-primary w-100"

                                onClick={() => loadHistory()}

                                disabled={loading}

                            >

                                {

                                    loading

                                    ? "Loading..."

                                    : "Load History"

                                }

                            </button>

                        </div>

                    </div>

                </div>

            </div>

            {

                error &&

                <div className="alert alert-danger">

                    {error}

                </div>

            }

            <TrialHistory

                protocolId={protocol}

                history={historyData}

            />

        </div>

    );

};
export default TrialHistoryPage;