"""
response_view.py

Clinical Trial Management System

Streamlit API Response Components

Responsibilities
----------------
1. Render FastAPI errors
2. Render successful API responses
3. Parse nested FastAPI validation errors
4. Display response status and messages
5. Render generic dictionary and list responses
6. Provide raw JSON response inspection
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import streamlit as st

from api.command_center_api import (
    TrialAPIConnectionError,
    TrialAPIError,
    TrialAPINotFoundError,
    TrialAPIServerError,
    TrialAPITimeoutError,
    TrialAPIValidationError,
)


# ============================================================
# TYPE ALIASES
# ============================================================

JsonDict = Dict[str, Any]


# ============================================================
# RESPONSE HELPERS
# ============================================================

def format_field_name(
    field_name: Any,
) -> str:
    """
    Convert API field name into display label.

    Example
    -------
    protocol_id -> Protocol Id
    trial_metrics -> Trial Metrics
    """

    return (
        str(field_name)
        .replace("_", " ")
        .replace("-", " ")
        .strip()
        .title()
    )


def is_scalar(
    value: Any,
) -> bool:
    """
    Check whether a value is a scalar response value.
    """

    return not isinstance(
        value,
        (
            dict,
            list,
            tuple,
            set,
        ),
    )


def get_response_success(
    response: Any,
) -> bool:
    """
    Determine API response success status.
    """

    if not isinstance(response, dict):

        return True

    success = response.get(
        "success"
    )

    if success is None:

        return True

    return bool(success)


def get_response_message(
    response: Any,
) -> Optional[str]:
    """
    Extract API response message.
    """

    if not isinstance(response, dict):

        return None

    message_keys = [
        "message",
        "detail",
        "status_message",
        "description",
    ]

    for key in message_keys:

        value = response.get(key)

        if isinstance(value, str) and value.strip():

            return value.strip()

    return None


# ============================================================
# FASTAPI VALIDATION ERROR PARSER
# ============================================================

def parse_validation_errors(
    detail: Any,
) -> List[str]:
    """
    Parse FastAPI/Pydantic validation errors.

    Supported structure
    -------------------
    [
        {
            "type": "missing",
            "loc": ["body", "protocol_id"],
            "msg": "Field required",
            "input": {}
        }
    ]
    """

    if detail is None:

        return []

    if isinstance(detail, str):

        return [
            detail
        ]

    if not isinstance(detail, list):

        return [
            str(detail)
        ]

    validation_errors: List[str] = []

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

        error_type = error.get(
            "type"
        )

        location_parts = [
            str(item)
            for item in location
            if item not in {
                "body",
                "response",
            }
        ]

        field_name = " → ".join(
            location_parts
        )

        if field_name:

            formatted_error = (
                f"{field_name}: {message}"
            )

        else:

            formatted_error = str(
                message
            )

        if error_type:

            formatted_error += (
                f" [{error_type}]"
            )

        validation_errors.append(
            formatted_error
        )

    return validation_errors


# ============================================================
# API ERROR RENDERER
# ============================================================

def render_api_error(
    error: Exception,
) -> None:
    """
    Render Clinical Trial API exception.

    Parameters
    ----------
    error:
        Exception raised by command_center_api.
    """

    error_message = str(
        error
    )

    # --------------------------------------------------------
    # Connection Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPIConnectionError,
    ):

        st.error(
            "🔌 Unable to Connect to Clinical Trial API"
        )

        st.markdown(
            """
The Streamlit application could not connect to the
FastAPI Clinical Trial service.

Please verify:

- FastAPI application is running.
- API host and port are correct.
- API base URL is correct.
- Docker/container networking is configured correctly.
- The `/api/v1/trials` router is registered.
"""
        )

        with st.expander(
            "🔍 Connection Error Details",
            expanded=False,
        ):

            st.code(
                error_message,
                language="text",
            )

        return

    # --------------------------------------------------------
    # Timeout Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPITimeoutError,
    ):

        st.error(
            "⏱️ Clinical Trial API Request Timed Out"
        )

        st.warning(
            "The trial management workflow did not "
            "complete within the configured request timeout."
        )

        st.info(
            "Agent-based clinical trial workflows may take "
            "several minutes when multiple agents execute "
            "sequentially."
        )

        with st.expander(
            "🔍 Timeout Details",
            expanded=False,
        ):

            st.code(
                error_message,
                language="text",
            )

        return

    # --------------------------------------------------------
    # Validation Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPIValidationError,
    ):

        st.error(
            "⚠️ Clinical Trial Request Validation Failed"
        )

        validation_errors = (
            parse_validation_errors(
                error_message
            )
        )

        if validation_errors:

            for validation_error in validation_errors:

                st.warning(
                    validation_error
                )

        else:

            st.code(
                error_message,
                language="text",
            )

        st.info(
            "Verify that the Streamlit request payload "
            "matches the FastAPI TrialRequest model."
        )

        return

    # --------------------------------------------------------
    # Not Found Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPINotFoundError,
    ):

        st.warning(
            "🔎 Clinical Trial Resource Not Found"
        )

        st.markdown(
            """
The requested clinical trial resource could not be found.

Verify:

