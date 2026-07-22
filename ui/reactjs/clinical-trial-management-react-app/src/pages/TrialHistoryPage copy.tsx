import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import TrialHistory from "../components/trial/TrialHistory";
import TrialService from "../services/TrialService";



const TrialHistoryPage = () => {

    const [protocolId, setProtocolId] = useState("");

    const [historyData, setHistoryData] = useState<any[]>([]);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    useEffect(() => {

    if (!protocolId) {

        return;

    }

      setProtocol(protocolId);

      loadHistory(protocolId);

    }, [protocolId]);

    const loadHistory = async () => {

        if (!protocol.trim()) {

            alert("Please enter Protocol ID");

            return;

        }

        try {

            setLoading(true);

            setError("");

            const response =
                await TrialService.getHistory(protocol);

            console.log(response.data);

            /*
               Adjust this line depending on your API response.

               If API returns

               {
                   history:[...]
               }

               use:

               setHistoryData(response.data.history);

               If API returns an array directly

               use:

               setHistoryData(response.data);

            */

            if (Array.isArray(response.data)) {

                setHistoryData(response.data);

            }
            else if (Array.isArray(response.data.history)) {

                setHistoryData(response.data.history);

            }
            else if (Array.isArray(response.data.data)) {

                setHistoryData(response.data.data);

            }
            else {

                setHistoryData([]);

            }

        }
        catch (err) {

            console.error(err);

            setError("Unable to load trial history.");

        }
        finally {

            setLoading(false);

        }

    };

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

                                onClick={loadHistory}

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