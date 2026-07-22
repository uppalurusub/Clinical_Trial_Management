from datetime import datetime
from typing import Dict, List, Any

from utils.logger import logger


class SiteTools:
    """
    Clinical Trial Site Management Tools
    """

    @staticmethod
    def evaluate_site_feasibility(
        site_name: str,
        patient_population: int,
        investigator_experience_years: int,
        previous_trials: int
    ) -> Dict[str, Any]:
        """
        Site feasibility assessment
        """

        logger.info(
            f"Evaluating feasibility for site: {site_name}"
        )

        try:

            score = 0

            if patient_population >= 5000:
                score += 40

            elif patient_population >= 2000:
                score += 25

            else:
                score += 10

            if investigator_experience_years >= 10:
                score += 30

            elif investigator_experience_years >= 5:
                score += 20

            else:
                score += 10

            if previous_trials >= 20:
                score += 30

            elif previous_trials >= 10:
                score += 20

            else:
                score += 10

            feasibility = (
                "High"
                if score >= 80
                else "Medium"
                if score >= 50
                else "Low"
            )

            result = {
                "site_name": site_name,
                "feasibility_score": score,
                "feasibility_rating": feasibility,
                "assessment_date": datetime.utcnow().isoformat()
            }

            logger.success(
                f"Feasibility assessment completed for {site_name}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Site feasibility evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def calculate_site_enrollment_target(
        total_patients: int,
        total_sites: int
    ) -> Dict[str, Any]:
        """
        Calculate patient target per site
        """

        logger.info(
            "Calculating site enrollment target"
        )

        try:

            if total_sites <= 0:
                raise ValueError(
                    "Total sites must be greater than zero"
                )

            target = round(
                total_patients / total_sites,
                2
            )

            result = {
                "total_patients": total_patients,
                "total_sites": total_sites,
                "target_per_site": target
            }

            logger.success(
                "Enrollment target calculation completed"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Enrollment target calculation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def generate_site_activation_plan(
        site_name: str,
        activation_days: int = 60
    ) -> Dict[str, Any]:
        """
        Generate site activation timeline
        """

        logger.info(
            f"Generating activation plan for {site_name}"
        )

        try:

            result = {
                "site_name": site_name,
                "activation_target_days": activation_days,
                "tasks": [
                    "Site Qualification Visit",
                    "Contract Execution",
                    "IRB Approval",
                    "Staff Training",
                    "System Access",
                    "Site Initiation Visit"
                ],
                "status": "Planned"
            }

            logger.success(
                f"Activation plan created for {site_name}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Activation plan generation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def evaluate_site_performance(
        site_name: str,
        target_patients: int,
        enrolled_patients: int,
        screen_failure_rate: float
    ) -> Dict[str, Any]:
        """
        Site performance evaluation
        """

        logger.info(
            f"Evaluating site performance for {site_name}"
        )

        try:

            enrollment_pct = round(
                (enrolled_patients / target_patients) * 100,
                2
            ) if target_patients else 0

            performance = (
                "Excellent"
                if enrollment_pct >= 90
                else "Good"
                if enrollment_pct >= 70
                else "Needs Improvement"
            )

            result = {
                "site_name": site_name,
                "target_patients": target_patients,
                "enrolled_patients": enrolled_patients,
                "screen_failure_rate": screen_failure_rate,
                "enrollment_percentage": enrollment_pct,
                "performance_rating": performance
            }

            logger.success(
                f"Performance evaluation completed for {site_name}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Performance evaluation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def assess_site_risk(
        site_name: str,
        protocol_deviations: int,
        overdue_queries: int,
        missing_documents: int
    ) -> Dict[str, Any]:
        """
        Site risk assessment
        """

        logger.info(
            f"Assessing risk for site {site_name}"
        )

        try:

            score = (
                protocol_deviations * 3
                + overdue_queries * 2
                + missing_documents
            )

            if score <= 10:
                level = "Low"

            elif score <= 25:
                level = "Medium"

            else:
                level = "High"

            result = {
                "site_name": site_name,
                "risk_score": score,
                "risk_level": level
            }

            logger.success(
                f"Risk assessment completed for {site_name}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Risk assessment failed: {str(ex)}"
            )
            raise

    @staticmethod
    def investigator_workload(
        investigator_name: str,
        active_trials: int,
        enrolled_patients: int
    ) -> Dict[str, Any]:
        """
        PI workload analysis
        """

        logger.info(
            f"Analyzing workload for {investigator_name}"
        )

        try:

            workload_score = (
                active_trials * 10
                + enrolled_patients
            )

            status = (
                "Overloaded"
                if workload_score > 150
                else "Balanced"
            )

            result = {
                "investigator_name": investigator_name,
                "active_trials": active_trials,
                "enrolled_patients": enrolled_patients,
                "workload_score": workload_score,
                "status": status
            }

            logger.success(
                f"Workload analysis completed for {investigator_name}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Workload analysis failed: {str(ex)}"
            )
            raise

    @staticmethod
    def rank_sites(
        sites: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Rank sites based on feasibility score
        """

        logger.info(
            f"Ranking {len(sites)} sites"
        )

        try:

            ranked = sorted(
                sites,
                key=lambda x: x.get(
                    "feasibility_score",
                    0
                ),
                reverse=True
            )

            logger.success(
                "Site ranking completed"
            )

            return ranked

        except Exception as ex:

            logger.exception(
                f"Site ranking failed: {str(ex)}"
            )
            raise

    @staticmethod
    def site_dashboard(
        site_name: str,
        enrolled_patients: int,
        target_patients: int,
        protocol_deviations: int
    ) -> Dict[str, Any]:
        """
        Site KPI dashboard
        """

        logger.info(
            f"Generating dashboard for {site_name}"
        )

        try:

            enrollment_pct = round(
                (enrolled_patients / target_patients) * 100,
                2
            ) if target_patients else 0

            dashboard = {
                "site_name": site_name,
                "enrolled_patients": enrolled_patients,
                "target_patients": target_patients,
                "enrollment_percentage": enrollment_pct,
                "protocol_deviations": protocol_deviations,
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                f"Dashboard generated for {site_name}"
            )

            return dashboard

        except Exception as ex:

            logger.exception(
                f"Dashboard generation failed: {str(ex)}"
            )
            raise