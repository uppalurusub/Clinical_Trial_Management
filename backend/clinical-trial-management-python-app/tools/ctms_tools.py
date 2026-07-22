from datetime import datetime
from typing import Dict, List, Any
from utils.logger import logger


class CTMSTools:
    """
    Clinical Trial Management System Tools
    """

    @staticmethod
    def generate_study_timeline(
        start_date: str,
        end_date: str
    ) -> Dict[str, Any]:
        """
        Generate study timeline
        """

        logger.info(
            f"Generating study timeline "
            f"from {start_date} to {end_date}"
        )

        try:

            start = datetime.strptime(
                start_date,
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                end_date,
                "%Y-%m-%d"
            )

            duration_days = (
                end - start
            ).days

            duration_months = round(
                duration_days / 30,
                2
            )

            result = {
                "start_date": start_date,
                "end_date": end_date,
                "duration_days": duration_days,
                "duration_months": duration_months
            }

            logger.success(
                "Timeline generated successfully"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Timeline generation failed: {str(ex)}"
            )

            raise

    @staticmethod
    def calculate_site_enrollment_target(
        total_patients: int,
        total_sites: int
    ) -> Dict[str, Any]:
        """
        Calculate enrollment target per site
        """

        logger.info(
            "Calculating site enrollment target"
        )

        try:

            if total_sites == 0:
                raise ValueError(
                    "Total sites cannot be zero"
                )

            target_per_site = round(
                total_patients / total_sites,
                2
            )

            result = {
                "total_patients": total_patients,
                "total_sites": total_sites,
                "target_per_site": target_per_site
            }

            logger.success(
                "Enrollment target calculated"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Enrollment calculation failed: {str(ex)}"
            )

            raise

    @staticmethod
    def calculate_budget_utilization(
        total_budget: float,
        projected_spend: float
    ) -> Dict[str, Any]:
        """
        Calculate budget utilization
        """

        logger.info(
            "Calculating budget utilization"
        )

        try:

            utilization_pct = round(
                (projected_spend / total_budget) * 100,
                2
            )

            remaining_budget = round(
                total_budget - projected_spend,
                2
            )

            result = {
                "total_budget": total_budget,
                "projected_spend": projected_spend,
                "utilization_percentage": utilization_pct,
                "remaining_budget": remaining_budget
            }

            logger.success(
                "Budget utilization calculated"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Budget calculation failed: {str(ex)}"
            )

            raise

    @staticmethod
    def evaluate_recruitment_status(
        target_patients: int,
        enrolled_patients: int
    ) -> Dict[str, Any]:
        """
        Recruitment progress tracker
        """

        logger.info(
            "Evaluating recruitment status"
        )

        try:

            completion_pct = round(
                (enrolled_patients / target_patients) * 100,
                2
            )

            remaining = (
                target_patients - enrolled_patients
            )

            status = (
                "On Track"
                if completion_pct >= 75
                else "Needs Attention"
            )

            result = {
                "target_patients": target_patients,
                "enrolled_patients": enrolled_patients,
                "remaining_patients": remaining,
                "completion_percentage": completion_pct,
                "status": status
            }

            logger.success(
                "Recruitment status generated"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Recruitment evaluation failed: "
                f"{str(ex)}"
            )

            raise

    @staticmethod
    def assess_trial_risk(
        sites: int,
        patients: int,
        countries: int
    ) -> Dict[str, Any]:
        """
        Simple risk assessment model
        """

        logger.info(
            "Performing trial risk assessment"
        )

        try:

            score = 0

            if sites > 20:
                score += 2

            if patients > 500:
                score += 2

            if countries > 5:
                score += 2

            if score <= 2:
                level = "Low"

            elif score <= 4:
                level = "Medium"

            else:
                level = "High"

            result = {
                "risk_score": score,
                "risk_level": level
            }

            logger.success(
                f"Risk level: {level}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Risk assessment failed: "
                f"{str(ex)}"
            )

            raise

    @staticmethod
    def generate_kpis(
        protocol_id: str,
        total_sites: int,
        total_patients: int,
        budget: float
    ) -> Dict[str, Any]:
        """
        Trial KPI generator
        """

        logger.info(
            f"Generating KPIs for "
            f"{protocol_id}"
        )

        try:

            result = {
                "protocol_id": protocol_id,
                "total_sites": total_sites,
                "total_patients": total_patients,
                "budget": budget,
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "KPIs generated successfully"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"KPI generation failed: "
                f"{str(ex)}"
            )

            raise

    @staticmethod
    def generate_trial_dashboard(
        protocol_id: str,
        enrolled_patients: int,
        target_patients: int,
        budget_utilization: float
    ) -> Dict[str, Any]:
        """
        Dashboard summary
        """

        logger.info(
            f"Generating dashboard "
            f"for {protocol_id}"
        )

        try:

            dashboard = {
                "protocol_id": protocol_id,
                "enrollment_progress": round(
                    (
                        enrolled_patients
                        / target_patients
                    ) * 100,
                    2
                ),
                "budget_utilization": budget_utilization,
                "status": "ACTIVE",
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "Dashboard generated"
            )

            return dashboard

        except Exception as ex:

            logger.exception(
                f"Dashboard generation failed: "
                f"{str(ex)}"
            )

            raise

    @staticmethod
    def validate_protocol(
        protocol_id: str
    ) -> Dict[str, Any]:
        """
        Protocol validation
        """

        logger.info(
            f"Validating protocol "
            f"{protocol_id}"
        )

        try:

            is_valid = protocol_id.startswith(
                "PROTO"
            )

            result = {
                "protocol_id": protocol_id,
                "is_valid": is_valid,
                "validation_timestamp":
                datetime.utcnow().isoformat()
            }

            logger.success(
                "Protocol validation completed"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Protocol validation failed: "
                f"{str(ex)}"
            )

            raise