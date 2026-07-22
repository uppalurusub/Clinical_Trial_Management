import { ChangeEvent, FormEvent, useState } from "react";

import type { TrialRequest } from "../../models/TrialRequest";
import useTrials from "../../hooks/useTrials";

import TrialActions from "./TrialActions";
import TrialBasicInfo from "./TrialBasicInfo";
import TrialBudget from "./TrialBudget";
import TrialCompliance from "./TrialCompliance";
import TrialCountries from "./TrialCountries";
import TrialEndpoints from "./TrialEndpoints";
import TrialMonitoring from "./TrialMonitoring";
import TrialObjectives from "./TrialObjectives";
import TrialRecruitment from "./TrialRecruitment";
import TrialSiteTable from "./TrialSiteTable";

const initialState: TrialRequest = {
  protocol_id: "PROTO-DM-2026-001",
  study_name:
    "A Multicenter Phase III Study Evaluating the Safety and Efficacy of GLP-1RA in Type 2 Diabetes Mellitus",
  sponsor_name: "ABC Pharma Ltd",
  therapeutic_area: "Endocrinology",
  indication: "Type 2 Diabetes Mellitus",
  phase: "Phase III",
  study_design:
    "Randomized Double-Blind Placebo-Controlled Multicenter Study",
  start_date: "2026-07-01",
  end_date: "2028-06-30",

  countries: [
    "India",
    "United States",
    "Germany",
    "United Kingdom",
  ],

  sites: [
    {
      site_id: "SITE-IND-001",
      site_name: "Apollo Hospitals",
      country: "India",
      city: "Hyderabad",
      principal_investigator: "Dr. Ramesh Kumar",
      target_enrollment: 100,
    },
    {
      site_id: "SITE-USA-001",
      site_name: "Mayo Clinic",
      country: "United States",
      city: "Rochester",
      principal_investigator: "Dr. John Smith",
      target_enrollment: 150,
    },
    {
      site_id: "SITE-GER-001",
      site_name: "Charite University Hospital",
      country: "Germany",
      city: "Berlin",
      principal_investigator: "Dr. Michael Weber",
      target_enrollment: 125,
    },
    {
      site_id: "SITE-UK-001",
      site_name: "King's College Hospital",
      country: "United Kingdom",
      city: "London",
      principal_investigator: "Dr. Sarah Johnson",
      target_enrollment: 125,
    },
  ],

  recruitment: {
    target_patients: 500,
    inclusion_criteria: [
      "Age between 18 and 75 years",
      "Diagnosed with Type 2 Diabetes Mellitus",
      "HbA1c between 7.0% and 10.5%",
      "BMI between 25 and 40 kg/m2",
      "Ability to provide informed consent",
    ],
    exclusion_criteria: [
      "Type 1 Diabetes",
      "Pregnant or breastfeeding women",
      "History of severe cardiovascular disease",
      "Severe renal impairment",
      "Participation in another clinical trial within 30 days",
    ],
    recruitment_channels: [
      "Hospital Referrals",
      "Physician Networks",
      "Digital Advertising",
      "Patient Registries",
      "Social Media Campaigns",
    ],
  },

  monitoring: {
    monitoring_type: "Risk Based Monitoring",
    monitoring_frequency: "Monthly",
    remote_monitoring: true,
  },

  budget: {
    total_budget: 15000000,
    site_budget: 8000000,
    monitoring_budget: 2500000,
    recruitment_budget: 3000000,
    contingency_budget: 1500000,
  },

  compliance: {
    regulatory_authorities: ["FDA", "EMA", "MHRA", "CDSCO"],
    ich_gcp_required: true,
    audit_required: true,
  },

  objectives: [
    "Evaluate efficacy of GLP-1RA compared with placebo",
    "Assess long-term safety profile",
    "Evaluate impact on HbA1c reduction",
    "Assess effect on body weight reduction",
  ],

  primary_endpoint:
    "Mean Change in HbA1c from Baseline to Week 52",

  secondary_endpoints: [
    "Body Weight Reduction",
    "Fasting Plasma Glucose Improvement",
    "Incidence of Adverse Events",
    "Quality of Life Assessment",
    "Cardiovascular Safety Outcomes",
  ],

  expected_duration_months: 24,
  created_by: "Clinical Trial Operations Manager",
};

const cloneInitialState = (): TrialRequest =>
  JSON.parse(JSON.stringify(initialState)) as TrialRequest;

const TrialForm = () => {
  const { saveTrial, loading } = useTrials();

  const [formData, setFormData] =
    useState<TrialRequest>(cloneInitialState());

  const handleBasicInfoChange = (
    e: ChangeEvent<
      HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement
    >
  ) => {
    const { name, value, type } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: type === "number" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (
    e?: FormEvent<HTMLFormElement>
  ) => {
    e?.preventDefault();

    const success = await saveTrial(formData);

    if (success) {
      alert("Clinical Trial saved successfully.");
    }
  };

  const handleReset = () => {
    setFormData(cloneInitialState());
  };

  const handleCancel = () => {
    setFormData(cloneInitialState());
  };

  const handlePreview = () => {
    alert(JSON.stringify(formData, null, 2));
  };

  return (
    <form onSubmit={handleSubmit}>
      <TrialBasicInfo
        formData={formData}
        onChange={handleBasicInfoChange}
      />

      <TrialCountries
        countries={formData.countries}
        onCountriesChange={(countries) =>
          setFormData((prev) => ({ ...prev, countries }))
        }
      />

      <TrialSiteTable
        sites={formData.sites}
        onChange={(sites) =>
          setFormData((prev) => ({ ...prev, sites }))
        }
      />

      <TrialRecruitment
        recruitment={formData.recruitment}
        onChange={(recruitment) =>
          setFormData((prev) => ({ ...prev, recruitment }))
        }
      />

      <TrialMonitoring
        monitoring={formData.monitoring}
        onChange={(monitoring) =>
          setFormData((prev) => ({ ...prev, monitoring }))
        }
      />

      <TrialBudget
        budget={formData.budget}
        onChange={(budget) =>
          setFormData((prev) => ({ ...prev, budget }))
        }
      />

      <TrialCompliance
        compliance={formData.compliance}
        onChange={(compliance) =>
          setFormData((prev) => ({ ...prev, compliance }))
        }
      />

      <TrialObjectives
        objectives={formData.objectives}
        onChange={(objectives) =>
          setFormData((prev) => ({ ...prev, objectives }))
        }
      />

      <TrialEndpoints
        primaryEndpoint={formData.primary_endpoint}
        secondaryEndpoints={formData.secondary_endpoints}
        onPrimaryChange={(primary_endpoint) =>
          setFormData((prev) => ({ ...prev, primary_endpoint }))
        }
        onSecondaryChange={(secondary_endpoints) =>
          setFormData((prev) => ({ ...prev, secondary_endpoints }))
        }
      />

      <TrialActions
        loading={loading}
        isEdit={false}
        onSubmit={() => void handleSubmit()}
        onReset={handleReset}
        onCancel={handleCancel}
        onPreview={handlePreview}
      />
    </form>
  );
};

export default TrialForm;
