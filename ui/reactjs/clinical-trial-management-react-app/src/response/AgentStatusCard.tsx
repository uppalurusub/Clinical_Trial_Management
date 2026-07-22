import "../styles/AgentStatusCard.css"

interface AgentStatusCardProps {

    agents: Record<string, string>;

}

function AgentStatusCard({

    agents

}: AgentStatusCardProps) {

    if (!agents) {

        return null;

    }

    const getStatusClass = (

        status: string

    ) => {

        switch (status.toLowerCase()) {

            case "completed":

                return "completed";

            case "running":

                return "running";

            case "failed":

                return "failed";

            case "warning":

                return "warning";

            default:

                return "unknown";

        }

    };

    const getStatusIcon = (

        status: string

    ) => {

        switch (status.toLowerCase()) {

            case "completed":

                return "✅";

            case "running":

                return "⏳";

            case "failed":

                return "❌";

            case "warning":

                return "⚠️";

            default:

                return "⚪";

        }

    };

    return (

        <div className="agent-card">

            <div className="agent-header">

                <h2>

                    Agent Execution Status

                </h2>

            </div>

            <table className="agent-table">

                <thead>

                    <tr>

                        <th>

                            Agent

                        </th>

                        <th>

                            Status

                        </th>

                    </tr>

                </thead>

                <tbody>

                    {

                        Object.entries(agents).map(

                            ([agent, status]) => (

                                <tr key={agent}>

                                    <td>

                                        {agent}

                                    </td>

                                    <td>

                                        <span

                                            className={`status ${getStatusClass(status)}`}

                                        >

                                            {getStatusIcon(status)}

                                            {" "}

                                            {status}

                                        </span>

                                    </td>

                                </tr>

                            )

                        )

                    }

                </tbody>

            </table>

        </div>

    );

}

export default AgentStatusCard;