- Protocol ID is correct.
- The trial exists in the backend repository.
- The FastAPI route prefix is correct.
- The requested API endpoint exists.
"""
        )

        with st.expander(
            "🔍 API Error Details",
            expanded=False,
        ):

            st.code(
                error_message,
                language="text",
            )

        return

    # --------------------------------------------------------
    # Server Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPIServerError,
    ):

        st.error(
            "🔥 Clinical Trial API Server Error"
        )

        st.warning(
            "FastAPI returned an internal server error "
            "while processing the clinical trial request."
        )

        with st.expander(
            "🔍 Server Error Details",
            expanded=True,
        ):

            st.code(
                error_message,
                language="text",
            )

        return

    # --------------------------------------------------------
    # Generic Trial API Error
    # --------------------------------------------------------

    if isinstance(
        error,
        TrialAPIError,
    ):

        st.error(
            "❌ Clinical Trial API Request Failed"
        )

        with st.expander(
            "🔍 API Error Details",
            expanded=True,
        ):

            st.code(
                error_message,
                language="text",
            )

        return

    # --------------------------------------------------------
    # Unexpected Application Error
    # --------------------------------------------------------

    st.error(
        "💥 Unexpected Streamlit Application Error"
    )

    with st.expander(
        "🔍 Exception Details",
        expanded=True,
    ):

        st.exception(
            error
        )


# ============================================================
# SCALAR RESPONSE RENDERER
# ============================================================

def render_scalar_response(
    key: str,
    value: Any,
) -> None:
    """
    Render scalar API response field.
    """

    label = format_field_name(
        key
    )

    if value is None:

        st.markdown(
            f"**{label}**"
        )

        st.caption(
            "Not available"
        )

        return

    if isinstance(value, bool):

        st.markdown(
            f"**{label}**"
        )

        if value:

            st.success(
                "Yes"
            )

        else:

            st.warning(
                "No"
            )

        return

    st.markdown(
        f"**{label}**"
    )

    st.write(
        value
    )


# ============================================================
# GENERIC LIST RENDERER
# ============================================================

def render_response_list(
    values: List[Any],
) -> None:
    """
    Render generic API list response.
    """

    if not values:

        st.info(
            "No records available."
        )

        return

    if all(
        isinstance(item, dict)
        for item in values
    ):

        try:

            st.dataframe(
                values,
                use_container_width=True,
                hide_index=True,
            )

            return

        except Exception:

            pass

    for index, value in enumerate(
        values,
        start=1,
    ):

        if isinstance(value, dict):

            with st.expander(
                f"Record {index}",
                expanded=False,
            ):

                render_response_dictionary(
                    value
                )

        elif isinstance(value, list):

            with st.expander(
                f"Item {index}",
                expanded=False,
            ):

                render_response_list(
                    value
                )

        else:

            st.markdown(
                f"- {value}"
            )


# ============================================================
# GENERIC DICTIONARY RENDERER
# ============================================================

def render_response_dictionary(
    response: JsonDict,
) -> None:
    """
    Render nested API dictionary.
    """

    if not response:

        st.info(
            "Empty API response."
        )

        return

    for key, value in response.items():

        if key == "success":

            continue

        label = format_field_name(
            key
        )

        if isinstance(value, dict):

            with st.expander(
                f"📊 {label}",
                expanded=True,
            ):

                render_response_dictionary(
                    value
                )

        elif isinstance(value, list):

            st.markdown(
                f"#### {label}"
            )

            render_response_list(
                value
            )

        else:

            render_scalar_response(
                key,
                value,
            )


# ============================================================
# API RESPONSE RENDERER
# ============================================================

def render_api_response(
    response: Any,
    title: str = "Clinical Trial API Response",
) -> None:
    """
    Render generic Clinical Trial API response.

    Parameters
    ----------
    response:
        API response returned by command_center_api.

    title:
        Response section title.
    """

    if response is None:

        st.info(
            "No API response available."
        )

        return

    st.subheader(
        f"📡 {title}"
    )

    success = get_response_success(
        response
    )

    message = get_response_message(
        response
    )

    # --------------------------------------------------------
    # Response Status
    # --------------------------------------------------------

    if success:

        if message:

            st.success(
                f"✅ {message}"
            )

        else:

            st.success(
                "✅ API request completed successfully."
            )

    else:

        if message:

            st.error(
                f"❌ {message}"
            )

        else:

            st.error(
                "❌ API response reported a failed status."
            )

    # --------------------------------------------------------
    # Response Metadata
    # --------------------------------------------------------

    if isinstance(response, dict):

        protocol_id = response.get(
            "protocol_id"
        )

        execution_time = (
            response.get(
                "execution_time_seconds"
            )
        )

        agent_summary = response.get(
            "agent_summary"
        )

        metadata_columns = []

        if protocol_id is not None:

            metadata_columns.append(
                (
                    "Protocol ID",
                    protocol_id,
                )
            )

        if execution_time is not None:

            metadata_columns.append(
                (
                    "Execution Time",
                    f"{execution_time} sec",
                )
            )

        if isinstance(
            agent_summary,
            dict,
        ):

            completed_agents = sum(
                1
                for status
                in agent_summary.values()
                if str(status).lower()
                == "completed"
            )

            metadata_columns.append(
                (
                    "Completed Agents",
                    (
                        f"{completed_agents}/"
                        f"{len(agent_summary)}"
                    ),
                )
            )

        if metadata_columns:

            columns = st.columns(
                len(metadata_columns)
            )

            for column, (
                label,
                value,
            ) in zip(
                columns,
                metadata_columns,
            ):

                with column:

                    st.metric(
                        label,
                        value,
                    )

    st.divider()

    # --------------------------------------------------------
    # Response Tabs
    # --------------------------------------------------------

    response_tab, json_tab = st.tabs(
        [
            "📋 Response",
            "🔍 Raw JSON",
        ]
    )

    with response_tab:

        if isinstance(response, dict):

            render_response_dictionary(
                response
            )

        elif isinstance(response, list):

            render_response_list(
                response
            )

        else:

            st.write(
                response
            )

    with json_tab:

        if isinstance(
            response,
            (
                dict,
                list,
            ),
        ):

            st.json(
                response
            )

        else:

            st.code(
                str(response),
                language="text",
            )