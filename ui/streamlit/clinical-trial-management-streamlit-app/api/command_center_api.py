"""
command_center_api.py

Clinical Trial Management System

Streamlit API Client

Responsibilities
----------------
1. Communicate with FastAPI Clinical Trial API
2. Execute HTTP requests
3. Handle API validation errors
4. Handle connection and timeout errors
5. Parse FastAPI error responses
6. Return JSON API responses
"""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests


# ============================================================
# API CONFIGURATION
# ============================================================

DEFAULT_API_BASE_URL = (
    "http://localhost:8000/api/v1/trials"
)

REQUEST_TIMEOUT = 600000


# ============================================================
# TYPE ALIASES
# ============================================================

JsonDict = Dict[str, Any]


# ============================================================
# API EXCEPTIONS
# ============================================================

class TrialAPIError(Exception):
    """
    Base Clinical Trial API exception.
    """


class TrialAPIConnectionError(TrialAPIError):
    """
    Raised when Streamlit cannot connect to FastAPI.
    """


class TrialAPITimeoutError(TrialAPIError):
    """
    Raised when an API request times out.
    """


class TrialAPIValidationError(TrialAPIError):
    """
    Raised when FastAPI request validation fails.
    """


class TrialAPINotFoundError(TrialAPIError):
    """
    Raised when API endpoint or trial is not found.
    """


class TrialAPIServerError(TrialAPIError):
    """
    Raised when FastAPI returns a server error.
    """


# ============================================================
# URL BUILDER
# ============================================================

def build_api_url(
    base_url: str,
    endpoint: str,
) -> str:
    """
    Build normalized FastAPI URL.

    Example
    -------
    Base URL:
        http://localhost:8000/api/v1/trials

    Endpoint:
        /manage-trial

    Result:
        http://localhost:8000/api/v1/trials/manage-trial
    """

    normalized_base_url = (
        base_url.rstrip("/")
    )

    normalized_endpoint = (
        endpoint.lstrip("/")
    )

    return (
        f"{normalized_base_url}/"
        f"{normalized_endpoint}"
    )


# ============================================================
# RESPONSE PARSER
# ============================================================

def parse_response(
    response: requests.Response,
) -> Any:
    """
    Safely parse HTTP response.
    """

    try:

        return response.json()

    except ValueError:

        return {
            "status_code": response.status_code,
            "text": response.text,
        }


# ============================================================
# FASTAPI ERROR DETAIL
# ============================================================

def extract_error_detail(
    response_data: Any,
) -> str:
    """
    Extract readable error detail from FastAPI response.
    """

    if isinstance(response_data, str):

        return response_data

    if not isinstance(
        response_data,
        dict,
    ):

        return str(response_data)

    detail = response_data.get(
        "detail"
    )

    if isinstance(detail, str):

        return detail

    if isinstance(detail, list):

        validation_errors = []

        for error in detail:

            if not isinstance(error, dict):

                validation_errors.append(
                    str(error)
                )

                continue

            location = error.get(
                "loc",
                [],
            )

            message = error.get(
                "msg",
                "Invalid value",
            )

            location = [
                str(item)
                for item in location
                if item != "body"
            ]

            field_name = " → ".join(
                location
            )

            if field_name:

                validation_errors.append(
                    f"{field_name}: {message}"
                )

            else:

                validation_errors.append(
                    str(message)
                )

        return " | ".join(
            validation_errors
        )

    message = response_data.get(
        "message"
    )

    if isinstance(message, str):

        return message

    return str(response_data)


# ============================================================
# RESPONSE VALIDATION
# ============================================================

