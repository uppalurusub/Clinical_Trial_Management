"""
request_form.py

Clinical Trial Management System

Streamlit Manage Trial Request Form

Responsibilities
----------------
1. Render TrialRequest form
2. Collect clinical trial information
3. Collect country and site information
4. Collect recruitment strategy
5. Collect monitoring configuration
6. Collect trial budget
7. Collect compliance configuration
8. Collect objectives and endpoints
9. Build FastAPI TrialRequest payload
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Tuple

import streamlit as st


# ============================================================
# TYPE ALIASES
# ============================================================

JsonDict = Dict[str, Any]


# ============================================================
# CONSTANTS
# ============================================================

TRIAL_PHASES = [
    "Phase I",
    "Phase II",
    "Phase III",
    "Phase IV",
]

THERAPEUTIC_AREAS = [
    "Cardiology",
    "Endocrinology",
    "Oncology",
    "Neurology",
    "Immunology",
    "Respiratory",
    "Gastroenterology",
    "Infectious Diseases",
    "Rare Diseases",
    "Other",
]

MONITORING_TYPES = [
    "Risk Based Monitoring",
    "Traditional Monitoring",
    "Centralized Monitoring",
    "Hybrid Monitoring",
]

MONITORING_FREQUENCIES = [
    "Weekly",
    "Bi-Weekly",
    "Monthly",
    "Quarterly",
]

COUNTRY_OPTIONS = [
    "India",
    "United States",
    "Germany",
    "United Kingdom",
    "Canada",
    "France",
    "Italy",
    "Spain",
    "Australia",
    "Japan",
    "Singapore",
]

REGULATORY_AUTHORITIES = [
    "FDA",
    "EMA",
    "MHRA",
    "CDSCO",
    "Health Canada",
    "TGA",
    "PMDA",
]


# ============================================================
# DEFAULT DATA
# ============================================================

DEFAULT_SITES = [
    {
        "site_id": "SITE-IND-001",
        "site_name": "Apollo Hospitals",
        "country": "India",
        "city": "Hyderabad",
        "principal_investigator": "Dr. Ramesh Kumar",
        "target_enrollment": 100,
    },
    {
        "site_id": "SITE-USA-001",
        "site_name": "Mayo Clinic",
        "country": "United States",
        "city": "Rochester",
        "principal_investigator": "Dr. John Smith",
        "target_enrollment": 150,
    },
    {
        "site_id": "SITE-GER-001",
        "site_name": "Charite University Hospital",
        "country": "Germany",
        "city": "Berlin",
        "principal_investigator": "Dr. Michael Weber",
        "target_enrollment": 125,
    },
    {
        "site_id": "SITE-UK-001",
        "site_name": "King's College Hospital",
        "country": "United Kingdom",
        "city": "London",
        "principal_investigator": "Dr. Sarah Johnson",
        "target_enrollment": 125,
    },
]


DEFAULT_INCLUSION_CRITERIA = """
Age between 18 and 75 years
Diagnosed with Type 2 Diabetes Mellitus
HbA1c between 7.0% and 10.5%
BMI between 25 and 40 kg/m2
Ability to provide informed consent
""".strip()


DEFAULT_EXCLUSION_CRITERIA = """
Type 1 Diabetes
Pregnant or breastfeeding women
History of severe cardiovascular disease
Severe renal impairment
Participation in another clinical trial within 30 days
""".strip()


DEFAULT_RECRUITMENT_CHANNELS = """
Hospital Referrals
Physician Networks
Digital Advertising
Patient Registries
Social Media Campaigns
""".strip()


DEFAULT_OBJECTIVES = """
Evaluate efficacy of GLP-1RA compared with placebo
Assess long-term safety profile
Evaluate impact on HbA1c reduction
Assess effect on body weight reduction
""".strip()


DEFAULT_SECONDARY_ENDPOINTS = """
Body Weight Reduction
Fasting Plasma Glucose Improvement
Incidence of Adverse Events
Quality of Life Assessment
Cardiovascular Safety Outcomes
""".strip()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def text_to_list(
    value: str,
) -> List[str]:
    """
    Convert multiline text into a clean list.
    """

    if not value:

        return []

    return [
        item.strip()
        for item in value.splitlines()
        if item.strip()
    ]


def normalize_date(
    value: date,
) -> str:
    """
    Convert date to ISO formatted string.
    """

    return value.isoformat()


def initialize_form_state() -> None:
    """
    Initialize request form session state.
    """

    if "trial_sites" not in st.session_state:

        st.session_state.trial_sites = [
            site.copy()
            for site in DEFAULT_SITES
        ]


# ============================================================
# SITE MANAGEMENT
# ============================================================

def render_sites_section() -> List[JsonDict]:
    """
    Render clinical trial site editor.
    """

    st.subheader(
        "🏥 Clinical Trial Sites"
    )

    st.caption(
        "Configure participating clinical trial sites."
    )

    sites = st.data_editor(
        st.session_state.trial_sites,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="trial_sites_editor",
        column_config={
            "site_id": st.column_config.TextColumn(
                "Site ID",
                required=True,
            ),
            "site_name": st.column_config.TextColumn(
                "Site Name",
                required=True,
            ),
            "country": st.column_config.TextColumn(
                "Country",
                required=True,
            ),
            "city": st.column_config.TextColumn(
                "City",
            ),
            "principal_investigator":
                st.column_config.TextColumn(
                    "Principal Investigator",
                ),
            "target_enrollment":
                st.column_config.NumberColumn(
                    "Target Enrollment",
                    min_value=0,
                    step=1,
                    format="%d",
                ),
        },
    )

    return [
        {
            "site_id": str(
                site.get(
                    "site_id",
                    "",
                )
            ).strip(),
            "site_name": str(
                site.get(
                    "site_name",
                    "",
                )
            ).strip(),
            "country": str(
                site.get(
                    "country",
                    "",
                )
            ).strip(),
            "city": str(
                site.get(
                    "city",
                    "",
                )
            ).strip(),
            "principal_investigator": str(
                site.get(
                    "principal_investigator",
                    "",
                )
            ).strip(),
            "target_enrollment": int(
                site.get(
                    "target_enrollment",
                    0,
                )
                or 0
            ),
        }
        for site in sites
        if site.get("site_id")
        or site.get("site_name")
    ]


# ============================================================
# MANAGE TRIAL FORM
# ============================================================

def render_manage_trial_form(
) -> Tuple[JsonDict, bool]:
    """
    Render Clinical Trial Manage Trial form.

    Returns
    -------
    Tuple[Dict, bool]

    payload:
        FastAPI TrialRequest payload.

    submitted:
        True when Manage Trial button is clicked.
    """

    initialize_form_state()

    # ========================================================
    # BASIC TRIAL INFORMATION
    # ========================================================

    st.subheader(
        "🧪 Basic Trial Information"
    )

    col1, col2 = st.columns(2)

    with col1:

        protocol_id = st.text_input(
            "Protocol ID *",
            value="PROTO-DM-2026-001",
            key="trial_protocol_id",
        )

        sponsor_name = st.text_input(
            "Sponsor Name *",
            value="ABC Pharma Ltd",
            key="trial_sponsor_name",
        )

        indication = st.text_input(
            "Indication",
            value="Type 2 Diabetes Mellitus",
            key="trial_indication",
        )

        phase = st.selectbox(
            "Trial Phase",
            options=TRIAL_PHASES,
            index=2,
            key="trial_phase",
        )

    with col2:

        study_name = st.text_area(
            "Study Name *",
            value=(
                "A Multicenter Phase III Study "
                "Evaluating the Safety and Efficacy "
                "of GLP-1RA in Type 2 Diabetes Mellitus"
            ),
            height=100,
            key="trial_study_name",
        )

        therapeutic_area = st.selectbox(
            "Therapeutic Area",
            options=THERAPEUTIC_AREAS,
            index=1,
            key="trial_therapeutic_area",
        )

        study_design = st.text_area(
            "Study Design",
            value=(
                "Randomized Double-Blind "
                "Placebo-Controlled Multicenter Study"
            ),
            height=100,
            key="trial_study_design",
        )

    st.divider()

    # ========================================================
    # TRIAL TIMELINE
    # ========================================================

    st.subheader(
        "📅 Trial Timeline"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        start_date = st.date_input(
            "Start Date",
            value=date(
                2026,
                7,
                1,
            ),
            key="trial_start_date",
        )

    with col2:

        end_date = st.date_input(
            "End Date",
            value=date(
                2028,
                6,
                30,
            ),
            key="trial_end_date",
        )

    with col3:

        expected_duration_months = (
            st.number_input(
                "Expected Duration (Months)",
                min_value=1,
                value=24,
                step=1,
                key="trial_duration_months",
            )
        )

    st.divider()

    # ========================================================
    # COUNTRIES
    # ========================================================

    st.subheader(
        "🌍 Participating Countries"
    )

    countries = st.multiselect(
        "Countries",
        options=COUNTRY_OPTIONS,
        default=[
            "India",
            "United States",
            "Germany",
            "United Kingdom",
        ],
        key="trial_countries",
    )

    st.divider()

    # ========================================================
    # SITES
    # ========================================================

    sites = render_sites_section()

    st.divider()

    # ========================================================
    # RECRUITMENT
    # ========================================================

    st.subheader(
        "👥 Patient Recruitment"
    )

    target_patients = st.number_input(
        "Target Patients",
        min_value=1,
        value=500,
        step=1,
        key="trial_target_patients",
    )

    col1, col2 = st.columns(2)

    with col1:

        inclusion_criteria = st.text_area(
            "Inclusion Criteria",
            value=DEFAULT_INCLUSION_CRITERIA,
            height=180,
            help=(
                "Enter one criterion per line."
            ),
            key="trial_inclusion_criteria",
        )

    with col2:

        exclusion_criteria = st.text_area(
            "Exclusion Criteria",
            value=DEFAULT_EXCLUSION_CRITERIA,
            height=180,
            help=(
                "Enter one criterion per line."
            ),
            key="trial_exclusion_criteria",
        )

    recruitment_channels = st.text_area(
        "Recruitment Channels",
        value=DEFAULT_RECRUITMENT_CHANNELS,
        height=150,
        help="Enter one channel per line.",
        key="trial_recruitment_channels",
    )

    st.divider()

    # ========================================================
    # MONITORING
    # ========================================================

    st.subheader(
        "🔎 Trial Monitoring"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        monitoring_type = st.selectbox(
            "Monitoring Type",
            options=MONITORING_TYPES,
            key="trial_monitoring_type",
        )

    with col2:

        monitoring_frequency = st.selectbox(
            "Monitoring Frequency",
            options=MONITORING_FREQUENCIES,
            index=2,
            key="trial_monitoring_frequency",
        )

    with col3:

        remote_monitoring = st.checkbox(
            "Remote Monitoring",
            value=True,
            key="trial_remote_monitoring",
        )

    st.divider()

    # ========================================================
    # BUDGET
    # ========================================================

    st.subheader(
        "💰 Trial Budget"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        total_budget = st.number_input(
            "Total Budget",
            min_value=0.0,
            value=15_000_000.0,
            step=100_000.0,
            format="%.2f",
            key="trial_total_budget",
        )

        site_budget = st.number_input(
            "Site Budget",
            min_value=0.0,
            value=8_000_000.0,
            step=100_000.0,
            format="%.2f",
            key="trial_site_budget",
        )

    with col2:

        monitoring_budget = st.number_input(
            "Monitoring Budget",
            min_value=0.0,
            value=2_500_000.0,
            step=100_000.0,
            format="%.2f",
            key="trial_monitoring_budget",
        )

        recruitment_budget = st.number_input(
            "Recruitment Budget",
            min_value=0.0,
            value=3_000_000.0,
            step=100_000.0,
            format="%.2f",
            key="trial_recruitment_budget",
        )

    with col3:

        contingency_budget = st.number_input(
            "Contingency Budget",
            min_value=0.0,
            value=1_500_000.0,
            step=100_000.0,
            format="%.2f",
            key="trial_contingency_budget",
        )

        allocated_budget = (
            site_budget
            + monitoring_budget
            + recruitment_budget
            + contingency_budget
        )

        st.metric(
            "Allocated Budget",
            f"${allocated_budget:,.2f}",
        )

    if allocated_budget > total_budget:

        st.warning(
            "Allocated budget exceeds total budget."
        )

    elif allocated_budget < total_budget:

        st.info(
            "There is unallocated budget remaining: "
            f"${total_budget - allocated_budget:,.2f}"
        )

    else:

        st.success(
            "Budget allocation matches total budget."
        )

    st.divider()

    # ========================================================
    # COMPLIANCE
    # ========================================================

    st.subheader(
        "🛡️ Regulatory Compliance"
    )

    regulatory_authorities = st.multiselect(
        "Regulatory Authorities",
        options=REGULATORY_AUTHORITIES,
        default=[
            "FDA",
            "EMA",
            "MHRA",
            "CDSCO",
        ],
        key="trial_regulatory_authorities",
    )

    col1, col2 = st.columns(2)

    with col1:

        ich_gcp_required = st.checkbox(
            "ICH-GCP Required",
            value=True,
            key="trial_ich_gcp_required",
        )

    with col2:

        audit_required = st.checkbox(
            "Audit Required",
            value=True,
            key="trial_audit_required",
        )

    st.divider()

    # ========================================================
    # OBJECTIVES
    # ========================================================

    st.subheader(
        "🎯 Trial Objectives"
    )

    objectives = st.text_area(
        "Objectives",
        value=DEFAULT_OBJECTIVES,
        height=160,
        help="Enter one objective per line.",
        key="trial_objectives",
    )

    st.divider()

    # ========================================================
    # ENDPOINTS
    # ========================================================

    st.subheader(
        "📈 Clinical Endpoints"
    )

    primary_endpoint = st.text_area(
        "Primary Endpoint",
        value=(
            "Mean Change in HbA1c "
            "from Baseline to Week 52"
        ),
        height=100,
        key="trial_primary_endpoint",
    )

    secondary_endpoints = st.text_area(
        "Secondary Endpoints",
        value=DEFAULT_SECONDARY_ENDPOINTS,
        height=160,
        help=(
            "Enter one secondary endpoint per line."
        ),
        key="trial_secondary_endpoints",
    )

    st.divider()

    # ========================================================
    # REQUEST METADATA
    # ========================================================

    st.subheader(
        "👤 Request Metadata"
    )

    created_by = st.text_input(
        "Created By",
        value=(
            "Clinical Trial Operations Manager"
        ),
        key="trial_created_by",
    )

    st.divider()

    # ========================================================
    # BUILD PAYLOAD
    # ========================================================

    payload: JsonDict = {
        "protocol_id": protocol_id.strip(),
        "study_name": study_name.strip(),
        "sponsor_name": sponsor_name.strip(),
        "therapeutic_area": therapeutic_area,
        "indication": indication.strip(),
        "phase": phase,
        "study_design": study_design.strip(),
        "start_date": normalize_date(
            start_date
        ),
        "end_date": normalize_date(
            end_date
        ),
        "countries": countries,
        "sites": sites,
        "recruitment": {
            "target_patients": int(
                target_patients
            ),
            "inclusion_criteria": text_to_list(
                inclusion_criteria
            ),
            "exclusion_criteria": text_to_list(
                exclusion_criteria
            ),
            "recruitment_channels": text_to_list(
                recruitment_channels
            ),
        },
        "monitoring": {
            "monitoring_type": monitoring_type,
            "monitoring_frequency":
                monitoring_frequency,
            "remote_monitoring":
                remote_monitoring,
        },
        "budget": {
            "total_budget": float(
                total_budget
            ),
            "site_budget": float(
                site_budget
            ),
            "monitoring_budget": float(
                monitoring_budget
            ),
            "recruitment_budget": float(
                recruitment_budget
            ),
            "contingency_budget": float(
                contingency_budget
            ),
        },
        "compliance": {
            "regulatory_authorities":
                regulatory_authorities,
            "ich_gcp_required":
                ich_gcp_required,
            "audit_required":
                audit_required,
        },
        "objectives": text_to_list(
            objectives
        ),
        "primary_endpoint":
            primary_endpoint.strip(),
        "secondary_endpoints":
            text_to_list(
                secondary_endpoints
            ),
        "expected_duration_months": int(
            expected_duration_months
        ),
        "created_by": created_by.strip(),
    }

    # ========================================================
    # FORM ACTIONS
    # ========================================================

    col1, col2 = st.columns(
        [3, 1]
    )

    with col1:

        submitted = st.button(
            "🚀 Manage Trial",
            type="primary",
            use_container_width=True,
            key="manage_trial_submit_button",
        )

    with col2:

        preview = st.button(
            "👁️ Preview",
            use_container_width=True,
            key="manage_trial_preview_button",
        )

    if preview:

        with st.expander(
            "📤 TrialRequest Payload",
            expanded=True,
        ):

            st.json(
                payload
            )

    return (
        payload,
        submitted,
    )