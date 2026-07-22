from datetime import datetime
from time import perf_counter
from utils.logger import logger

from agents.trial_agents import TrialAgents
from config.llm_config import get_model_client
from memory.trial_memory import TrialMemory


class TrialImplementation:

    def __init__(self):

        logger.info(
            "Initializing TrialImplementation..."
        )

        self.memory = TrialMemory()

        self.model_client = get_model_client()

        self.agents = TrialAgents.build_agents(
            self.model_client
        )

        logger.success(
            "TrialImplementation initialized successfully"
        )

    async def get_all_trials(self):

        logger.info(
            "Fetching all trial records"
        )

        return {
            "success": True,
            "count": self.memory.count(),
            "data": self.memory.get_all()
        }


    async def delete_trial(
        self,
        protocol_id: str
    ):

        deleted = self.memory.delete(
            protocol_id
        )

        return {
            "success": deleted,
            "protocol_id": protocol_id,
            "message":
                "Deleted Successfully"
                if deleted
                else "Protocol Not Found"
        }


    async def get_dashboard(
        self,
        protocol_id: str
    ):

        trial = self.memory.get(
            protocol_id
        )

        if not trial:

            return {
                "success": False,
                "message": "Protocol not found"
            }

        return {
            "success": True,
            "protocol_id": protocol_id,
            "dashboard": trial
        }

    async def get_trial_history(
        self,
        protocol_id: str
    ):

        logger.info(
            f"Fetching trial history: {protocol_id}"
        )

        result = self.memory.get(protocol_id)

        if not result:

            return {
                "success": False,
                "protocol_id": protocol_id,
                "message": "Protocol not found"
            }

        return {
            "success": True,
            "protocol_id": protocol_id,
            "history": result
        }

    async def manage_trial(self, request):

        start_time = perf_counter()

        logger.info(
            f"Processing protocol: {request.protocol_id}"
        )

        try:

            # =====================================================
            # Study Setup Agent
            # =====================================================

            logger.info(
                "Executing StudySetupAgent..."
            )

            study_setup_result = await self.agents[
                "study_setup"
            ].run(
                task=f"""
                Create Clinical Trial Study Setup Plan

                Protocol ID: {request.protocol_id}
                Study Name: {request.study_name}
                Phase: {request.phase}
                Therapeutic Area: {request.therapeutic_area}
                Countries: {request.countries}

                Generate:
                1. Protocol Summary
                2. Study Design
                3. Timeline
                4. Risk Assessment
                5. Recommendations
                """
            )

            study_setup_output = (
                study_setup_result.messages[-1].content
            )

            logger.success(
                "StudySetupAgent completed"
            )

            # =====================================================
            # Site Agent
            # =====================================================

            logger.info(
                "Executing SiteAgent..."
            )

            site_result = await self.agents[
                "site"
            ].run(
                task=f"""
                Create Site Strategy

                Number of Sites:
                {len(request.sites)}

                Countries:
                {request.countries}

                Generate:
                1. Site Selection Plan
                2. Site Activation Plan
                3. Enrollment Forecast
                4. Recommendations
                """
            )

            site_output = (
                site_result.messages[-1].content
            )

            logger.success(
                "SiteAgent completed"
            )

            # =====================================================
            # Recruitment Agent
            # =====================================================

            logger.info(
                "Executing RecruitmentAgent..."
            )

            recruitment_result = await self.agents[
                "recruitment"
            ].run(
                task=f"""
                Create Recruitment Strategy

                Target Patients:
                {request.recruitment.target_patients}

                Recruitment Channels:
                {request.recruitment.recruitment_channels}

                Generate:
                1. Recruitment Plan
                2. Enrollment Timeline
                3. Retention Strategy
                4. Recommendations
                """
            )

            recruitment_output = (
                recruitment_result.messages[-1].content
            )

            logger.success(
                "RecruitmentAgent completed"
            )

            # =====================================================
            # Monitoring Agent
            # =====================================================

            logger.info(
                "Executing MonitoringAgent..."
            )

            monitoring_result = await self.agents[
                "monitoring"
            ].run(
                task=f"""
                Create Monitoring Plan

                Monitoring Type:
                {request.monitoring.monitoring_type}

                Frequency:
                {request.monitoring.monitoring_frequency}

                Generate:
                1. Monitoring Schedule
                2. RBM Strategy
                3. Issue Management Plan
                4. CAPA Strategy
                """
            )

            monitoring_output = (
                monitoring_result.messages[-1].content
            )

            logger.success(
                "MonitoringAgent completed"
            )

            # =====================================================
            # Finance Agent
            # =====================================================

            logger.info(
                "Executing FinanceAgent..."
            )

            finance_result = await self.agents[
                "finance"
            ].run(
                task=f"""
                Create Financial Plan

                Total Budget:
                {request.budget.total_budget}

                Site Budget:
                {request.budget.site_budget}

                Recruitment Budget:
                {request.budget.recruitment_budget}

                Generate:
                1. Budget Forecast
                2. Site Payments
                3. Cost Control Plan
                4. Recommendations
                """
            )

            finance_output = (
                finance_result.messages[-1].content
            )

            logger.success(
                "FinanceAgent completed"
            )

            # =====================================================
            # Compliance Agent
            # =====================================================

            logger.info(
                "Executing ComplianceAgent..."
            )

            compliance_result = await self.agents[
                "compliance"
            ].run(
                task=f"""
                Create Compliance Strategy

                Authorities:
                {request.compliance.regulatory_authorities}

                Generate:
                1. Regulatory Strategy
                2. Audit Readiness
                3. TMF Readiness
                4. Inspection Plan
                """
            )

            compliance_output = (
                compliance_result.messages[-1].content
            )

            logger.success(
                "ComplianceAgent completed"
            )

            # =====================================================
            # Trial Director Summary
            # =====================================================

            logger.info(
                "Executing TrialDirectorAgent..."
            )

            director_result = await self.agents[
                "trial_director"
            ].run(
                task=f"""
                Review all outputs:

                STUDY SETUP:
                {study_setup_output}

                SITE:
                {site_output}

                RECRUITMENT:
                {recruitment_output}

                MONITORING:
                {monitoring_output}

                FINANCE:
                {finance_output}

                COMPLIANCE:
                {compliance_output}

                Generate:
                1. Executive Summary
                2. Overall Recommendations
                3. Trial Success Factors
                """
            )

            executive_summary = (
                director_result.messages[-1].content
            )

            logger.success(
                "TrialDirectorAgent completed"
            )

            execution_time = round(
                perf_counter() - start_time,
                2
            )

            logger.info(
                f"Execution completed in "
                f"{execution_time} seconds"
            )

            response = {
                "protocol_id": request.protocol_id,
                "study_name": request.study_name,
                "execution_timestamp": datetime.utcnow(),

                "study_setup": {
                    "protocol_summary": study_setup_output
                },

                "site_management": {
                    "strategy": site_output
                },

                "recruitment_management": {
                    "strategy": recruitment_output
                },

                "monitoring_management": {
                    "strategy": monitoring_output
                },

                "finance_management": {
                    "strategy": finance_output
                },

                "compliance_management": {
                    "strategy": compliance_output
                },

                "executive_summary": executive_summary,

                "agent_summary": {
                    "StudySetupAgent": "Completed",
                    "SiteAgent": "Completed",
                    "RecruitmentAgent": "Completed",
                    "MonitoringAgent": "Completed",
                    "FinanceAgent": "Completed",
                    "ComplianceAgent": "Completed",
                    "TrialDirectorAgent": "Completed"
                },

                "execution_time_seconds": execution_time
            }

            self.memory.save(
                request.protocol_id,
                response
            )

            logger.success(
                f"Protocol {request.protocol_id} "
                f"stored in memory"
            )

            return response

        except Exception as ex:

            logger.exception(
                f"Trial processing failed: {str(ex)}"
            )

            raise Exception(
                f"Clinical Trial Management Error: "
                f"{str(ex)}"
            )