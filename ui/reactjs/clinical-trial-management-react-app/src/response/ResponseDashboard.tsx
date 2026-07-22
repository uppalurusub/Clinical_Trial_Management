import "../styles/ResponseDashboard.css"



import SummaryCard from "./SummaryCard";
import StrategyCard from "./StrategyCard";
import AgentStatusCard from "./AgentStatusCard";

interface ResponseDashboardProps {

    response: any;

}

function ResponseDashboard({

    response

}: ResponseDashboardProps) {

    if (!response) {

        return null;

    }

    return (

        <div className="response-dashboard">

            <SummaryCard response={response} />

            <StrategyCard

                title="Study Setup"

                strategy={response.study_setup}

            />

            <StrategyCard

                title="Site Management"

                strategy={response.site_management}

            />

            <StrategyCard

                title="Recruitment Management"

                strategy={response.recruitment_management}

            />

            <StrategyCard

                title="Monitoring Management"

                strategy={response.monitoring_management}

            />

            <StrategyCard

                title="Finance Management"

                strategy={response.finance_management}

            />

            <StrategyCard

                title="Compliance Management"

                strategy={response.compliance_management}

            />

            <AgentStatusCard

                agents={response.agent_summary}

            />

            {

                response.overall_recommendations?.length > 0 &&

                <div className="card">

                    <h2>

                        Overall Recommendations

                    </h2>

                    <ul>

                        {

                            response.overall_recommendations.map(

                                (item: string, index: number) => (

                                    <li key={index}>

                                        {item}

                                    </li>

                                )

                            )

                        }

                    </ul>

                </div>

            }

        </div>

    );

}

export default ResponseDashboard;