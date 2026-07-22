"""
formatters.py

Clinical Trial Management System

Streamlit Formatting Utilities

Responsibilities
----------------
1. Format API field names
2. Format metric values
3. Format currency values
4. Format percentage values
5. Format numeric values
6. Format boolean values
7. Format dates and datetime values
8. Format protocol and status values
9. Safely convert values for Streamlit display
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, Optional


# ============================================================
# CONSTANTS
# ============================================================

CURRENCY_FIELD_TOKENS = (
    "budget",
    "cost",
    "revenue",
    "amount",
    "expense",
    "payment",
    "fund",
    "price",
    "financial",
)

PERCENTAGE_FIELD_TOKENS = (
    "percentage",
    "percent",
    "rate",
    "ratio",
    "utilization",
    "occupancy",
    "compliance",
    "progress",
)

COUNT_FIELD_TOKENS = (
    "count",
    "total",
    "number",
    "patients",
    "sites",
    "countries",
    "records",
    "trials",
    "agents",
    "enrollment",
)

DURATION_FIELD_TOKENS = (
    "duration",
    "days",
    "months",
    "weeks",
    "hours",
    "minutes",
    "seconds",
)

DATE_FIELD_TOKENS = (
    "date",
    "created_at",
    "updated_at",
    "timestamp",
    "time",
)

IDENTIFIER_FIELD_TOKENS = (
    "_id",
    "protocol_id",
    "site_id",
    "trial_id",
    "study_id",
)


# ============================================================
# FIELD NAME FORMATTER
# ============================================================

def format_field_name(
    field_name: Any,
) -> str:
    """
    Convert API field name into a readable UI label.

    Examples
    --------
    protocol_id
        -> Protocol ID

    trial_metrics
        -> Trial Metrics

    ich_gcp_required
        -> ICH GCP Required

    api_status
        -> API Status
    """

    if field_name is None:

        return ""

    value = (
        str(field_name)
        .strip()
        .replace("-", "_")
        .replace(".", "_")
    )

    words = [
        word
        for word in value.split("_")
        if word
    ]

    acronym_mapping = {
        "api": "API",
        "id": "ID",
        "ids": "IDs",
        "ai": "AI",
        "ml": "ML",
        "ich": "ICH",
        "gcp": "GCP",
        "fda": "FDA",
        "ema": "EMA",
        "mhra": "MHRA",
        "cdsco": "CDSCO",
        "tga": "TGA",
        "pmda": "PMDA",
        "cro": "CRO",
        "ctms": "CTMS",
        "kpi": "KPI",
        "kpis": "KPIs",
        "pi": "PI",
        "url": "URL",
        "uri": "URI",
        "json": "JSON",
        "http": "HTTP",
        "https": "HTTPS",
        "hba1c": "HbA1c",
        "bmi": "BMI",
    }

    formatted_words = []

    for word in words:

        normalized_word = word.lower()

        formatted_words.append(
            acronym_mapping.get(
                normalized_word,
                normalized_word.title(),
            )
        )

    return " ".join(
        formatted_words
    )


# ============================================================
# FIELD TYPE HELPERS
# ============================================================

def normalize_field_name(
    field_name: Any,
) -> str:
    """
    Normalize field name for token detection.
    """

    return (
        str(field_name or "")
        .strip()
        .lower()
    )


def field_contains_token(
    field_name: Any,
    tokens: tuple[str, ...],
) -> bool:
    """
    Determine whether field name contains a token.
    """

    normalized_field = normalize_field_name(
        field_name
    )

    return any(
        token in normalized_field
        for token in tokens
    )


def is_currency_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents currency.
    """

    return field_contains_token(
        field_name,
        CURRENCY_FIELD_TOKENS,
    )


def is_percentage_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents percentage.
    """

    return field_contains_token(
        field_name,
        PERCENTAGE_FIELD_TOKENS,
    )


def is_count_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents a count.
    """

    return field_contains_token(
        field_name,
        COUNT_FIELD_TOKENS,
    )


def is_duration_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents duration.
    """

    return field_contains_token(
        field_name,
        DURATION_FIELD_TOKENS,
    )


def is_date_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents a date/time.
    """

    return field_contains_token(
        field_name,
        DATE_FIELD_TOKENS,
    )


def is_identifier_field(
    field_name: Any,
) -> bool:
    """
    Determine whether field represents an identifier.
    """

    normalized_field = normalize_field_name(
        field_name
    )

    return (
        normalized_field.endswith("_id")
        or field_contains_token(
            normalized_field,
            IDENTIFIER_FIELD_TOKENS,
        )
    )


