import React from "react";
import "../../styles/TrialMonitoring.css"

export interface Monitoring {

    monitoring_type: string;

    monitoring_frequency: string;

    remote_monitoring: boolean;

}

interface TrialMonitoringProps {

    monitoring: Monitoring;

    onChange: (monitoring: Monitoring) => void;

}

const monitoringTypes = [

    "Risk Based Monitoring",

    "On Site Monitoring",

    "Central Monitoring",

    "Hybrid Monitoring",

    "Remote Monitoring"

];

const monitoringFrequency = [

    "Weekly",

    "Bi-Weekly",

    "Monthly",

    "Quarterly",

    "As Required"

];

function TrialMonitoring({

    monitoring,

    onChange

}: TrialMonitoringProps) {

    const handleChange = (

        event: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement
        >

    ) => {

        const { name, value } = event.target;

        onChange({

            ...monitoring,

            [name]: value

        });

    };

    const handleCheckbox = (

        event: React.ChangeEvent<HTMLInputElement>

    ) => {

        onChange({

            ...monitoring,

            remote_monitoring: event.target.checked

        });

    };

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Monitoring Information

                </h2>

            </div>

            <div className="monitor-grid">

                <div className="form-group">

                    <label>

                        Monitoring Type

                    </label>

                    <select

                        name="monitoring_type"

                        value={monitoring.monitoring_type}

                        onChange={handleChange}

                    >

                        <option value="">

                            Select

                        </option>

                        {

                            monitoringTypes.map(type => (

                                <option

                                    key={type}

                                    value={type}

                                >

                                    {type}

                                </option>

                            ))

                        }

                    </select>

                </div>

                <div className="form-group">

                    <label>

                        Monitoring Frequency

                    </label>

                    <select

                        name="monitoring_frequency"

                        value={monitoring.monitoring_frequency}

                        onChange={handleChange}

                    >

                        <option value="">

                            Select

                        </option>

                        {

                            monitoringFrequency.map(item => (

                                <option

                                    key={item}

                                    value={item}

                                >

                                    {item}

                                </option>

                            ))

                        }

                    </select>

                </div>

                <div className="checkbox-group">

                    <label>

                        <input

                            type="checkbox"

                            checked={monitoring.remote_monitoring}

                            onChange={handleCheckbox}

                        />

                        Enable Remote Monitoring

                    </label>

                </div>

            </div>

        </div>

    );

}

export default TrialMonitoring;