from datetime import datetime
from typing import Dict, List, Any

from utils.logger import logger


class FinanceTools:
    """
    Clinical Trial Financial Management Tools
    """

    @staticmethod
    def calculate_budget_utilization(
        total_budget: float,
        actual_spend: float
    ) -> Dict[str, Any]:
        """
        Calculate budget utilization
        """

        logger.info(
            "Calculating budget utilization"
        )

        try:

            utilization_percentage = round(
                (actual_spend / total_budget) * 100,
                2
            ) if total_budget > 0 else 0

            remaining_budget = round(
                total_budget - actual_spend,
                2
            )

            result = {
                "total_budget": total_budget,
                "actual_spend": actual_spend,
                "remaining_budget": remaining_budget,
                "utilization_percentage": utilization_percentage,
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "Budget utilization calculated successfully"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Budget utilization calculation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def forecast_trial_cost(
        current_spend: float,
        completed_percentage: float
    ) -> Dict[str, Any]:
        """
        Forecast final trial cost
        """

        logger.info(
            "Forecasting clinical trial cost"
        )

        try:

            if completed_percentage <= 0:
                projected_cost = current_spend
            else:
                projected_cost = round(
                    current_spend /
                    (completed_percentage / 100),
                    2
                )

            result = {
                "current_spend": current_spend,
                "completion_percentage": completed_percentage,
                "projected_final_cost": projected_cost
            }

            logger.success(
                "Cost forecast completed"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Cost forecast failed: {str(ex)}"
            )
            raise

    @staticmethod
    def calculate_site_payment(
        enrolled_patients: int,
        payment_per_patient: float
    ) -> Dict[str, Any]:
        """
        Calculate site payment amount
        """

        logger.info(
            "Calculating site payment"
        )

        try:

            total_payment = round(
                enrolled_patients *
                payment_per_patient,
                2
            )

            result = {
                "enrolled_patients": enrolled_patients,
                "payment_per_patient": payment_per_patient,
                "total_payment": total_payment
            }

            logger.success(
                "Site payment calculated"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Site payment calculation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def calculate_patient_reimbursement(
        visit_count: int,
        reimbursement_per_visit: float,
        travel_allowance: float = 0
    ) -> Dict[str, Any]:
        """
        Calculate patient reimbursement
        """

        logger.info(
            "Calculating patient reimbursement"
        )

        try:

            reimbursement = (
                visit_count *
                reimbursement_per_visit
            ) + travel_allowance

            result = {
                "visit_count": visit_count,
                "reimbursement_per_visit": reimbursement_per_visit,
                "travel_allowance": travel_allowance,
                "total_reimbursement": round(
                    reimbursement,
                    2
                )
            }

            logger.success(
                "Patient reimbursement calculated"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Patient reimbursement calculation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def assess_financial_risk(
        budget_utilization_pct: float,
        projected_overrun_pct: float
    ) -> Dict[str, Any]:
        """
        Financial risk assessment
        """

        logger.info(
            "Assessing financial risk"
        )

        try:

            score = (
                budget_utilization_pct * 0.6 +
                projected_overrun_pct * 0.4
            )

            if score < 60:
                risk = "Low"
            elif score < 85:
                risk = "Medium"
            else:
                risk = "High"

            result = {
                "risk_score": round(score, 2),
                "risk_level": risk
            }

            logger.success(
                f"Financial risk assessment completed: {risk}"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Financial risk assessment failed: {str(ex)}"
            )
            raise

    @staticmethod
    def process_invoice(
        invoice_id: str,
        vendor_name: str,
        amount: float
    ) -> Dict[str, Any]:
        """
        Process invoice
        """

        logger.info(
            f"Processing invoice {invoice_id}"
        )

        try:

            result = {
                "invoice_id": invoice_id,
                "vendor_name": vendor_name,
                "amount": amount,
                "status": "Approved",
                "processed_at": datetime.utcnow().isoformat()
            }

            logger.success(
                f"Invoice processed: {invoice_id}"
            )

            return result

        except Exception as ex:
            logger.exception(
                f"Invoice processing failed: {str(ex)}"
            )
            raise

    @staticmethod
    def generate_financial_kpis(
        total_budget: float,
        actual_spend: float,
        site_payments: float,
        reimbursements: float
    ) -> Dict[str, Any]:
        """
        Generate financial KPIs
        """

        logger.info(
            "Generating financial KPIs"
        )

        try:

            remaining_budget = (
                total_budget - actual_spend
            )

            kpis = {
                "total_budget": total_budget,
                "actual_spend": actual_spend,
                "remaining_budget": remaining_budget,
                "site_payments": site_payments,
                "patient_reimbursements": reimbursements,
                "budget_consumption_pct": round(
                    (actual_spend / total_budget) * 100,
                    2
                ) if total_budget > 0 else 0
            }

            logger.success(
                "Financial KPIs generated"
            )

            return kpis

        except Exception as ex:
            logger.exception(
                f"KPI generation failed: {str(ex)}"
            )
            raise

    @staticmethod
    def generate_finance_dashboard(
        protocol_id: str,
        total_budget: float,
        actual_spend: float
    ) -> Dict[str, Any]:
        """
        Generate finance dashboard
        """

        logger.info(
            f"Generating finance dashboard for {protocol_id}"
        )

        try:

            dashboard = {
                "protocol_id": protocol_id,
                "total_budget": total_budget,
                "actual_spend": actual_spend,
                "remaining_budget": (
                    total_budget - actual_spend
                ),
                "budget_utilization_pct": round(
                    (actual_spend / total_budget) * 100,
                    2
                ) if total_budget > 0 else 0,
                "status": "ACTIVE",
                "generated_at": datetime.utcnow().isoformat()
            }

            logger.success(
                "Finance dashboard generated"
            )

            return dashboard

        except Exception as ex:
            logger.exception(
                f"Finance dashboard generation failed: {str(ex)}"
            )
            raise