# ============================================================
# NUMBER FORMATTER
# ============================================================

def format_number(
    value: Any,
    decimal_places: int = 2,
) -> str:
    """
    Format numeric value.

    Examples
    --------
    500
        -> 500

    1500000
        -> 1,500,000

    1234.567
        -> 1,234.57
    """

    if value is None:

        return "N/A"

    if isinstance(value, bool):

        return format_boolean(
            value
        )

    try:

        numeric_value = float(
            value
        )

    except (
        TypeError,
        ValueError,
    ):

        return str(
            value
        )

    if numeric_value.is_integer():

        return f"{int(numeric_value):,}"

    return (
        f"{numeric_value:,.{decimal_places}f}"
    )


# ============================================================
# CURRENCY FORMATTER
# ============================================================

def format_currency(
    value: Any,
    currency_symbol: str = "$",
    decimal_places: int = 2,
    compact: bool = False,
) -> str:
    """
    Format currency value.

    Examples
    --------
    15000000
        -> $15,000,000.00

    compact=True
        -> $15.00M
    """

    if value is None:

        return "N/A"

    try:

        numeric_value = float(
            value
        )

    except (
        TypeError,
        ValueError,
    ):

        return str(
            value
        )

    if compact:

        return format_compact_currency(
            numeric_value,
            currency_symbol,
        )

    return (
        f"{currency_symbol}"
        f"{numeric_value:,.{decimal_places}f}"
    )


# ============================================================
# COMPACT CURRENCY FORMATTER
# ============================================================

def format_compact_currency(
    value: Any,
    currency_symbol: str = "$",
) -> str:
    """
    Format large currency values.

    Examples
    --------
    15000000
        -> $15.00M

    2500000000
        -> $2.50B
    """

    if value is None:

        return "N/A"

    try:

        numeric_value = float(
            value
        )

    except (
        TypeError,
        ValueError,
    ):

        return str(
            value
        )

    absolute_value = abs(
        numeric_value
    )

    if absolute_value >= 1_000_000_000:

        return (
            f"{currency_symbol}"
            f"{numeric_value / 1_000_000_000:,.2f}B"
        )

    if absolute_value >= 1_000_000:

        return (
            f"{currency_symbol}"
            f"{numeric_value / 1_000_000:,.2f}M"
        )

    if absolute_value >= 1_000:

        return (
            f"{currency_symbol}"
            f"{numeric_value / 1_000:,.2f}K"
        )

    return (
        f"{currency_symbol}"
        f"{numeric_value:,.2f}"
    )


# ============================================================
# PERCENTAGE FORMATTER
# ============================================================

def format_percentage(
    value: Any,
    decimal_places: int = 2,
    decimal_ratio: bool = False,
) -> str:
    """
    Format percentage value.

    Parameters
    ----------
    decimal_ratio:
        When True, 0.75 is displayed as 75.00%.

        When False, 75 is displayed as 75.00%.
    """

    if value is None:

        return "N/A"

    try:

        numeric_value = float(
            value
        )

    except (
        TypeError,
        ValueError,
    ):

        return str(
            value
        )

    if decimal_ratio:

        numeric_value *= 100

    return (
        f"{numeric_value:,.{decimal_places}f}%"
    )


# ============================================================
# BOOLEAN FORMATTER
# ============================================================

def format_boolean(
    value: Any,
) -> str:
    """
    Format boolean values.
    """

    if value is None:

        return "N/A"

    if isinstance(value, bool):

        return (
            "Yes"
            if value
            else "No"
        )

    normalized_value = (
        str(value)
        .strip()
        .lower()
    )

    if normalized_value in {
        "true",
        "yes",
        "1",
    }:

        return "Yes"

    if normalized_value in {
        "false",
        "no",
        "0",
    }:

        return "No"

    return str(
        value
    )


# ============================================================
# DATE FORMATTER
# ============================================================

def format_date(
    value: Any,
    output_format: str = "%d %b %Y",
) -> str:
    """
    Format date values.

    Examples
    --------
    2026-07-01
        -> 01 Jul 2026
    """

    if value is None:

        return "N/A"

    if isinstance(value, datetime):

        return value.strftime(
            output_format
        )

    if isinstance(value, date):

        return value.strftime(
            output_format
        )

    string_value = str(
        value
    ).strip()

    datetime_formats = (
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
    )

    normalized_value = (
        string_value
        .replace("Z", "")
    )

    for datetime_format in datetime_formats:

        try:

            parsed_value = datetime.strptime(
                normalized_value,
                datetime_format,
            )

            return parsed_value.strftime(
                output_format
            )

        except ValueError:

            continue

    return string_value


