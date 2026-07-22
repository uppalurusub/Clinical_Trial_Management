import React from "react";

import "../../styles/TrialBudget.css"

export interface Budget {

    total_budget: number;

    site_budget: number;

    monitoring_budget: number;

    recruitment_budget: number;

    contingency_budget: number;

}

interface TrialBudgetProps {

    budget: Budget;

    onChange: (budget: Budget) => void;

}

function TrialBudget({

    budget,

    onChange

}: TrialBudgetProps) {

    const handleChange = (

        e: React.ChangeEvent<HTMLInputElement>

    ) => {

        const { name, value } = e.target;

        onChange({

            ...budget,

            [name]: Number(value)

        });

    };

    const totalAllocated =

        budget.site_budget +

        budget.monitoring_budget +

        budget.recruitment_budget +

        budget.contingency_budget;

    const remainingBudget =

        budget.total_budget -

        totalAllocated;

    return (

        <div className="card">

            <div className="card-header">

                <h2>

                    Trial Budget

                </h2>

            </div>

            <div className="budget-grid">

                <div className="form-group">

                    <label>Total Budget</label>

                    <input
                        type="number"
                        name="total_budget"
                        value={budget.total_budget}
                        onChange={handleChange}
                    />

                </div>

                <div className="form-group">

                    <label>Site Budget</label>

                    <input
                        type="number"
                        name="site_budget"
                        value={budget.site_budget}
                        onChange={handleChange}
                    />

                </div>

                <div className="form-group">

                    <label>Monitoring Budget</label>

                    <input
                        type="number"
                        name="monitoring_budget"
                        value={budget.monitoring_budget}
                        onChange={handleChange}
                    />

                </div>

                <div className="form-group">

                    <label>Recruitment Budget</label>

                    <input
                        type="number"
                        name="recruitment_budget"
                        value={budget.recruitment_budget}
                        onChange={handleChange}
                    />

                </div>

                <div className="form-group">

                    <label>Contingency Budget</label>

                    <input
                        type="number"
                        name="contingency_budget"
                        value={budget.contingency_budget}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div className="budget-summary">

                <div className="summary-card">

                    <h4>Total Budget</h4>

                    <span>

                        ${budget.total_budget.toLocaleString()}

                    </span>

                </div>

                <div className="summary-card">

                    <h4>Allocated Budget</h4>

                    <span>

                        ${totalAllocated.toLocaleString()}

                    </span>

                </div>

                <div className="summary-card">

                    <h4>Remaining Budget</h4>

                    <span
                        className={
                            remainingBudget >= 0
                                ? "positive"
                                : "negative"
                        }
                    >

                        ${remainingBudget.toLocaleString()}

                    </span>

                </div>

            </div>

        </div>

    );

}

export default TrialBudget;