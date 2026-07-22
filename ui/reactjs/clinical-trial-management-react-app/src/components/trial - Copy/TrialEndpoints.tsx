import "../../styles/TrialEndpoints.css"


interface TrialEndpointsProps {

    primaryEndpoint: string;

    secondaryEndpoints: string[];

    onPrimaryChange: (value: string) => void;

    onSecondaryChange: (values: string[]) => void;

}

function TrialEndpoints({

    primaryEndpoint,

    secondaryEndpoints,

    onPrimaryChange,

    onSecondaryChange

}: TrialEndpointsProps) {

    const updateSecondary = (

        index: number,

        value: string

    ) => {

        const updated = [...secondaryEndpoints];

        updated[index] = value;

        onSecondaryChange(updated);

    };

    const addSecondary = () => {

        onSecondaryChange([

            ...secondaryEndpoints,

            ""

        ]);

    };

    const removeSecondary = (

        index: number

    ) => {

        const updated =

            secondaryEndpoints.filter(

                (_, i) => i !== index

            );

        onSecondaryChange(updated);

    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Clinical Endpoints

                </h2>

            </div>

            {/* Primary Endpoint */}

            <div className="form-group">

                <label>

                    Primary Endpoint

                </label>

                <textarea

                    rows={3}

                    value={primaryEndpoint}

                    placeholder="Enter Primary Endpoint"

                    onChange={(e) =>

                        onPrimaryChange(

                            e.target.value

                        )

                    }

                />

            </div>

            {/* Secondary Endpoints */}

            <div className="secondary-header">

                <h3>

                    Secondary Endpoints

                </h3>

                <button

                    type="button"

                    className="add-btn"

                    onClick={addSecondary}

                >

                    + Add Endpoint

                </button>

            </div>

            {

                secondaryEndpoints.length === 0 && (

                    <p className="empty">

                        No Secondary Endpoints Added

                    </p>

                )

            }

            {

                secondaryEndpoints.map(

                    (endpoint, index) => (

                        <div

                            className="endpoint-row"

                            key={index}

                        >

                            <span className="number">

                                {index + 1}

                            </span>

                            <textarea

                                rows={2}

                                value={endpoint}

                                placeholder="Enter Secondary Endpoint"

                                onChange={(e) =>

                                    updateSecondary(

                                        index,

                                        e.target.value

                                    )

                                }

                            />

                            <button

                                type="button"

                                className="delete-btn"

                                onClick={() =>

                                    removeSecondary(index)

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

}

export default TrialEndpoints;