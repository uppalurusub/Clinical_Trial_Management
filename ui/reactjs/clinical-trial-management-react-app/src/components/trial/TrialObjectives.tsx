import "../../styles/TrialObjectives.css"


interface TrialObjectivesProps {

    objectives: string[];

    onChange: (objectives: string[]) => void;

}

function TrialObjectives({

    objectives,

    onChange

}: TrialObjectivesProps) {

    const updateObjective = (

        index: number,

        value: string

    ) => {

        const updated = [...objectives];

        updated[index] = value;

        onChange(updated);

    };

    const addObjective = () => {

        onChange([

            ...objectives,

            ""

        ]);

    };

    const removeObjective = (

        index: number

    ) => {

        const updated = objectives.filter(

            (_, i) => i !== index

        );

        onChange(updated);

    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Trial Objectives

                </h2>

                <button

                    type="button"

                    className="add-btn"

                    onClick={addObjective}

                >

                    + Add Objective

                </button>

            </div>

            {

                objectives.length === 0 &&

                <p className="empty">

                    No objectives added.

                </p>

            }

            {

                objectives.map((objective, index) => (

                    <div
                        className="objective-row"
                        key={index}
                    >

                        <span className="serial">

                            {index + 1}

                        </span>

                        <textarea

                            rows={2}

                            value={objective}

                            onChange={(e) =>

                                updateObjective(

                                    index,

                                    e.target.value

                                )

                            }

                            placeholder="Enter trial objective"

                        />

                        <button

                            type="button"

                            className="delete-btn"

                            onClick={() =>

                                removeObjective(index)

                            }

                        >

                            Delete

                        </button>

                    </div>

                ))

            }

        </div>

    );

}

export default TrialObjectives;