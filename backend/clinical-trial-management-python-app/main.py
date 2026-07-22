import sys
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from utils.logger import logger

from routers.trial_router import router as trial_router


# =====================================================
# Loguru Configuration
# =====================================================

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
)

logger.add(
    "logs/clinical_trial_management.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
    enqueue=True,
    backtrace=True,
    diagnose=True
)


# =====================================================
# Application Lifecycle
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Starting Autonomous Clinical Trial "
        "Management Platform..."
    )

    logger.success(
        "Application startup completed"
    )

    yield

    logger.info(
        "Shutting down application..."
    )

    logger.success(
        "Application shutdown completed"
    )


# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(
    title="Autonomous Clinical Trial Management Platform",
    description=(
        "Enterprise Multi-Agent Clinical Trial "
        "Management System powered by AutoGen 0.7.5"
    ),
    version="1.0.0",
    lifespan=lifespan
)


# =====================================================
# CORS Configuration
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# =====================================================
# Request Logging Middleware
# =====================================================

@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):

    start_time = time.time()

    logger.info(
        f"Incoming Request | "
        f"Method={request.method} | "
        f"Path={request.url.path}"
    )

    response = await call_next(request)

    process_time = round(
        time.time() - start_time,
        3
    )

    logger.info(
        f"Completed Request | "
        f"Status={response.status_code} | "
        f"Duration={process_time}s"
    )

    return response


# =====================================================
# Global Exception Handler
# =====================================================

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        f"Unhandled Exception: {str(exc)}"
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": str(exc)
        }
    )


# =====================================================
# Root Endpoint
# =====================================================

@app.get(
    "/",
    tags=["System"]
)
async def root():

    logger.info(
        "Root endpoint accessed"
    )

    return {
        "success": True,
        "application":
        "Autonomous Clinical Trial Management Platform",
        "version": "1.0.0",
        "status": "Running"
    }


# =====================================================
# Health Endpoint
# =====================================================

@app.get(
    "/health",
    tags=["System"]
)
async def health_check():

    logger.info(
        "Health check requested"
    )

    return {
        "success": True,
        "status": "UP",
        "application":
        "Clinical Trial Management Platform"
    }


# =====================================================
# Router Registration
# =====================================================

app.include_router(
    trial_router,
    prefix="/api/v1/trials",
    tags=["Clinical Trial Management"]
)


# =====================================================
# Startup Log
# =====================================================

logger.success(
    "Router registration completed"
)