from datetime import datetime
from typing import Dict, List, Any

from utils.logger import logger


class ComplianceTools:
    """
    Clinical Trial Compliance and Regulatory Tools
    """

    @staticmethod
    def evaluate_ich_gcp_compliance(
        completed_trainings: int,
        total_required_trainings: int
    ) -> Dict[str, Any]:
        """
        Evaluate ICH-GCP compliance status
        """

        logger.info(
            "Evaluating ICH-GCP compliance"
        )

        try:

            compliance_percentage = round(
                (
                    completed_trainings /
                    total_required_trainings
                ) * 100,
                2
            ) if total_required_trainings > 0 else 0

            status = (
                "Compliant"
                if compliance_percentage >= 95
                else "Needs Attention"
            )

            result = {
                "completed_trainings": completed_trainings,
                "required_trainings": total_required_trainings,
                "compliance_percentage": compliance_percentage,
                "status": status,
                "evaluated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "ICH-GCP compliance evaluation completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"ICH-GCP compliance evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def assess_protocol_deviations(
        major_deviations: int,
        minor_deviations: int
    ) -> Dict[str, Any]:
        """
        Protocol deviation assessment
        """

        logger.info(
            "Assessing protocol deviations"
        )

        try:

            risk_score = (
                major_deviations * 5
            ) + (
                minor_deviations * 2
            )

            if risk_score <= 10:
                risk_level = "Low"
            elif risk_score <= 25:
                risk_level = "Medium"
            else:
                risk_level = "High"

            result = {
                "major_deviations": major_deviations,
                "minor_deviations": minor_deviations,
                "risk_score": risk_score,
                "risk_level": risk_level
            }

            logger.success(
                "Protocol deviation assessment completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Protocol deviation assessment failed: {str(ex)}"
            )
            raise

    @staticmethod
    def generate_capa_plan(
        issue_id: str,
        root_cause: str,
        corrective_action: str,
        preventive_action: str
    ) -> Dict[str, Any]:
        """
        Generate CAPA plan
        """

        logger.info(
            f"Generating CAPA plan for {issue_id}"
        )

        try:

            result = {
                "issue_id": issue_id,
                "root_cause": root_cause,
                "corrective_action": corrective_action,
                "preventive_action": preventive_action,
                "status": "Open",
                "created_at": datetime.utcnow().isoformat()
            }

            logger.success(
                f"CAPA plan generated for {issue_id}"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"CAPA plan generation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def evaluate_audit_readiness(
        completed_documents: int,
        required_documents: int
    ) -> Dict[str, Any]:
        """
        Audit readiness assessment
        """

        logger.info(
            "Evaluating audit readiness"
        )

        try:

            readiness_pct = round(
                (
                    completed_documents /
                    required_documents
                ) * 100,
                2
            ) if required_documents > 0 else 0

            status = (
                "Ready"
                if readiness_pct >= 95
                else "Not Ready"
            )

            result = {
                "completed_documents": completed_documents,
                "required_documents": required_documents,
                "readiness_percentage": readiness_pct,
                "status": status
            }

            logger.success(
                "Audit readiness evaluation completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Audit readiness evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def evaluate_tmf_completeness(
        available_documents: int,
        expected_documents: int
    ) -> Dict[str, Any]:
        """
        TMF completeness check
        """

        logger.info(
            "Evaluating TMF completeness"
        )

        try:

            completeness_pct = round(
                (
                    available_documents /
                    expected_documents
                ) * 100,
                2
            ) if expected_documents > 0 else 0

            result = {
                "available_documents": available_documents,
                "expected_documents": expected_documents,
                "completeness_percentage": completeness_pct,
                "status": (
                    "Complete"
                    if completeness_pct >= 95
                    else "Incomplete"
                )
            }

            logger.success(
                "TMF completeness evaluation completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"TMF completeness evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def assess_regulatory_risk(
        open_findings: int,
        overdue_capa: int,
        critical_findings: int
    ) -> Dict[str, Any]:
        """
        Regulatory risk assessment
        """

        logger.info(
            "Assessing regulatory risk"
        )

        try:

            score = (
                open_findings * 2 +
                overdue_capa * 3 +
                critical_findings * 5
            )

            if score <= 10:
                risk_level = "Low"
            elif score <= 25:
                risk_level = "Medium"
            else:
                risk_level = "High"

            result = {
                "risk_score": score,
                "risk_level": risk_level
            }

            logger.success(
                "Regulatory risk assessment completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Regulatory risk assessment failed: {str(ex)}"
            )
            raise

    @staticmethod
    def evaluate_inspection_readiness(
        training_completion_pct: float,
        tmf_completeness_pct: float,
        capa_closure_pct: float
    ) -> Dict[str, Any]:
        """
        Inspection readiness evaluation
        """

        logger.info(
            "Evaluating inspection readiness"
        )

        try:

            readiness_score = round(
                (
                    training_completion_pct +
                    tmf_completeness_pct +
                    capa_closure_pct
                ) / 3,
                2
            )

            status = (
                "Ready"
                if readiness_score >= 90
                else "Needs Preparation"
            )

            result = {
                "readiness_score": readiness_score,
                "status": status
            }

            logger.success(
                "Inspection readiness evaluation completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Inspection readiness evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def generate_compliance_dashboard(
        protocol_id: str,
        audit_status: str,
        tmf_completeness: float,
        open_findings: int
    ) -> Dict[str, Any]:
        """
        Compliance dashboard
        """

        logger.info(
            f"Generating compliance dashboard for {protocol_id}"
        )

        try:

            dashboard = {
                "protocol_id": protocol_id,
                "audit_status": audit_status,
                "tmf_completeness": tmf_completeness,
                "open_findings": open_findings,
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "Compliance dashboard generated"
            )

            return dashboard

        except Exception as ex:
            logger.exception(
                f"Compliance dashboard generation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def check_regulatory_authority_compliance(
        authority: str
    ) -> Dict[str, Any]:
        """
        Regulatory authority compliance check
        """

        logger.info(
            f"Checking compliance for {authority}"
        )

        try:

            supported_authorities = [
                "FDA",
                "EMA",
                "MHRA",
                "CDSCO",
                "PMDA",
                "TGA"
            ]

            status = (
                "Supported"
                if authority.upper() in supported_authorities
                else "Not Supported"
            )

            result = {
                "authority": authority,
                "status": status,
                "checked_at": datetime.utcnow().isoformat()
            }

            logger.success(
                f"Compliance check completed for {authority}"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Authority compliance check failed: {str(ex)}"
            )
            raise