def validate_response(
    response: requests.Response,
) -> Any:
    """
    Validate FastAPI HTTP response.
    """

    response_data = parse_response(
        response
    )

    if response.ok:

        return response_data

    error_detail = extract_error_detail(
        response_data
    )

    request_url = response.url

    # --------------------------------------------------------
    # Bad Request
    # --------------------------------------------------------

    if response.status_code == 400:

        raise TrialAPIValidationError(
            "400 Bad Request\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Unauthorized
    # --------------------------------------------------------

    if response.status_code == 401:

        raise TrialAPIError(
            "401 Unauthorized\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Forbidden
    # --------------------------------------------------------

    if response.status_code == 403:

        raise TrialAPIError(
            "403 Forbidden\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Not Found
    # --------------------------------------------------------

    if response.status_code == 404:

        raise TrialAPINotFoundError(
            "404 Not Found\n\n"
            f"Requested URL:\n"
            f"{request_url}\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Request Timeout
    # --------------------------------------------------------

    if response.status_code == 408:

        raise TrialAPITimeoutError(
            "408 Request Timeout\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # FastAPI Validation Error
    # --------------------------------------------------------

    if response.status_code == 422:

        raise TrialAPIValidationError(
            "422 FastAPI Request Validation Failed"
            "\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Too Many Requests
    # --------------------------------------------------------

    if response.status_code == 429:

        raise TrialAPIError(
            "429 Too Many Requests\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Server Errors
    # --------------------------------------------------------

    if response.status_code >= 500:

        raise TrialAPIServerError(
            f"{response.status_code} "
            f"FastAPI Server Error\n\n"
            f"{error_detail}"
        )

    # --------------------------------------------------------
    # Generic API Error
    # --------------------------------------------------------

    raise TrialAPIError(
        f"Clinical Trial API request failed "
        f"with HTTP status "
        f"{response.status_code}.\n\n"
        f"{error_detail}"
    )


# ============================================================
# GENERIC API REQUEST
# ============================================================

def api_request(
    method: str,
    base_url: str,
    endpoint: str,
    payload: Optional[JsonDict] = None,
) -> Any:
    """
    Execute generic FastAPI request.
    """

    url = build_api_url(
        base_url=base_url,
        endpoint=endpoint,
    )

    try:

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )

        return validate_response(
            response
        )

    except requests.exceptions.ConnectionError as exc:

        raise TrialAPIConnectionError(
            "Unable to connect to FastAPI server."
            "\n\n"
            f"Requested URL:\n{url}"
            "\n\n"
            "Verify that the FastAPI service "
            "is running."
        ) from exc

    except requests.exceptions.Timeout as exc:

        raise TrialAPITimeoutError(
            "Clinical Trial API request timed out."
            "\n\n"
            f"Requested URL:\n{url}"
        ) from exc

    except TrialAPIError:

        raise

    except requests.exceptions.RequestException as exc:

        raise TrialAPIError(
            "Clinical Trial API request failed."
            "\n\n"
            f"Requested URL:\n{url}"
            "\n\n"
            f"Error: {str(exc)}"
        ) from exc


# ============================================================
# HEALTH CHECK
# ============================================================

def health_check(
    base_url: str = DEFAULT_API_BASE_URL,
) -> Any:
    """
    Check Clinical Trial API health.

    FastAPI Endpoint
    ----------------
    GET /health
    """

    return api_request(
        method="GET",
        base_url=base_url,
        endpoint="/health",
    )


# ============================================================
# MANAGE CLINICAL TRIAL
# ============================================================

def manage_trial(
    base_url: str,
    payload: JsonDict,
) -> Any:
    """
    Create or manage a clinical trial.

    FastAPI Endpoint
    ----------------
    POST /manage-trial
    """

    if not isinstance(payload, dict):

        raise TrialAPIValidationError(
            "Trial request payload must "
            "be a dictionary."
        )

    protocol_id = payload.get(
        "protocol_id"
    )

    if not protocol_id:

        raise TrialAPIValidationError(
            "protocol_id is required."
        )

    return api_request(
        method="POST",
        base_url=base_url,
        endpoint="/manage-trial",
        payload=payload,
    )


# ============================================================
# GET TRIAL HISTORY
# ============================================================

def get_trial_history(
    base_url: str,
    protocol_id: str,
) -> Any:
    """
    Retrieve clinical trial history.

    FastAPI Endpoint
    ----------------
    GET /history/{protocol_id}
    """

    protocol_id = validate_protocol_id(
        protocol_id
    )

    return api_request(
        method="GET",
        base_url=base_url,
        endpoint=(
            f"/history/{protocol_id}"
        ),
    )


# ============================================================
# GET ALL TRIALS
# ============================================================

def get_all_trials(
    base_url: str,
) -> Any:
    """
    Retrieve all clinical trial records.

    FastAPI Endpoint
    ----------------
    GET /trials
    """

    return api_request(
        method="GET",
        base_url=base_url,
        endpoint="/trials",
    )


# ============================================================
# DELETE TRIAL
# ============================================================

def delete_trial(
    base_url: str,
    protocol_id: str,
) -> Any:
    """
    Delete clinical trial protocol.

    FastAPI Endpoint
    ----------------
    DELETE /delete/{protocol_id}
    """

    protocol_id = validate_protocol_id(
        protocol_id
    )

    return api_request(
        method="DELETE",
        base_url=base_url,
        endpoint=(
            f"/delete/{protocol_id}"
        ),
    )


# ============================================================
# GET TRIAL DASHBOARD
# ============================================================

def get_dashboard(
    base_url: str,
    protocol_id: str,
) -> Any:
    """
    Retrieve protocol dashboard.

    FastAPI Endpoint
    ----------------
    GET /dashboard/{protocol_id}
    """

    protocol_id = validate_protocol_id(
        protocol_id
    )

    return api_request(
        method="GET",
        base_url=base_url,
        endpoint=(
            f"/dashboard/{protocol_id}"
        ),
    )


# ============================================================
# PROTOCOL ID VALIDATION
# ============================================================

def validate_protocol_id(
    protocol_id: str,
) -> str:
    """
    Validate and normalize protocol ID.
    """

    if protocol_id is None:

        raise TrialAPIValidationError(
            "Protocol ID is required."
        )

    normalized_protocol_id = str(
        protocol_id
    ).strip()

    if not normalized_protocol_id:

        raise TrialAPIValidationError(
            "Protocol ID is required."
        )

    return normalized_protocol_id