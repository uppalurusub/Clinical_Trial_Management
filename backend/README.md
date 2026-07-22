# 🧬 Autonomous Clinical Trial Management Platform

An enterprise-grade **Multi-Agent Clinical Trial Management System (CTMS)** built using **AutoGen 0.7.5**, **FastAPI**, **Python**, and **LLMs** to automate end-to-end clinical trial planning, study setup, site management, recruitment strategy, compliance, monitoring, budgeting, and trial execution.

The platform leverages multiple specialized AI agents that collaboratively generate comprehensive clinical trial management plans while maintaining audit history through an in-memory trial repository.

---

# Architecture

```
                    ┌──────────────────────┐
                    │      REST API        │
                    │      FastAPI         │
                    └──────────┬───────────┘
                               │
                      Trial Router
                               │
                               ▼
                     Trial Service Layer
                               │
                               ▼
                 Trial Implementation Layer
                               │
      ┌────────────────────────┼────────────────────────┐
      │                        │                        │
      ▼                        ▼                        ▼
 Study Setup Agent       Site Agent          Recruitment Agent
      │                        │                        │
      └──────────────┬─────────┴──────────────┬────────┘
                     ▼                        ▼
              Monitoring Agent       Compliance Agent
                     │
                     ▼
               Finance Agent
                     │
                     ▼
              Trial Memory Store
```

---

# Features

- Multi-Agent Clinical Trial Planning
- Automated Study Setup
- Site Selection Strategy
- Site Activation Planning
- Patient Recruitment Planning
- Enrollment Forecasting
- Risk Based Monitoring Strategy
- Compliance Validation
- Regulatory Assessment
- Budget Planning
- Financial Analysis
- Trial Dashboard
- Trial History
- Trial Repository
- Structured JSON APIs
- Enterprise Logging using Loguru
- AutoGen 0.7.5 Integration
- Modular Architecture

---

# Multi-Agent Workflow

The platform consists of multiple autonomous AI agents.

| Agent | Responsibility |
|---------|---------------|
| Study Setup Agent | Generates protocol summary, timeline, study design and risk assessment |
| Site Agent | Site feasibility, activation plan and enrollment strategy |
| Recruitment Agent | Recruitment planning, inclusion/exclusion analysis |
| Monitoring Agent | Risk Based Monitoring strategy |
| Compliance Agent | Regulatory compliance and ICH-GCP validation |
| Finance Agent | Budget allocation and financial recommendations |

---

# Project Structure

```
Clinical_Trial_Management/
│
├── app/
│   ├── agents/
│   │     └── trial_agents.py
│   │
│   ├── config/
│   │     ├── llm_config.py
│   │     └── llm_models_config.py
│   │
│   ├── implementation/
│   │     └── trial_impl.py
│   │
│   ├── memory/
│   │     └── trial_memory.py
│   │
│   ├── models/
│   │     ├── request_model.py
│   │     └── response_model.py
│   │
│   ├── routers/
│   │     └── trial_router.py
│   │
│   ├── services/
│   │     └── trial_service.py
│   │
│   ├── tools/
│   │     ├── compliance_tools.py
│   │     ├── ctms_tools.py
│   │     ├── finance_tools.py
│   │     └── site_tools.py
│   │
│   ├── utils/
│   │     ├── logger.py
│   │     ├── json_utils.py
│   │     └── prompt_templates.py
│   │
│   └── main.py
│
├── logs/
├── manage_trial_request.json
├── requirements.txt
└── README.md
```

---

# Technology Stack

- Python 3.11+
- FastAPI
- AutoGen 0.7.5
- OpenAI / LLM Provider
- Pydantic
- Loguru
- AsyncIO

---

# Clinical Trial Lifecycle Covered

- Study Design
- Protocol Planning
- Site Selection
- Site Activation
- Patient Recruitment
- Enrollment Planning
- Budget Planning
- Compliance Validation
- Regulatory Assessment
- Monitoring Strategy
- Trial Dashboard
- Trial History

---

# REST API Endpoints

## Root

```
GET /
```

Returns application status.

---

## Health

```
GET /health
```

Application health check.

---

## Trial Module Health

```
GET /api/v1/trials/health
```

Checks trial service health.

---

## Manage Clinical Trial

```
POST /api/v1/trials/manage-trial
```

Creates a complete AI-driven clinical trial management plan.

---

## Get Trial History

```
GET /api/v1/trials/history/{protocol_id}
```

Returns historical information for a protocol.

---

## Get Dashboard

