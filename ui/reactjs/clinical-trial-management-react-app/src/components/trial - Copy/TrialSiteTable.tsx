import "../../styles/TrialSiteTable.css"

export interface Site {

    site_id: string;

    site_name: string;

    country: string;

    city: string;

    principal_investigator: string;

    target_enrollment: number;

}

interface Props {

    sites: Site[];

    onChange: (sites: Site[]) => void;

}

const emptySite: Site = {

    site_id: "",

    site_name: "",

    country: "",

    city: "",

    principal_investigator: "",

    target_enrollment: 0

};

function TrialSiteTable({

    sites,

    onChange

}: Props) {

    const handleChange = (

        index: number,

        field: keyof Site,

        value: string | number

    ) => {

        const updated = [...sites];

        updated[index] = {

            ...updated[index],

            [field]: value

        };

        onChange(updated);

    };

    const addSite = () => {

        onChange([

            ...sites,

            { ...emptySite }

        ]);

    };

    const removeSite = (

        index: number

    ) => {

        const updated = sites.filter(

            (_, i) => i !== index

        );

        onChange(updated);

    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>Study Sites</h2>

                <button
                    type="button"
                    className="add-btn"
                    onClick={addSite}
                >
                    + Add Site
                </button>

            </div>

            <table className="site-table">

                <thead>

                    <tr>

                        <th>Site ID</th>

                        <th>Site Name</th>

                        <th>Country</th>

                        <th>City</th>

                        <th>Principal Investigator</th>

                        <th>Enrollment</th>

                        <th>Action</th>

                    </tr>

                </thead>

                <tbody>

                    {

                        sites.map((site, index) => (

                            <tr key={index}>

                                <td>

                                    <input

                                        value={site.site_id}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "site_id",

                                                e.target.value

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <input

                                        value={site.site_name}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "site_name",

                                                e.target.value

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <input

                                        value={site.country}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "country",

                                                e.target.value

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <input

                                        value={site.city}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "city",

                                                e.target.value

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <input

                                        value={site.principal_investigator}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "principal_investigator",

                                                e.target.value

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <input

                                        type="number"

                                        value={site.target_enrollment}

                                        onChange={(e) =>

                                            handleChange(

                                                index,

                                                "target_enrollment",

                                                Number(e.target.value)

                                            )

                                        }

                                    />

                                </td>

                                <td>

                                    <button

                                        type="button"

                                        className="delete-btn"

                                        onClick={() =>

                                            removeSite(index)

                                        }

                                    >

                                        Delete

                                    </button>

                                </td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </div>

    );

}

export default TrialSiteTable;