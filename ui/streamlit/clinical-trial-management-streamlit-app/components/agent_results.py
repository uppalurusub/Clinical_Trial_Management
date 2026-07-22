"""
agent_results.py

Clinical Trial Management System

Streamlit Trial Result Components

Responsibilities
----------------
1. Render protocol dashboard results
2. Render clinical trial history
3. Render all clinical trial records
4. Safely render nested dictionaries and lists
5. Display business metrics and structured tables
"""

from __future__ import annotations

from typing import Any, Dict, List

import pandas as pd
import streamlit as st

from utils.formatters import (
    format_field_name,
    format_metric_value,
)


# ============================================================
# TYPE ALIASES
# ============================================================

JsonDict = Dict[str, Any]
JsonList = List[Any]


# ============================================================
# VALUE HELPERS
# ============================================================

def is_scalar(
    value: Any,
) -> bool:
    """
    Determine whether value can be rendered as scalar text.
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


def is_numeric_metric(
    value: Any,
) -> bool:
    """
    Determine whether value is suitable for st.metric.
    """

    return (
        isinstance(
            value,
            (
                int,
                float,
            ),
        )
        and not isinstance(
            value,
            bool,
        )
    )


def extract_records(
    data: Any,
) -> List[Dict[str, Any]]:
    """
    Extract table-compatible records from API response.
    """

    if isinstance(data, list):

        return [
            item
            for item in data
            if isinstance(item, dict)
        ]

    if not isinstance(data, dict):

        return []

    record_keys = [
        "trials",
        "history",
        "records",
        "data",
        "results",
        "items",
    ]

    for key in record_keys:

        value = data.get(key)

        if isinstance(value, list):

            return [
                item
                for item in value
                if isinstance(item, dict)
            ]

    return []


# ============================================================
# LIST RENDERER
# ============================================================

def render_list(
    values: JsonList,
) -> None:
    """
    Render a generic list.
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

            dataframe = pd.json_normalize(
                values
            )

            st.dataframe(
                dataframe,
                use_container_width=True,
                hide_index=True,
            )

            return

        except Exception:

            pass

    for index, item in enumerate(
        values,
        start=1,
    ):

        if isinstance(item, dict):

            with st.expander(
                f"Record {index}",
                expanded=False,
            ):

                render_dictionary(
                    item
                )

        elif isinstance(item, list):

            with st.expander(
                f"Item {index}",
                expanded=False,
            ):

                render_list(
                    item
                )

        else:

            st.markdown(
                f"- {item}"
            )


# ============================================================
# DICTIONARY RENDERER
# ============================================================

def render_dictionary(
    data: JsonDict,
) -> None:
    """
    Render nested dictionary response.
    """

    if not data:

        st.info(
            "No data available."
        )

        return

    numeric_metrics = {
        key: value
        for key, value in data.items()
        if is_numeric_metric(value)
    }

    if numeric_metrics:

        metric_items = list(
            numeric_metrics.items()
        )

        for start_index in range(
            0,
            len(metric_items),
            4,
        ):

            metric_group = metric_items[
                start_index:
                start_index + 4
            ]

            columns = st.columns(
                len(metric_group)
            )

            for column, (
                key,
                value,
            ) in zip(
                columns,
                metric_group,
            ):

                with column:

                    st.metric(
                        label=format_field_name(
                            key
                        ),
                        value=format_metric_value(
                            key,
                            value,
                        ),
                    )

    for key, value in data.items():

        if key in numeric_metrics:

            continue

        title = format_field_name(
            key
        )

        if isinstance(value, dict):

            with st.expander(
                f"📊 {title}",
                expanded=True,
            ):

                render_dictionary(
                    value
                )

        elif isinstance(value, list):

            st.markdown(
                f"#### {title}"
            )

            render_list(
                value
            )

        else:

            st.markdown(
                f"**{title}**"
            )

            if value is None:

                st.caption(
                    "Not available"
                )

            elif isinstance(value, bool):

                if value:

                    st.success(
                        "Yes"
                    )

                else:

                    st.warning(
                        "No"
                    )

            else:

                st.write(
                    value
                )


# ============================================================
# PROTOCOL SUMMARY
# ============================================================

def render_protocol_summary(
    protocol_id: Any,
    dashboard: Any,
    success: bool,
) -> None:
    """
    Render protocol dashboard summary metrics.
    """

    columns = st.columns(4)

    with columns[0]:

        st.metric(
            "Protocol ID",
            (
                str(protocol_id)
                if protocol_id
                else "N/A"
            ),
        )

    with columns[1]:

        if isinstance(dashboard, list):

            record_count = len(
                dashboard
            )

        elif isinstance(dashboard, dict):

            records = extract_records(
                dashboard
            )

            record_count = (
                len(records)
                if records
                else len(dashboard)
            )

        else:

            record_count = 0

        st.metric(
            "Dashboard Records",
            record_count,
        )

    with columns[2]:

        st.metric(
            "API Status",
            (
                "SUCCESS"
                if success
                else "FAILED"
            ),
        )

    with columns[3]:

        st.metric(
            "Data Type",
            type(
                dashboard
            ).__name__.upper(),
        )


# ============================================================
# DASHBOARD RESULT
# ============================================================

