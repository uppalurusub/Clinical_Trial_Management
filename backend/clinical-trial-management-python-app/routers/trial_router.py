from utils.logger import logger

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.trial_service import TrialService

from models.request_model import TrialRequest
from models.response_model import (
    TrialResponse
)

router = APIRouter()

service = TrialService()


# =====================================================
# Health Check
# =====================================================

@router.get(
    "/health",
    tags=["Health"]
)
async def health_check():

    logger.info(
        "Health check endpoint called"
    )

    try:

        return await service.health_check()

    except Exception as ex:

        logger.exception(
            f"Health check failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


# =====================================================
# Manage Clinical Trial
# =====================================================

@router.post(
    "/manage-trial",
    response_model=TrialResponse,
    tags=["Clinical Trial Management"]
)
async def manage_trial(
    request: TrialRequest
):

    logger.info(
        f"Received manage trial request "
        f"for protocol: {request.protocol_id}"
    )

    try:

        result = await service.manage_trial(
            request
        )

        logger.success(
            f"Trial managed successfully "
            f"for protocol: {request.protocol_id}"
        )

        return result

    except Exception as ex:

        logger.exception(
            f"Manage trial failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


# =====================================================
# Get Trial History
# =====================================================

@router.get(
    "/history/{protocol_id}",
    tags=["Clinical Trial Management"]
)
async def get_trial_history(
    protocol_id: str
):

    logger.info(
        f"Fetching trial history "
        f"for protocol: {protocol_id}"
    )

    try:

        result = await service.get_trial_history(
            protocol_id
        )

        return result

    except Exception as ex:

        logger.exception(
            f"Error fetching history: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


# =====================================================
# Get All Trials
# =====================================================

@router.get(
    "/trials",
    tags=["Clinical Trial Management"]
)
async def get_all_trials():

    logger.info(
        "Fetching all trial records"
    )

    try:

        result = await service.get_all_trials()

        return result

    except Exception as ex:

        logger.exception(
            f"Failed to fetch trials: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


# =====================================================
# Delete Trial
# =====================================================

@router.delete(
    "/delete/{protocol_id}",
    tags=["Clinical Trial Management"]
)
async def delete_trial(
    protocol_id: str
):

    logger.info(
        f"Deleting protocol: {protocol_id}"
    )

    try:

        result = await service.delete_trial(
            protocol_id
        )

        return result

    except Exception as ex:

        logger.exception(
            f"Delete failed: {str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )


# =====================================================
# Dashboard Endpoint
# =====================================================

@router.get(
    "/dashboard/{protocol_id}",
    tags=["Dashboard"]
)
async def get_dashboard(
    protocol_id: str
):

    logger.info(
        f"Dashboard requested for "
        f"{protocol_id}"
    )

    try:

        history = await service.get_trial_history(
            protocol_id
        )

        return {
            "success": True,
            "protocol_id": protocol_id,
            "dashboard": history
        }

    except Exception as ex:

        logger.exception(
            f"Dashboard generation failed: "
            f"{str(ex)}"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex)
        )