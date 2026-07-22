"""
sidebar.py

Clinical Trial Management System

Streamlit Sidebar Component

Responsibilities
----------------
1. Render application branding
2. Configure FastAPI base URL
3. Render application navigation
4. Display API environment information
5. Return sidebar configuration to app.py
"""

from __future__ import annotations

from typing import Tuple

import streamlit as st

from api.command_center_api import (
    DEFAULT_API_BASE_URL,
)


# ============================================================
# CONSTANTS
# ============================================================

APPLICATION_NAME = (
    "Clinical Trial Management"
)

APPLICATION_DESCRIPTION = (
    "AI-Powered Clinical Trial "
    "Management System"
)

APPLICATION_VERSION = "1.0.0"


NAVIGATION_OPTIONS = [
    "Dashboard",
    "Manage Trial",
    "Trial History",
    "All Trials",
    "Delete Trial",
    "API Health",
]


NAVIGATION_ICONS = {
    "Dashboard": "📊",
    "Manage Trial": "🧬",
    "Trial History": "📜",
    "All Trials": "📋",
    "Delete Trial": "🗑️",
    "API Health": "❤️",
}


# ============================================================
# SESSION STATE
# ============================================================

def initialize_sidebar_state() -> None:
    """
    Initialize sidebar session state.
    """

    if "api_base_url" not in st.session_state:

        st.session_state.api_base_url = (
            DEFAULT_API_BASE_URL
        )

    if "selected_page" not in st.session_state:

        st.session_state.selected_page = (
            "Dashboard"
        )


# ============================================================
# API URL NORMALIZATION
# ============================================================

def normalize_api_base_url(
    api_base_url: str,
) -> str:
    """
    Normalize FastAPI base URL.
    """

    if not api_base_url:

        return DEFAULT_API_BASE_URL

    return (
        str(api_base_url)
        .strip()
        .rstrip("/")
    )


# ============================================================
# API ENVIRONMENT
# ============================================================

def get_api_environment(
    api_base_url: str,
) -> str:
    """
    Determine API environment from URL.
    """

    normalized_url = (
        api_base_url.lower()
    )

    if (
        "localhost" in normalized_url
        or "127.0.0.1" in normalized_url
    ):

        return "LOCAL"

    if (
        "dev" in normalized_url
        or "development" in normalized_url
    ):

        return "DEVELOPMENT"

    if (
        "test" in normalized_url
        or "qa" in normalized_url
        or "uat" in normalized_url
    ):

        return "TEST / UAT"

    if (
        "prod" in normalized_url
        or "production" in normalized_url
    ):

        return "PRODUCTION"

    return "REMOTE"


# ============================================================
# APPLICATION BRANDING
# ============================================================

def render_application_branding() -> None:
    """
    Render sidebar application branding.
    """

    st.title(
        "🧪 Clinical Trials"
    )

    st.caption(
        APPLICATION_DESCRIPTION
    )

    st.divider()


# ============================================================
# API CONFIGURATION
# ============================================================

def render_api_configuration() -> str:
    """
    Render FastAPI configuration.

    Returns
    -------
    str
        Normalized FastAPI base URL.
    """

    st.subheader(
        "🔌 API Configuration"
    )

    api_base_url = st.text_input(
        "FastAPI Base URL",
        value=st.session_state.api_base_url,
        placeholder=(
            "http://localhost:8000/"
            "api/v1/trials"
        ),
        help=(
            "Enter the Clinical Trial FastAPI "
            "router base URL."
        ),
        key="sidebar_api_base_url_input",
    )

    api_base_url = normalize_api_base_url(
        api_base_url
    )

    st.session_state.api_base_url = (
        api_base_url
    )

    environment = get_api_environment(
        api_base_url
    )

    col1, col2 = st.columns(2)

    with col1:

        st.caption(
            "Environment"
        )

        st.markdown(
            f"**{environment}**"
        )

    with col2:

        st.caption(
            "API Version"
        )

        st.markdown(
            "**v1**"
        )

    with st.expander(
        "🔍 API Details",
        expanded=False,
    ):

        st.markdown(
            "**Configured Base URL**"
        )

        st.code(
            api_base_url,
            language="text",
        )

        st.markdown(
            "**Manage Trial Endpoint**"
        )

        st.code(
            (
                f"{api_base_url}/"
                "manage-trial"
            ),
            language="text",
        )

        st.markdown(
            "**API Documentation**"
        )

        docs_url = get_docs_url(
            api_base_url
        )

        st.code(
            docs_url,
            language="text",
        )

    st.divider()

    return api_base_url


# ============================================================
# API DOCUMENTATION URL
# ============================================================

def get_docs_url(
    api_base_url: str,
) -> str:
    """
    Build FastAPI Swagger documentation URL.

    Example
    -------
    API URL:
        http://localhost:8000/api/v1/trials

    Documentation URL:
        http://localhost:8000/docs
    """

    if "/api/" in api_base_url:

        root_url = api_base_url.split(
            "/api/",
            maxsplit=1,
        )[0]

        return (
            f"{root_url}/docs"
        )

    return (
        f"{api_base_url}/docs"
    )


# ============================================================
# NAVIGATION
# ============================================================

def render_navigation() -> str:
    """
    Render application navigation.

    Returns
    -------
    str
        Selected application page.
    """

    st.subheader(
        "🧭 Navigation"
    )

    selected_page = st.radio(
        "Application Pages",
        options=NAVIGATION_OPTIONS,
        index=NAVIGATION_OPTIONS.index(
            st.session_state.selected_page
        ),
        format_func=lambda page: (
            f"{NAVIGATION_ICONS.get(page, '')} "
            f"{page}"
        ),
        label_visibility="collapsed",
        key="sidebar_navigation",
    )

    st.session_state.selected_page = (
        selected_page
    )

    st.divider()

    return selected_page


# ============================================================
# APPLICATION INFORMATION
# ============================================================

def render_application_information(
    api_base_url: str,
) -> None:
    """
    Render application information.
    """

    environment = get_api_environment(
        api_base_url
    )

    with st.expander(
        "ℹ️ Application Information",
        expanded=False,
    ):

        st.markdown(
            f"""
**Application**

{APPLICATION_NAME}

**Version**

{APPLICATION_VERSION}

**Environment**

{environment}

**Frontend**

Streamlit

**Backend**

FastAPI

**Architecture**

Modular API Client + UI Components

**Domain**

Clinical Trial Management
"""
        )


# ============================================================
# SIDEBAR FOOTER
# ============================================================

def render_sidebar_footer() -> None:
    """
    Render sidebar footer.
    """

    st.divider()

    st.caption(
        "Clinical Trial Management System"
    )

    st.caption(
        f"Version {APPLICATION_VERSION}"
    )

    st.caption(
        "Streamlit + FastAPI"
    )


# ============================================================
# MAIN SIDEBAR
# ============================================================

def render_sidebar() -> Tuple[str, str]:
    """
    Render complete application sidebar.

    Returns
    -------
    Tuple[str, str]

    api_base_url:
        Clinical Trial FastAPI base URL.

    page:
        Selected navigation page.

    Usage
    -----
    api_base_url, page = render_sidebar()
    """

    initialize_sidebar_state()

    with st.sidebar:

        render_application_branding()

        api_base_url = (
            render_api_configuration()
        )

        page = render_navigation()

        render_application_information(
            api_base_url
        )

        render_sidebar_footer()

    return (
        api_base_url,
        page,
    )