# ============================================================
# DATETIME FORMATTER
# ============================================================

def format_datetime(
    value: Any,
    output_format: str = "%d %b %Y %H:%M:%S",
) -> str:
    """
    Format datetime values.
    """

    if value is None:

        return "N/A"

    if isinstance(value, datetime):

        return value.strftime(
            output_format
        )

    if isinstance(value, date):

        return datetime.combine(
            value,
            datetime.min.time(),
        ).strftime(
            output_format
        )

    string_value = str(
        value
    ).strip()

    normalized_value = (
        string_value
        .replace("Z", "+00:00")
    )

    try:

        parsed_value = datetime.fromisoformat(
            normalized_value
        )

        return parsed_value.strftime(
            output_format
        )

    except ValueError:

        return string_value


# ============================================================
# STATUS FORMATTER
# ============================================================

def format_status(
    value: Any,
) -> str:
    """
    Format API/trial status value.
    """

    if value is None:

        return "N/A"

    return (
        str(value)
        .strip()
        .replace("_", " ")
        .replace("-", " ")
        .upper()
    )


# ============================================================
# DURATION FORMATTER
# ============================================================

def format_duration(
    field_name: Any,
    value: Any,
) -> str:
    """
    Format duration based on field name.
    """

    formatted_value = format_number(
        value
    )

    normalized_field = normalize_field_name(
        field_name
    )

    duration_units = {
        "seconds": "sec",
        "minutes": "min",
        "hours": "hrs",
        "days": "days",
        "weeks": "weeks",
        "months": "months",
    }

    for token, unit in duration_units.items():

        if token in normalized_field:

            return (
                f"{formatted_value} {unit}"
            )

    return formatted_value


# ============================================================
# GENERIC VALUE FORMATTER
# ============================================================

def format_value(
    field_name: Any,
    value: Any,
) -> str:
    """
    Format API value based on field semantics.
    """

    if value is None:

        return "N/A"

    if isinstance(value, bool):

        return format_boolean(
            value
        )

    if is_identifier_field(
        field_name
    ):

        return str(
            value
        )

    if is_date_field(
        field_name
    ):

        if "time" in normalize_field_name(
            field_name
        ):

            return format_datetime(
                value
            )

        return format_date(
            value
        )

    if is_currency_field(
        field_name
    ):

        return format_currency(
            value
        )

    if is_percentage_field(
        field_name
    ):

        return format_percentage(
            value
        )

    if is_duration_field(
        field_name
    ):

        return format_duration(
            field_name,
            value,
        )

    if isinstance(
        value,
        (
            int,
            float,
            Decimal,
        ),
    ):

        return format_number(
            value
        )

    return str(
        value
    )


# ============================================================
# STREAMLIT METRIC VALUE FORMATTER
# ============================================================

def format_metric_value(
    key: Any,
    value: Any,
) -> str:
    """
    Format value for Streamlit st.metric.

    Used by
    -------
    components.agent_results.render_dictionary()
    """

    if value is None:

        return "N/A"

    normalized_key = normalize_field_name(
        key
    )

    if isinstance(value, bool):

        return format_boolean(
            value
        )

    if is_identifier_field(
        normalized_key
    ):

        return str(
            value
        )

    if is_currency_field(
        normalized_key
    ):

        return format_compact_currency(
            value
        )

    if is_percentage_field(
        normalized_key
    ):

        return format_percentage(
            value
        )

    if is_duration_field(
        normalized_key
    ):

        return format_duration(
            normalized_key,
            value,
        )

    if isinstance(
        value,
        (
            int,
            float,
            Decimal,
        ),
    ):

        return format_number(
            value
        )

    return str(
        value
    )


# ============================================================
# OPTIONAL VALUE FORMATTER
# ============================================================

def format_optional_value(
    value: Any,
    default: str = "N/A",
) -> str:
    """
    Safely format optional value.
    """

    if value is None:

        return default

    if isinstance(value, str):

        normalized_value = (
            value.strip()
        )

        return (
            normalized_value
            if normalized_value
            else default
        )

    return str(
        value
    )


# ============================================================
# TEXT TRUNCATION
# ============================================================

def truncate_text(
    value: Any,
    max_length: int = 100,
    suffix: str = "...",
) -> str:
    """
    Truncate long text for table/card display.
    """

    if value is None:

        return "N/A"

    text = str(
        value
    )

    if len(text) <= max_length:

        return text

    truncate_length = max(
        0,
        max_length - len(suffix),
    )

    return (
        f"{text[:truncate_length]}"
        f"{suffix}"
    )