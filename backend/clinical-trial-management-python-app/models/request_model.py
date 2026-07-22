from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class SiteInformation(BaseModel):
    site_id: str
    site_name: str
    country: str
    city: str
    principal_investigator: str
    target_enrollment: int


class BudgetInformation(BaseModel):
    total_budget: float
    site_budget: float
    monitoring_budget: float
    recruitment_budget: float
    contingency_budget: float


class RecruitmentInformation(BaseModel):
    target_patients: int
    inclusion_criteria: List[str]
    exclusion_criteria: List[str]
    recruitment_channels: List[str]


class MonitoringInformation(BaseModel):
    monitoring_type: str = Field(
        default="Risk Based Monitoring"
    )
    monitoring_frequency: str = Field(
        default="Monthly"
    )
    remote_monitoring: bool = True


class ComplianceInformation(BaseModel):
    regulatory_authorities: List[str]
    ich_gcp_required: bool = True
    audit_required: bool = True


class TrialRequest(BaseModel):

    protocol_id: str
    study_name: str
    sponsor_name: str

    therapeutic_area: str

    indication: str

    phase: str

    study_design: str

    start_date: date

    end_date: date

    countries: List[str]

    sites: List[SiteInformation]

    recruitment: RecruitmentInformation

    monitoring: MonitoringInformation

    budget: BudgetInformation

    compliance: ComplianceInformation

    objectives: List[str]

    primary_endpoint: str

    secondary_endpoints: List[str]

    expected_duration_months: int

    created_by: str