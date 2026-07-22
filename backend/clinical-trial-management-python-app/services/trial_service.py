from utils.logger import logger

from implementation.trial_impl import (
    TrialImplementation
)

import mlflow
from datetime import datetime
import time

mlflow.set_tracking_uri(
    "http://localhost:5000"
)

mlflow.set_experiment(
    "Clinical_Trial_Management_Manage_Interface"
)

class TrialService:

    def __init__(self):

        logger.info(
            "Initializing TrialService..."
        )

        self.impl = TrialImplementation()

        logger.success(
            "TrialService initialized successfully"
        )

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

    async def manage_trial(
        self,
        request
    ):
        """
        Execute complete clinical trial management workflow
        """

        start_time = datetime.now()
        start_ts = time.time()

        logger.info(
            f"Received trial management request "
            f"for protocol: {request.protocol_id}"
        )

        try:

            with mlflow.start_run(
                run_name=
                f"Clinical_Trial_Management_Manage_Trial_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ):
                # Log to MLflow
                mlflow.log_param(
                    "start_time",
                    start_time.strftime("%Y-%m-%d %H:%M:%S")
                )
                mlflow.log_param(
                    "input_text",
                    request
                )

                result = await self.impl.manage_trial(
                    request
                )

                mlflow.log_param(
                    "response",
                    result
                )

                mlflow.set_tag(
                    "source",
                    "FastAPI"
                )

                mlflow.set_tag(
                    "endpoint",
                    "trials/manage-trial"
                )



                end_time = datetime.now()
                end_ts = time.time()

                execution_time = end_ts - start_ts

                mlflow.log_param(
                    "end_time",
                    end_time.strftime("%Y-%m-%d %H:%M:%S")
                )

                mlflow.log_metric(
                    "execution_time_seconds",
                    round(execution_time, 4)
                )

            logger.success(
                f"Trial management completed "
                f"for protocol: {request.protocol_id}"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"Trial management failed "
                f"for protocol: {request.protocol_id}"
            )

            raise Exception(str(ex))

    async def get_trial_history(
        self,
        protocol_id: str
    ):
        """
        Get trial execution history
        """

        logger.info(
            f"Fetching trial history "
            f"for protocol: {protocol_id}"
        )

        try:

            result = await self.impl.get_trial_history(
                protocol_id
            )

            if result is None:

                logger.warning(
                    f"No trial history found for "
                    f"{protocol_id}"
                )

                return {
                    "success": False,
                    "message": "Trial not found"
                }

            logger.success(
                f"Trial history retrieved "
                f"for {protocol_id}"
            )

            return {
                "success": True,
                "data": result
            }

        except Exception as ex:

            logger.exception(
                f"Error retrieving trial history "
                f"for {protocol_id}"
            )

            raise Exception(str(ex))

    async def get_all_trials(self):
        """
        Get all managed trials
        """

        logger.info(
            "Fetching all trial records..."
        )

        try:

            result = await self.impl.get_all_trials()

            logger.success(
                f"Retrieved "
                f"{len(result)} trial records"
            )

            return {
                "success": True,
                "count": len(result),
                "data": result
            }

        except Exception as ex:

            logger.exception(
                "Error fetching all trials"
            )

            raise Exception(str(ex))

    async def delete_trial(
        self,
        protocol_id: str
    ):
        """
        Delete trial history
        """

        logger.info(
            f"Deleting protocol: {protocol_id}"
        )

        try:

            deleted = await self.impl.delete_trial(
                protocol_id
            )

            if deleted:

                logger.success(
                    f"Protocol deleted: "
                    f"{protocol_id}"
                )

                return {
                    "success": True,
                    "message": (
                        f"{protocol_id} deleted "
                        f"successfully"
                    )
                }

            logger.warning(
                f"Protocol not found: "
                f"{protocol_id}"
            )

            return {
                "success": False,
                "message": "Protocol not found"
            }

        except Exception as ex:

            logger.exception(
                f"Delete failed for "
                f"{protocol_id}"
            )

            raise Exception(str(ex))

    async def health_check(self):
        """
        Service health check
        """

        logger.info(
            "Performing health check..."
        )

        try:

            return {
                "success": True,
                "service": (
                    "Clinical Trial "
                    "Management Platform"
                ),
                "status": "UP"
            }

        except Exception as ex:

            logger.exception(
                "Health check failed"
            )

            return {
                "success": False,
                "status": "DOWN",
                "message": str(ex)
            }