def render_dashboard_results(
    response: Any,
) -> None:
    """
    Render clinical trial dashboard results.

    Expected API structure
    ----------------------
    {
        "success": true,
        "protocol_id": "...",
        "dashboard": ...
    }
    """

    if response is None:

        st.info(
            "No dashboard response available."
        )

        return

    if not isinstance(response, dict):

        st.warning(
            "Unexpected dashboard response format."
        )

        st.write(
            response
        )

        return

    success = bool(
        response.get(
            "success",
            True,
        )
    )

    protocol_id = response.get(
        "protocol_id",
        "N/A",
    )

    dashboard = response.get(
        "dashboard",
        {},
    )

    if success:

        st.success(
            "✅ Clinical trial dashboard "
            "loaded successfully."
        )

    else:

        st.error(
            "❌ Clinical trial dashboard "
            "reported a failed status."
        )

    render_protocol_summary(
        protocol_id=protocol_id,
        dashboard=dashboard,
        success=success,
    )

    st.divider()

    tabs = st.tabs(
        [
            "📊 Dashboard",
            "📋 Records",
            "🔍 Complete API Response",
        ]
    )

    with tabs[0]:

        st.subheader(
            "Clinical Trial Dashboard"
        )

        if isinstance(
            dashboard,
            dict,
        ):

            render_dictionary(
                dashboard
            )

        elif isinstance(
            dashboard,
            list,
        ):

            render_list(
                dashboard
            )

        else:

            st.write(
                dashboard
            )

    with tabs[1]:

        records = extract_records(
            dashboard
        )

        if not records and isinstance(
            dashboard,
            list,
        ):

            records = [
                item
                for item in dashboard
                if isinstance(item, dict)
            ]

        if records:

            dataframe = pd.json_normalize(
                records
            )

            st.metric(
                "Total Records",
                len(dataframe),
            )

            st.dataframe(
                dataframe,
                use_container_width=True,
                hide_index=True,
            )

        else:

            st.info(
                "No tabular dashboard "
                "records available."
            )

    with tabs[2]:

        st.json(
            response
        )


# ============================================================
# TRIAL HISTORY
# ============================================================

def render_trial_history(
    history: Any,
) -> None:
    """
    Render clinical trial protocol history.
    """

    if history is None:

        st.info(
            "No trial history available."
        )

        return

    records = extract_records(
        history
    )

    if isinstance(history, list):

        records = [
            item
            for item in history
            if isinstance(item, dict)
        ]

    record_count = len(
        records
    )

    columns = st.columns(3)

    with columns[0]:

        st.metric(
            "History Records",
            record_count,
        )

    with columns[1]:

        st.metric(
            "Response Type",
            type(
                history
            ).__name__.upper(),
        )

    with columns[2]:

        st.metric(
            "History Status",
            (
                "AVAILABLE"
                if history
                else "EMPTY"
            ),
        )

    st.divider()

    tabs = st.tabs(
        [
            "📜 Trial History",
            "🔍 JSON Response",
        ]
    )

    with tabs[0]:

        if records:

            dataframe = pd.json_normalize(
                records
            )

            st.dataframe(
                dataframe,
                use_container_width=True,
                hide_index=True,
            )

        elif isinstance(
            history,
            dict,
        ):

            render_dictionary(
                history
            )

        elif isinstance(
            history,
            list,
        ):

            if history:

                render_list(
                    history
                )

            else:

                st.info(
                    "No trial history found."
                )

        else:

            st.write(
                history
            )

    with tabs[1]:

        st.json(
            history
        )


# ============================================================
# ALL CLINICAL TRIALS
# ============================================================

def render_trials(
    trials: Any,
) -> None:
    """
    Render all clinical trial records.
    """

    if trials is None:

        st.info(
            "No clinical trial data available."
        )

        return

    records = extract_records(
        trials
    )

    if isinstance(trials, list):

        records = [
            item
            for item in trials
            if isinstance(item, dict)
        ]

    total_trials = len(
        records
    )

    columns = st.columns(3)

    with columns[0]:

        st.metric(
            "Total Trials",
            total_trials,
        )

    with columns[1]:

        protocol_ids = {
            str(
                trial.get(
                    "protocol_id"
                )
            )
            for trial in records
            if trial.get(
                "protocol_id"
            )
        }

        st.metric(
            "Unique Protocols",
            len(protocol_ids),
        )

    with columns[2]:

        st.metric(
            "Data Status",
            (
                "AVAILABLE"
                if records
                else "EMPTY"
            ),
        )

    st.divider()

    tabs = st.tabs(
        [
            "📋 Clinical Trials",
            "📊 Trial Details",
            "🔍 JSON Response",
        ]
    )

    with tabs[0]:

        if records:

            dataframe = pd.json_normalize(
                records
            )

            st.dataframe(
                dataframe,
                use_container_width=True,
                hide_index=True,
            )

        elif isinstance(
            trials,
            dict,
        ):

            render_dictionary(
                trials
            )

        else:

            st.info(
                "No clinical trial records found."
            )

    with tabs[1]:

        if not records:

            st.info(
                "No trial details available."
            )

        else:

            for index, trial in enumerate(
                records,
                start=1,
            ):

                protocol_id = trial.get(
                    "protocol_id"
                )

                trial_name = (
                    trial.get("trial_name")
                    or trial.get("study_title")
                    or trial.get("title")
                )

                label = (
                    protocol_id
                    or trial_name
                    or f"Trial {index}"
                )

                with st.expander(
                    f"🧪 {label}",
                    expanded=False,
                ):

                    render_dictionary(
                        trial
                    )

    with tabs[2]:

        st.json(
            trials
        )