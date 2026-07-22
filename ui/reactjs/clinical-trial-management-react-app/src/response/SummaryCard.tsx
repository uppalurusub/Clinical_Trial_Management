import "../styles/SummaryCard.css";

interface SummaryCardProps {

    response: any;

}

function SummaryCard({

    response

}: SummaryCardProps) {

    if (!response) {

        return null;

    }

    const completedAgents =

        response.agent_summary

            ? Object.keys(response.agent_summary).length

            : 0;

    const recommendationCount =

        response.overall_recommendations

            ? response.overall_recommendations.length

            : 0;

    return (

        <div className="summary-card">

            <div className="summary-header">

                <h1>

                    Clinical Trial Management Report

                </h1>

                <span

                    className={

                        response.success

                            ? "status success"

                            : "status failed"

                    }

                >

                    {

                        response.success

                            ? "SUCCESS"

                            : "FAILED"

                    }

                </span>

            </div>

            <div className="summary-grid">

                <div className="summary-item">

                    <label>

                        Protocol ID

                    </label>

                    <span>

                        {response.protocol_id}

                    </span>

                </div>

                <div className="summary-item">

                    <label>

                        Study Name

                    </label>

                    <span>

                        {response.study_name}

                    </span>

                </div>

                <div className="summary-item">

                    <label>

                        Execution Time

                    </label>

                    <span>

                        {response.execution_timestamp}

                    </span>

                </div>

                <div className="summary-item">

                    <label>

                        Status

                    </label>

                    <span>

                        {

                            response.success

                                ? "Completed"

                                : "Failed"

                        }

                    </span>

                </div>

                <div className="summary-item">

                    <label>

                        Agents Executed

                    </label>

                    <span>

                        {completedAgents}

                    </span>

                </div>

                <div className="summary-item">

                    <label>

                        Recommendations

                    </label>

                    <span>

                        {recommendationCount}

                    </span>

                </div>

            </div>

            {

                response.message &&

                <div className="summary-message">

                    {response.message}

                </div>

            }

        </div>

    );

}

export default SummaryCard;