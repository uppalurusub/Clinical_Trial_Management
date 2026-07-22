import "../../styles/TrialActions.css";

interface TrialActionsProps {

    loading: boolean;

    isEdit: boolean;

    onSubmit: () => void;

    onReset: () => void;

    onCancel: () => void;

    onPreview: () => void;

}

function TrialActions({

    loading,

    isEdit,

    onSubmit,

    onReset,

    onCancel,

    onPreview

}: TrialActionsProps) {

    return (

        <div className="action-card">

            <div className="action-header">

                <h2>

                    Trial Actions

                </h2>

            </div>

            <div className="action-buttons">

                <button

                    type="button"

                    className="btn btn-success"

                    onClick={onSubmit}

                    disabled={loading}

                >

                    {

                        loading

                            ? "Saving..."

                            : isEdit

                                ? "Update Trial"

                                : "Save Trial"

                    }

                </button>

                <button

                    type="button"

                    className="btn btn-primary"

                    onClick={onPreview}

                >

                    Preview JSON

                </button>

                <button

                    type="button"

                    className="btn btn-warning"

                    onClick={onReset}

                >

                    Reset

                </button>

                <button

                    type="button"

                    className="btn btn-danger"

                    onClick={onCancel}

                >

                    Cancel

                </button>

            </div>

        </div>

    );

}

export default TrialActions;