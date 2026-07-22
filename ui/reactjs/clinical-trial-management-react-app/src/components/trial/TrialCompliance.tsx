import React from "react";

import "../../styles/TrialCompliance.css"

export interface Compliance {

    regulatory_authorities: string[];

    ich_gcp_required: boolean;

    audit_required: boolean;

}

interface TrialComplianceProps {

    compliance: Compliance;

    onChange: (compliance: Compliance) => void;

}

const authorities = [

    "FDA",

    "EMA",

    "MHRA",

    "CDSCO",

    "PMDA",

    "Health Canada",

    "TGA",

    "NMPA"

];

function TrialCompliance({

    compliance,

    onChange

}: TrialComplianceProps) {

    const handleAuthorityChange = (

        event: React.ChangeEvent<HTMLSelectElement>

    ) => {

        const values = Array.from(

            event.target.selectedOptions,

            option => option.value

        );

        onChange({

            ...compliance,

            regulatory_authorities: values

        });

    };

    const handleCheckbox = (

        event: React.ChangeEvent<HTMLInputElement>

    ) => {

        const { name, checked } = event.target;

        onChange({

            ...compliance,

            [name]: checked

        });

    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Regulatory Compliance

                </h2>

            </div>

            <div className="form-group">

                <label>

                    Regulatory Authorities

                </label>

                <select

                    multiple

                    size={6}

                    value={compliance.regulatory_authorities}

                    onChange={handleAuthorityChange}

                    className="authority-select"

                >

                    {

                        authorities.map(authority => (

                            <option

                                key={authority}

                                value={authority}

                            >

                                {authority}

                            </option>

                        ))

                    }

                </select>

            </div>

            <div className="checkbox-container">

                <label className="checkbox-item">

                    <input

                        type="checkbox"

                        name="ich_gcp_required"

                        checked={compliance.ich_gcp_required}

                        onChange={handleCheckbox}

                    />

                    ICH-GCP Compliance Required

                </label>

                <label className="checkbox-item">

                    <input

                        type="checkbox"

                        name="audit_required"

                        checked={compliance.audit_required}

                        onChange={handleCheckbox}

                    />

                    Audit Required

                </label>

            </div>

            <div className="selected-authorities">

                <h4>

                    Selected Authorities

                </h4>

                {

                    compliance.regulatory_authorities.length === 0

                    ?

                    <p>No authorities selected.</p>

                    :

                    compliance.regulatory_authorities.map(authority => (

                        <span

                            key={authority}

                            className="authority-chip"

                        >

                            {authority}

                        </span>

                    ))

                }

            </div>

        </div>

    );

}

export default TrialCompliance;