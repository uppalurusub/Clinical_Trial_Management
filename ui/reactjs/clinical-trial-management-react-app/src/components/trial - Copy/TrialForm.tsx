import { useState, ChangeEvent, FormEvent } from "react";

import type { TrialRequest } from "../../models/TrialRequest";
import useTrials from "../../hooks/useTrials";

import {
  TRIAL_PHASES,
  TRIAL_STATUS,
  STUDY_TYPES,
  THERAPEUTIC_AREAS,
  REGULATORY_STATUS,
  COUNTRIES,
} from "../../utils/constants";

const initialState: TrialRequest = {
  protocol_id: "",
  trial_name: "",
  sponsor: "",
  indication: "",
  phase: "",
  status: "",
  therapeutic_area: "",
  study_type: "",
  start_date: "",
  end_date: "",
  planned_subjects: 0,
  enrolled_subjects: 0,
  principal_investigator: "",
  study_site: "",
  country: "",
  regulatory_status: "",
  ethics_approval: false,
  description: "",
};

const TrialForm = () => {
  const { saveTrial, loading } = useTrials();

  const [formData, setFormData] =
    useState<TrialRequest>(initialState);

  const handleChange = (
    e: ChangeEvent<
      HTMLInputElement |
      HTMLSelectElement |
      HTMLTextAreaElement
    >
  ) => {

    const { name, value, type } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]:
        type === "checkbox"
          ? (e.target as HTMLInputElement).checked
          : type === "number"
          ? Number(value)
          : value,
    }));
  };

  const handleSubmit = async (
    e: FormEvent<HTMLFormElement>
  ) => {

    e.preventDefault();

    const success =
      await saveTrial(formData);

    if (success) {

      alert(
        "Clinical Trial saved successfully."
      );

      setFormData(initialState);

    }

  };

  return (

    <form onSubmit={handleSubmit}>

      <div className="row">

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Protocol ID
          </label>

          <input
            type="text"
            name="protocol_id"
            value={formData.protocol_id}
            onChange={handleChange}
            className="form-control"
            required
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Trial Name
          </label>

          <input
            type="text"
            name="trial_name"
            value={formData.trial_name}
            onChange={handleChange}
            className="form-control"
            required
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Sponsor
          </label>

          <input
            type="text"
            name="sponsor"
            value={formData.sponsor}
            onChange={handleChange}
            className="form-control"
            required
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Indication
          </label>

          <input
            type="text"
            name="indication"
            value={formData.indication}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Therapeutic Area
          </label>

          <select
            name="therapeutic_area"
            value={formData.therapeutic_area}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {THERAPEUTIC_AREAS.map(area => (

              <option
                key={area}
                value={area}
              >
                {area}
              </option>

            ))}

          </select>

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Phase
          </label>

          <select
            name="phase"
            value={formData.phase}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {TRIAL_PHASES.map(phase => (

              <option
                key={phase}
                value={phase}
              >
                {phase}
              </option>

            ))}

          </select>

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Study Type
          </label>

          <select
            name="study_type"
            value={formData.study_type}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {STUDY_TYPES.map(type => (

              <option
                key={type}
                value={type}
              >
                {type}
              </option>

            ))}

          </select>

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Status
          </label>

          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {TRIAL_STATUS.map(status => (

              <option
                key={status}
                value={status}
              >
                {status}
              </option>

            ))}

          </select>

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Planned Subjects
          </label>

          <input
            type="number"
            name="planned_subjects"
            value={formData.planned_subjects}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Enrolled Subjects
          </label>

          <input
            type="number"
            name="enrolled_subjects"
            value={formData.enrolled_subjects}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Start Date
          </label>

          <input
            type="date"
            name="start_date"
            value={formData.start_date}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            End Date
          </label>

          <input
            type="date"
            name="end_date"
            value={formData.end_date}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Principal Investigator
          </label>

          <input
            type="text"
            name="principal_investigator"
            value={formData.principal_investigator}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Study Site
          </label>

          <input
            type="text"
            name="study_site"
            value={formData.study_site}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Country
          </label>

          <select
            name="country"
            value={formData.country}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {COUNTRIES.map(country => (

              <option
                key={country}
                value={country}
              >
                {country}
              </option>

            ))}

          </select>

        </div>

        <div className="col-md-6 mb-3">

          <label className="form-label">
            Regulatory Status
          </label>

          <select
            name="regulatory_status"
            value={formData.regulatory_status}
            onChange={handleChange}
            className="form-select"
          >

            <option value="">
              Select
            </option>

            {REGULATORY_STATUS.map(status => (

              <option
                key={status}
                value={status}
              >
                {status}
              </option>

            ))}

          </select>

        </div>

        <div className="col-12 mb-3">

          <label className="form-label">
            Description
          </label>

          <textarea
            name="description"
            rows={4}
            value={formData.description}
            onChange={handleChange}
            className="form-control"
          />

        </div>

        <div className="col-12 mb-4">

          <div className="form-check">

            <input
              type="checkbox"
              className="form-check-input"
              id="ethics_approval"
              name="ethics_approval"
              checked={formData.ethics_approval}
              onChange={handleChange}
            />

            <label
              className="form-check-label"
              htmlFor="ethics_approval"
            >
              Ethics Committee Approved
            </label>

          </div>

        </div>

        <div className="col-12">

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading}
          >

            {loading
              ? "Saving..."
              : "Save Clinical Trial"}

          </button>

        </div>

      </div>

    </form>

  );
};

export default TrialForm;

