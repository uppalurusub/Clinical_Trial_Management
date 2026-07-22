"""
app.py

Clinical Trial Management System

Streamlit Application Entry Point

Responsibilities
----------------
1. Configure Streamlit application
2. Initialize session state
3. Render application header
4. Render sidebar navigation
5. Route UI pages
6. Coordinate API and UI components
7. Handle application-level exceptions
"""

from __future__ import annotations

import streamlit as st

from api.command_center_api import (
    delete_trial,
    get_all_trials,
    get_dashboard,
    get_trial_history,
    health_check,
    manage_trial,
)

from components.agent_results import (
    render_dashboard_results,
    render_trial_history,
    render_trials,
)

from components.request_form import (
    render_manage_trial_form,
)

from components.response_view import (
    render_api_error,
    render_api_response,
)

from components.sidebar import (
    render_sidebar,
)


# ============================================================
# STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Clinical Trial Management",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SESSION STATE
# ============================================================

def initialize_session_state() -> None:
    """
    Initialize Streamlit application session state.
    """

    default_state = {
        "manage_trial_response": None,
        "trial_history": None,
        "all_trials": None,
        "dashboard_data": None,
        "delete_trial_response": None,
        "health_response": None,
    }

    for key, value in default_state.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ============================================================
# APPLICATION HEADER
# ============================================================

def render_header() -> None:
    """
    Render application header.
    """

    st.title(
        "🧪 Clinical Trial Management"
    )

    st.caption(
        "AI-powered clinical trial management, "
        "monitoring and protocol governance platform"
    )

    st.divider()


# ============================================================
# DASHBOARD PAGE
# ============================================================

def render_dashboard_page(
    api_base_url: str,
) -> None:
    """
    Render clinical trial dashboard page.
    """

    st.header(
        "📊 Trial Dashboard"
    )

    st.caption(
        "Review clinical trial dashboard information "
        "for a protocol."
    )

    protocol_id = st.text_input(
        "Protocol ID",
        placeholder="Example: PROTOCOL-001",
        key="dashboard_protocol_id",
    )

    load_dashboard = st.button(
        "Load Dashboard",
        type="primary",
        width='stretch',
        key="load_dashboard_button",
    )

    if load_dashboard:

        if not protocol_id.strip():

            st.warning(
                "Protocol ID is required."
            )

            return

        with st.spinner(
            "Loading clinical trial dashboard..."
        ):

            try:

                response = get_dashboard(
                    base_url=api_base_url,
                    protocol_id=protocol_id.strip(),
                )

                st.session_state.dashboard_data = (
                    response
                )

                st.success(
                    "Dashboard loaded successfully."
                )

            except Exception as exc:

                render_api_error(exc)

    if st.session_state.dashboard_data:

        st.divider()

        render_dashboard_results(
            st.session_state.dashboard_data
        )


# ============================================================
# MANAGE TRIAL PAGE
# ============================================================

def render_manage_trial_page(
    api_base_url: str,
) -> None:
    """
    Render manage clinical trial page.
    """

    st.header(
        "🧬 Manage Clinical Trial"
    )

    st.caption(
        "Create or manage a clinical trial protocol "
        "using the TrialRequest payload."
    )

    payload, submitted = (
        render_manage_trial_form()
    )

    if submitted:

        protocol_id = payload.get(
            "protocol_id"
        )

        if not protocol_id:

            st.warning(
                "Protocol ID is required."
            )

            return

        with st.expander(
            "📤 API Request Payload",
            expanded=False,
        ):

            st.json(payload)

        with st.spinner(
            f"Managing clinical trial "
            f"{protocol_id}..."
        ):

            try:

                response = manage_trial(
                    base_url=api_base_url,
                    payload=payload,
                )

                st.session_state.manage_trial_response = (
                    response
                )

                st.success(
                    "Clinical trial managed successfully."
                )

            except Exception as exc:

                render_api_error(exc)

    response = (
        st.session_state.manage_trial_response
    )

    if response:

        st.divider()

        render_api_response(
            response=response,
            title="Clinical Trial Result",
        )


# ============================================================
# TRIAL HISTORY PAGE
# ============================================================

def render_trial_history_page(
    api_base_url: str,
) -> None:
    """
    Render trial history page.
    """

    st.header(
        "📜 Trial History"
    )

    st.caption(
        "Retrieve clinical trial execution history "
        "using the protocol identifier."
    )

    protocol_id = st.text_input(
        "Protocol ID",
        placeholder="Example: PROTOCOL-001",
        key="history_protocol_id",
    )

    get_history = st.button(
        "Get Trial History",
        type="primary",
        width='stretch',
        key="get_history_button",
    )

    if get_history:

        if not protocol_id.strip():

            st.warning(
                "Protocol ID is required."
            )

            return

        with st.spinner(
            "Fetching trial history..."
        ):

            try:

                response = get_trial_history(
                    base_url=api_base_url,
                    protocol_id=protocol_id.strip(),
                )

                st.session_state.trial_history = (
                    response
                )

                st.success(
                    "Trial history loaded successfully."
                )

            except Exception as exc:

                render_api_error(exc)

    history = (
        st.session_state.trial_history
    )

    if history is not None:

        st.divider()

        render_trial_history(
            history
        )


