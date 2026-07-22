import { useState } from "react";
import { useNavigate } from "react-router-dom";

import TrialService from "../services/TrialService";

import type { TrialRequest } from "../models/TrialRequest";

import TrialBasicInfo from "../components/trial/TrialBasicInfo";
import TrialCountries from "../components/trial/TrialCountries";
import TrialSiteTable from "../components/trial/TrialSiteTable";
import TrialRecruitment from "../components/trial/TrialRecruitment";
import TrialMonitoring from "../components/trial/TrialMonitoring";
import TrialBudget from "../components/trial/TrialBudget";
import TrialCompliance from "../components/trial/TrialCompliance";
import TrialObjectives from "../components/trial/TrialObjectives";
import TrialEndpoints from "../components/trial/TrialEndpoints";
import TrialActions from "../components/trial/TrialActions";
import ResponseDashboard from "../response/ResponseDashboard";

import "../styles/ManageTrialPage.css";

const initialForm: TrialRequest = {

    protocol_id: "",

    study_name: "",

    sponsor_name: "",

    therapeutic_area: "",

    indication: "",

    phase: "",

    study_design: "",

    start_date: "",

    end_date: "",

    countries: [],

    sites: [],

    recruitment: {

        target_patients: 0,

        inclusion_criteria: [],

        exclusion_criteria: [],

        recruitment_channels: []

    },

    monitoring: {

        monitoring_type: "",

        monitoring_frequency: "",

        remote_monitoring: false

    },

    budget: {

        total_budget: 0,

        site_budget: 0,

        monitoring_budget: 0,

        recruitment_budget: 0,

        contingency_budget: 0

    },

    compliance: {

        regulatory_authorities: [],

        ich_gcp_required: false,

        audit_required: false

    },

    objectives: [],

    primary_endpoint: "",

    secondary_endpoints: [],

    expected_duration_months: 0,

    created_by: ""

};

function ManageTrialPage() {

    const navigate = useNavigate();

    const [formData, setFormData] =
        useState<TrialRequest>(initialForm);

    const [responseData, setResponseData] = useState<any>(null);

    const [loading, setLoading] =
        useState(false);

    const [message, setMessage] =
        useState("");

    const handleChange = (

        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLTextAreaElement |
            HTMLSelectElement
        >

    ) => {

        const { name, value } = e.target;

        setFormData({

            ...formData,

            [name]: value

        });

    };

    const saveTrial = async () => {

        try {

            setLoading(true);

            console.log(formData);

            const response =
                await TrialService.manageTrial(formData);

            setResponseData(response.data);

            setMessage(response.data.message);

            

        }

        catch (error) {

            console.error(error);

            setMessage("Unable to Save Trial");

        }

        finally {

            setLoading(false);

        }

    };

    const resetForm = () => {

        setFormData(initialForm);

        setMessage("");

    };

    const previewJson = () => {

        console.log(formData);

        alert(

            JSON.stringify(

                formData,

                null,

                2

            )

        );

    };

    const cancel = () => {

        navigate("/");

    };

    return (

        <div className="manage-page">

            <h1>

                Clinical Trial Management

            </h1>

            <TrialBasicInfo

                formData={formData}

                onChange={handleChange}

            />

            <TrialCountries

                countries={formData.countries}

                onCountriesChange={(countries) =>

                    setFormData({

                        ...formData,

                        countries

                    })

                }

            />

            <TrialSiteTable

                sites={formData.sites}

                onChange={(sites) =>

                    setFormData({

                        ...formData,

                        sites

                    })

                }

            />

            <TrialRecruitment

                recruitment={formData.recruitment}

                onChange={(recruitment) =>

                    setFormData({

                        ...formData,

                        recruitment

                    })

                }

            />

            <TrialMonitoring

                monitoring={formData.monitoring}

                onChange={(monitoring) =>

                    setFormData({

                        ...formData,

                        monitoring

                    })

                }

            />

            <TrialBudget

                budget={formData.budget}

                onChange={(budget) =>

                    setFormData({

                        ...formData,

                        budget

                    })

                }

            />

            <TrialCompliance

                compliance={formData.compliance}

                onChange={(compliance) =>

                    setFormData({

                        ...formData,

                        compliance

                    })

                }

            />

            <TrialObjectives

                objectives={formData.objectives}

                onChange={(objectives) =>

                    setFormData({

                        ...formData,

                        objectives

                    })

                }

            />

            <TrialEndpoints

                primaryEndpoint={formData.primary_endpoint}

                secondaryEndpoints={formData.secondary_endpoints}

                onPrimaryChange={(primary_endpoint) =>

                    setFormData({

                        ...formData,

                        primary_endpoint

                    })

                }

                onSecondaryChange={(secondary_endpoints) =>

                    setFormData({

                        ...formData,

                        secondary_endpoints

                    })

                }

            />

            <TrialActions

                loading={loading}

                isEdit={false}

                onSubmit={saveTrial}

                onReset={resetForm}

                onCancel={cancel}

                onPreview={previewJson}

            />

            {/* ===== API RESPONSE START ===== */}

            {responseData && (

                <div className="response-card">

                    <h2>API Response</h2>

                    <ResponseDashboard

                        response={responseData}

                    />

                </div>

            )}

            {/* ===== API RESPONSE END ===== */}

            {message && (

                <div className="message">

                    {message}

                </div>

            )}

        </div>


        

    );

}

export default ManageTrialPage;