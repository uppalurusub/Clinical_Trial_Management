import { useEffect, useState } from "react";
import TrialService from "../../services/TrialService";

function TrialList() {
    const [trials, setTrials] = useState([]);

    useEffect(() => {
        loadTrials();
    }, []);

    async function loadTrials() {
        try {
            const response = await TrialService.getAllTrials();
            
            console.log("Response Data:", response.data);

            const trials = Object.values(
                response.data.data.data
            );

            setTrials(trials);

        } catch (error) {
            console.error("Error loading trials:", error);
        }
    }

    return (
        <div>
            <h2>Clinical Trials</h2>

            <table>
                <thead>
                    <tr>
                        <th>Protocol ID</th>
                        <th>Trial Name</th>
                        <th>Sponsor</th>
                        <th>Status</th>
                    </tr>
                </thead>

                <tbody>

                    {trials.map((trial:any,index:number)=>{

                        const t = trial.data;

                        return(

                            <tr key={index}>

                                <td>{t.protocol_id}</td>

                                <td>{t.study_name}</td>

                                <td>{t.execution_timestamp}</td>

                            </tr>

                        );

                    })}

                </tbody>
            </table>
        </div>
    );
}

export default TrialList;