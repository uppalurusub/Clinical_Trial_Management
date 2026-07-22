from utils.logger import logger
from config.llm_config import get_model_client

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = get_model_client()

class TrialAgents:
    """
    Clinical Trial Management Multi-Agent Factory
    """

    @staticmethod
    def build_agents(
        model_client: OpenAIChatCompletionClient
    ) -> dict:

        logger.info(
            "Initializing Clinical Trial Management Agents..."
        )

        try:

            # =====================================================
            # Trial Director Agent
            # =====================================================

            trial_director_agent = AssistantAgent(
                name="TrialDirectorAgent",
                model_client=model_client,
                system_message="""
                You are an expert Clinical Trial Director.

                Responsibilities:
                - Coordinate all trial agents
                - Review outputs
                - Resolve conflicts
                - Generate executive summaries
                - Provide final recommendations

                Focus on:
                - Trial success
                - Patient safety
                - Budget adherence
                - Regulatory compliance
                """
            )

            logger.info(
                "TrialDirectorAgent initialized successfully"
            )

            # =====================================================
            # Study Setup Agent
            # =====================================================

            study_setup_agent = AssistantAgent(
                name="StudySetupAgent",
                model_client=model_client,
                system_message="""
                You are an expert Clinical Trial Design Specialist.

                Responsibilities:
                - Protocol design
                - Study objectives
                - Endpoint definition
                - Timeline planning
                - Country selection
                - Risk assessment

                Deliver:
                - Study setup plan
                - Risk mitigation plan
                - Operational recommendations
                """
            )

            logger.info(
                "StudySetupAgent initialized successfully"
            )

            # =====================================================
            # Site Agent
            # =====================================================

            site_agent = AssistantAgent(
                name="SiteAgent",
                model_client=model_client,
                system_message="""
                You are an expert Clinical Site Management Specialist.

                Responsibilities:
                - Site feasibility
                - Site selection
                - Site activation
                - Investigator management
                - Site performance monitoring

                Deliver:
                - Site strategy
                - Enrollment projections
                - Activation plans
                """
            )

            logger.info(
                "SiteAgent initialized successfully"
            )

            # =====================================================
            # Recruitment Agent
            # =====================================================

            recruitment_agent = AssistantAgent(
                name="RecruitmentAgent",
                model_client=model_client,
                system_message="""
                You are an expert Patient Recruitment Specialist.

                Responsibilities:
                - Recruitment planning
                - Eligibility review
                - Enrollment forecasting
                - Recruitment channel optimization
                - Patient retention

                Deliver:
                - Recruitment strategy
                - Enrollment timeline
                - Retention recommendations
                """
            )

            logger.info(
                "RecruitmentAgent initialized successfully"
            )

            # =====================================================
            # Monitoring Agent
            # =====================================================

            monitoring_agent = AssistantAgent(
                name="MonitoringAgent",
                model_client=model_client,
                system_message="""
                You are an expert Clinical Monitoring Specialist.

                Responsibilities:
                - Risk-Based Monitoring
                - Remote Monitoring
                - Source Data Verification
                - Monitoring Visits
                - CAPA Management
                - Protocol Compliance

                Deliver:
                - Monitoring Plan
                - Risk Assessment
                - Issue Management Strategy
                """
            )

            logger.info(
                "MonitoringAgent initialized successfully"
            )

            # =====================================================
            # Finance Agent
            # =====================================================

            finance_agent = AssistantAgent(
                name="FinanceAgent",
                model_client=model_client,
                system_message="""
                You are an expert Clinical Trial Finance Manager.

                Responsibilities:
                - Budget planning
                - Cost forecasting
                - Site payments
                - Patient reimbursements
                - Financial risk management

                Deliver:
                - Budget utilization plan
                - Cost forecasts
                - Financial recommendations
                """
            )

            logger.info(
                "FinanceAgent initialized successfully"
            )

            # =====================================================
            # Compliance Agent
            # =====================================================

            compliance_agent = AssistantAgent(
                name="ComplianceAgent",
                model_client=model_client,
                system_message="""
                You are an expert Regulatory Compliance Officer.

                Responsibilities:
                - FDA compliance
                - EMA compliance
                - ICH-GCP compliance
                - Audit readiness
                - TMF review
                - Inspection preparation

                Deliver:
                - Compliance report
                - Audit readiness report
                - Regulatory recommendations
                """
            )

            logger.info(
                "ComplianceAgent initialized successfully"
            )

            agents = {
                "trial_director": trial_director_agent,
                "study_setup": study_setup_agent,
                "site": site_agent,
                "recruitment": recruitment_agent,
                "monitoring": monitoring_agent,
                "finance": finance_agent,
                "compliance": compliance_agent
            }

            logger.success(
                f"{len(agents)} agents initialized successfully"
            )

            return agents

        except Exception as ex:
            logger.exception(
                f"Agent initialization failed: {str(ex)}"
            )
            raise