# ============================================================
# ALL TRIALS PAGE
# ============================================================

def render_all_trials_page(
    api_base_url: str,
) -> None:
    """
    Render all clinical trials page.
    """

    st.header(
        "📋 All Clinical Trials"
    )

    st.caption(
        "Review all clinical trial records."
    )

    refresh_trials = st.button(
        "Refresh Trials",
        type="primary",
        width='stretch',
        key="refresh_trials_button",
    )

    if refresh_trials:

        with st.spinner(
            "Fetching clinical trial records..."
        ):

            try:

                response = get_all_trials(
                    base_url=api_base_url,
                )

                st.session_state.all_trials = (
                    response
                )

                st.success(
                    "Clinical trials loaded successfully."
                )

            except Exception as exc:

                render_api_error(exc)

    trials = (
        st.session_state.all_trials
    )

    if trials is not None:

        st.divider()

        render_trials(
            trials
        )


# ============================================================
# DELETE TRIAL PAGE
# ============================================================

def render_delete_trial_page(
    api_base_url: str,
) -> None:
    """
    Render delete clinical trial page.
    """

    st.header(
        "🗑️ Delete Clinical Trial"
    )

    st.warning(
        "Deleting a clinical trial may permanently "
        "remove the protocol record."
    )

    protocol_id = st.text_input(
        "Protocol ID",
        placeholder="Example: PROTOCOL-001",
        key="delete_protocol_id",
    )

    confirmation = st.checkbox(
        "I confirm that I want to delete this trial.",
        key="delete_confirmation",
    )

    delete_button = st.button(
        "Delete Trial",
        type="primary",
        width='stretch',
        disabled=not confirmation,
        key="delete_trial_button",
    )

    if delete_button:

        if not protocol_id.strip():

            st.warning(
                "Protocol ID is required."
            )

            return

        with st.spinner(
            f"Deleting clinical trial "
            f"{protocol_id}..."
        ):

            try:

                response = delete_trial(
                    base_url=api_base_url,
                    protocol_id=protocol_id.strip(),
                )

                st.session_state.delete_trial_response = (
                    response
                )

                st.session_state.trial_history = None
                st.session_state.all_trials = None
                st.session_state.dashboard_data = None

                st.success(
                    "Clinical trial deleted successfully."
                )

            except Exception as exc:

                render_api_error(exc)

    response = (
        st.session_state.delete_trial_response
    )

    if response:

        st.divider()

        render_api_response(
            response=response,
            title="Delete Trial Response",
        )


# ============================================================
# API HEALTH PAGE
# ============================================================

def render_api_health_page(
    api_base_url: str,
) -> None:
    """
    Render FastAPI health page.
    """

    st.header(
        "❤️ API Health Check"
    )

    st.caption(
        "Verify connectivity between the Streamlit "
        "application and FastAPI service."
    )

    check_health = st.button(
        "Check API Health",
        type="primary",
        width='stretch',
        key="health_check_button",
    )

    if check_health:

        with st.spinner(
            "Checking FastAPI service health..."
        ):

            try:

                response = health_check(
                    base_url=api_base_url,
                )

                st.session_state.health_response = (
                    response
                )

                st.success(
                    "FastAPI service is available."
                )

            except Exception as exc:

                render_api_error(exc)

    response = (
        st.session_state.health_response
    )

    if response:

        st.divider()

        render_api_response(
            response=response,
            title="API Health Response",
        )


# ============================================================
# PAGE ROUTER
# ============================================================

def route_page(
    page: str,
    api_base_url: str,
) -> None:
    """
    Route selected sidebar page.
    """

    page_routes = {
        "Dashboard": render_dashboard_page,
        "Manage Trial": render_manage_trial_page,
        "Trial History": render_trial_history_page,
        "All Trials": render_all_trials_page,
        "Delete Trial": render_delete_trial_page,
        "API Health": render_api_health_page,
    }

    page_renderer = page_routes.get(
        page
    )

    if page_renderer is None:

        st.error(
            f"Unsupported page: {page}"
        )

        return

    page_renderer(
        api_base_url
    )


# ============================================================
# APPLICATION FOOTER
# ============================================================

def render_footer() -> None:
    """
    Render application footer.
    """

    st.divider()

    st.caption(
        "Clinical Trial Management System | "
        "Streamlit + FastAPI"
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main() -> None:
    """
    Streamlit application entry point.
    """

    initialize_session_state()

    render_header()

    try:

        api_base_url, page = (
            render_sidebar()
        )

        route_page(
            page=page,
            api_base_url=api_base_url,
        )

    except Exception as exc:

        st.error(
            "Clinical Trial Management "
            "application failed."
        )

        st.exception(exc)

    render_footer()


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()