```
GET /api/v1/trials/dashboard/{protocol_id}
```

Returns dashboard data.

---

## Get All Trials

```
GET /api/v1/trials/trials
```

Lists all stored trials.

---

## Delete Trial

```
DELETE /api/v1/trials/delete/{protocol_id}
```

Deletes a protocol.

---

# Sample Request

```json
{
  "protocol_id": "PROTO-DM-2026-001",
  "study_name": "A Multicenter Phase III Study",
  "sponsor_name": "ABC Pharma Ltd",
  "therapeutic_area": "Endocrinology",
  "indication": "Type 2 Diabetes Mellitus",
  "phase": "Phase III",
  "study_design": "Randomized Double-Blind",
  "start_date": "2026-07-01",
  "end_date": "2028-06-30",
  "countries": [
    "India",
    "United States"
  ],
  "sites": [
    {
      "site_id": "SITE001",
      "site_name": "Apollo Hospital",
      "country": "India",
      "city": "Hyderabad",
      "principal_investigator": "Dr. Kumar",
      "target_enrollment": 100
    }
  ],
  "recruitment": {
    "target_patients": 500,
    "inclusion_criteria": [
      "Age >18"
    ],
    "exclusion_criteria": [
      "Pregnancy"
    ],
    "recruitment_channels": [
      "Hospital"
    ]
  },
  "monitoring": {
    "monitoring_type": "Risk Based Monitoring",
    "monitoring_frequency": "Monthly",
    "remote_monitoring": true
  },
  "budget": {
    "total_budget": 15000000,
    "site_budget": 8000000,
    "monitoring_budget": 2500000,
    "recruitment_budget": 3000000,
    "contingency_budget": 1500000
  },
  "compliance": {
    "regulatory_authorities": [
      "FDA",
      "EMA"
    ],
    "ich_gcp_required": true,
    "audit_required": true
  },
  "objectives": [
    "Evaluate efficacy"
  ],
  "primary_endpoint": "HbA1c",
  "secondary_endpoints": [
    "Weight Reduction"
  ],
  "expected_duration_months": 24,
  "created_by": "Clinical Trial Manager"
}
```

---

# Example Response

```json
{
  "success": true,
  "protocol_id": "PROTO-DM-2026-001",
  "study_setup": "...",
  "site_strategy": "...",
  "recruitment_strategy": "...",
  "monitoring_plan": "...",
  "compliance_report": "...",
  "budget_plan": "...",
  "execution_time_seconds": 18.45
}
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Clinical_Trial_Management
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
OPENAI_API_KEY=your_api_key

OPENAI_MODEL=gpt-4.1

BASE_URL=https://api.openai.com/v1
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Logging

The application uses **Loguru** for centralized logging.

Log files include:

```
logs/
│
├── clinical_trial_management.log
├── healthcare.log
├── error.log
└── medical_coding.log
```

Features:

- Console logging
- Rotating log files
- Exception tracing
- Compression
- Retention policy
- Async logging

---

# Trial Memory

The platform maintains an in-memory repository for:

- Trial History
- Dashboard Data
- Trial Retrieval
- Trial Deletion
- Trial Count

---

# AI Workflow

```
Clinical Trial Request
        │
        ▼
Study Setup Agent
        │
        ▼
Site Agent
        │
        ▼
Recruitment Agent
        │
        ▼
Monitoring Agent
        │
        ▼
Compliance Agent
        │
        ▼
Finance Agent
        │
        ▼
Merge Results
        │
        ▼
Store in Memory
        │
        ▼
Return Response
```

---

# Future Enhancements

- CTMS Database Integration
- PostgreSQL Support
- Clinical Data Repository
- RBAC Authentication
- JWT Security
- MLflow Integration
- Power BI Dashboard
- Site Performance Analytics
- Patient Recruitment Prediction
- Risk Scoring Models
- Document Management
- Trial Milestone Tracking
- Email Notifications
- Azure Deployment
- Docker & Kubernetes Support

---

# Highlights

- Enterprise-ready architecture
- AutoGen 0.7.5 Multi-Agent implementation
- FastAPI REST services
- Modular service-based design
- Clinical trial lifecycle automation
- AI-assisted study planning
- Compliance and regulatory support
- Budget and financial planning
- Comprehensive logging
- Dashboard and trial history APIs
- Easily extensible for production CTMS deployments

---

# License

This project is intended for educational, research, and enterprise accelerator purposes. Ensure compliance with applicable clinical trial regulations (such as ICH-GCP and regional regulatory requirements) before using it in production.