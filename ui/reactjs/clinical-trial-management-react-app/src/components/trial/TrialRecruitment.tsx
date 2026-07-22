import "../../styles/TrialRecruitment.css"

export interface Recruitment {

    target_patients: number;

    inclusion_criteria: string[];

    exclusion_criteria: string[];

    recruitment_channels: string[];

}

interface Props {

    recruitment: Recruitment;

    onChange: (recruitment: Recruitment) => void;

}

function TrialRecruitment({

    recruitment,

    onChange

}: Props) {

    const updateTargetPatients = (

        value: number

    ) => {

        onChange({

            ...recruitment,

            target_patients: value

        });

    };

    const updateArray = (

        field: keyof Recruitment,

        index: number,

        value: string

    ) => {

        const updated = [...(recruitment[field] as string[])];

        updated[index] = value;

        onChange({

            ...recruitment,

            [field]: updated

        });

    };

    const addItem = (

        field: keyof Recruitment

    ) => {

        onChange({

            ...recruitment,

            [field]: [

                ...(recruitment[field] as string[]),

                ""

            ]

        });

    };

    const removeItem = (

        field: keyof Recruitment,

        index: number

    ) => {

        const updated =

            (recruitment[field] as string[])

                .filter((_, i) => i !== index);

        onChange({

            ...recruitment,

            [field]: updated

        });

    };

    const renderSection = (

        title: string,

        field: keyof Recruitment

    ) => (

        <div className="section">

            <div className="section-header">

                <h3>{title}</h3>

                <button

                    type="button"

                    className="add-btn"

                    onClick={() => addItem(field)}

                >

                    + Add

                </button>

            </div>

            {

                (recruitment[field] as string[]).map(

                    (item, index) => (

                        <div

                            className="row"

                            key={index}

                        >

                            <input

                                value={item}

                                onChange={(e) =>

                                    updateArray(

                                        field,

                                        index,

                                        e.target.value

                                    )

                                }

                            />

                            <button

                                type="button"

                                className="delete-btn"

                                onClick={() =>

                                    removeItem(

                                        field,

                                        index

                                    )

                                }

                            >

                                Delete

                            </button>

                        </div>

                    )

                )

            }

        </div>

    );

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Recruitment

                </h2>

            </div>

            <div className="form-group">

                <label>

                    Target Patients

                </label>

                <input

                    type="number"

                    value={recruitment.target_patients}

                    onChange={(e) =>

                        updateTargetPatients(

                            Number(e.target.value)

                        )

                    }

                />

            </div>

            {renderSection(

                "Inclusion Criteria",

                "inclusion_criteria"

            )}

            {renderSection(

                "Exclusion Criteria",

                "exclusion_criteria"

            )}

            {renderSection(

                "Recruitment Channels",

                "recruitment_channels"

            )}

        </div>

    );

}

export default TrialRecruitment;