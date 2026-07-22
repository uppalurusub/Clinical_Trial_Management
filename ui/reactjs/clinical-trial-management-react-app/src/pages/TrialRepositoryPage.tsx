import { useEffect, useState } from "react";
import TrialService from "../services/TrialService";
import type { Trial } from "../models/Trial";

function TrialRepositoryPage() {

    const [trials, setTrials] = useState<Trial[]>([]);

    const [loading, setLoading] = useState(true);

    const [search, setSearch] = useState("");

    const [error, setError] = useState("");

    useEffect(() => {

        loadTrials();

    }, []);

    async function loadTrials() {

        try {

            setLoading(true);

            const response = await TrialService.getAllTrials();

            console.log(response.data);

            const apiTrials = response.data.data.data;

            const repository: Trial[] = Object.values(apiTrials).map(

                (item: any) => item.data

            );

            setTrials(repository);

            console.log("Repository");

            console.log(repository);

            console.log(repository[0]);

        }
        catch (err) {

            console.error(err);

            setError("Unable to load Trial Repository");

        }
        finally {

            setLoading(false);

        }

    }

    const filteredTrials = trials.filter((trial) =>

        trial.protocol_id
            ?.toLowerCase()
            .includes(search.toLowerCase())

        ||

        trial.study_name
            ?.toLowerCase()
            .includes(search.toLowerCase())

    );

    if (loading)
        return <h3>Loading Trial Repository...</h3>;

    if (error)
        return <h3>{error}</h3>;

    return (

        <div className="container">

            <h2>Clinical Trial Repository</h2>

            <input

                type="text"

                placeholder="Search Protocol..."

                value={search}

                onChange={(e) =>

                    setSearch(e.target.value)

                }

            />

            <br />

            <br />

            <table>

                <thead>

                    <tr>

                        <th>Protocol</th>

                        <th>Study</th>

                        

                        

                        <th>Status</th>

                        

                        

                    </tr>

                </thead>

                <tbody>

            {

            filteredTrials.map((trial)=>(

            <tr key={trial.protocol_id}>

                <td>

                    {trial.protocol_id}

                </td>

                <td>

                    {trial.study_name}

                </td>

                

                

                <td>

                    <span className="badge bg-success">

                        Active

                    </span>

                </td>

                

                

            </tr>

            ))

            }

            </tbody>
            </table>

        </div>

    );

}

export default TrialRepositoryPage;