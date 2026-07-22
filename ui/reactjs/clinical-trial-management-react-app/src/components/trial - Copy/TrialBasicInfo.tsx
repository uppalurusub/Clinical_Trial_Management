import React from "react";
import type { TrialRequest } from "../../models/TrialRequest";
import "../../styles/TrialBasicInfo.css"

interface TrialBasicInfoProps {
    formData: TrialRequest;
    onChange: (
        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement |
            HTMLTextAreaElement
        >
    ) => void;
}

const TrialBasicInfo: React.FC<TrialBasicInfoProps> = ({
    formData,
    onChange,
}) => {

    return (

        <div className="card">

            <div className="card-header">

                <h2>Basic Trial Information</h2>

            </div>

            <div className="card-body">

                <div className="form-grid">

                    <div className="form-group">
                        <label>Protocol ID</label>

                        <input
                            type="text"
                            name="protocol_id"
                            value={formData.protocol_id}
                            onChange={onChange}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Sponsor Name</label>

                        <input
                            type="text"
                            name="sponsor_name"
                            value={formData.sponsor_name}
                            onChange={onChange}
                            required
                        />
                    </div>

                    <div className="form-group full-width">

                        <label>Study Name</label>

                        <textarea
                            rows={3}
                            name="study_name"
                            value={formData.study_name}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>Therapeutic Area</label>

                        <select
                            name="therapeutic_area"
                            value={formData.therapeutic_area}
                            onChange={onChange}
                        >

                            <option value="">
                                Select
                            </option>

                            <option>
                                Oncology
                            </option>

                            <option>
                                Cardiology
                            </option>

                            <option>
                                Endocrinology
                            </option>

                            <option>
                                Neurology
                            </option>

                            <option>
                                Immunology
                            </option>

                        </select>

                    </div>

                    <div className="form-group">

                        <label>Indication</label>

                        <input
                            type="text"
                            name="indication"
                            value={formData.indication}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>Phase</label>

                        <select
                            name="phase"
                            value={formData.phase}
                            onChange={onChange}
                        >

                            <option value="">
                                Select
                            </option>

                            <option>
                                Phase I
                            </option>

                            <option>
                                Phase II
                            </option>

                            <option>
                                Phase III
                            </option>

                            <option>
                                Phase IV
                            </option>

                        </select>

                    </div>

                    <div className="form-group full-width">

                        <label>Study Design</label>

                        <textarea
                            rows={3}
                            name="study_design"
                            value={formData.study_design}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>Start Date</label>

                        <input
                            type="date"
                            name="start_date"
                            value={formData.start_date}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>End Date</label>

                        <input
                            type="date"
                            name="end_date"
                            value={formData.end_date}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>Expected Duration (Months)</label>

                        <input
                            type="number"
                            name="expected_duration_months"
                            value={formData.expected_duration_months}
                            onChange={onChange}
                        />

                    </div>

                    <div className="form-group">

                        <label>Created By</label>

                        <input
                            type="text"
                            name="created_by"
                            value={formData.created_by}
                            onChange={onChange}
                        />

                    </div>

                </div>

            </div>

        </div>

    );

};

export default TrialBasicInfo;