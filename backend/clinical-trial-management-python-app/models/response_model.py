from pydantic import BaseModel,Field
from typing import Dict, List, Optional
from datetime import datetime


class StudySetupResponse(BaseModel):
    protocol_summary: str
    


class SiteManagementResponse(BaseModel):
    strategy: str


class RecruitmentManagementResponse(BaseModel):
    strategy: str


class MonitoringManagementResponse(BaseModel):
    strategy: str


class FinanceManagementResponse(BaseModel):
    strategy: str


class ComplianceManagementResponse(BaseModel):
    strategy: str


class TrialMetrics(BaseModel):
    expected_sites: int = 0
    expected_patients: int = 0
    expected_duration_months: int = 0
    estimated_completion_percentage: float = 0.0
    estimated_cost_utilization: float = 0.0


class TrialResponse(BaseModel):

    success: bool = True

    protocol_id: str

    study_name: str

    execution_timestamp: datetime

    study_setup: StudySetupResponse

    site_management: SiteManagementResponse

    recruitment_management: RecruitmentManagementResponse

    monitoring_management: MonitoringManagementResponse

    finance_management: FinanceManagementResponse

    compliance_management: ComplianceManagementResponse

    trial_metrics: Optional[TrialMetrics] = None

    overall_recommendations: List[str] = Field(default_factory=list)

    agent_summary: Dict[str, str]

    message: str = "Clinical Trial Management completed successfully"