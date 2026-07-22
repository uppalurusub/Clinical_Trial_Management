# 🧬 Autonomous Clinical Trial Management Platform

An enterprise-grade **AI-powered Clinical Trial Management Platform (CTMS)** that automates the planning, execution, monitoring, compliance, budgeting, and operational management of clinical trials using a **Multi-Agent AI architecture**.

The solution consists of:

- **Backend:** FastAPI + Python + AutoGen Multi-Agent Framework
- **Frontend:** React + TypeScript + Vite
- **LLM Integration:** OpenAI Compatible Models
- **Architecture:** Service-Oriented + Multi-Agent AI
- **Logging:** Loguru
- **Deployment Ready:** Docker/Kubernetes Compatible

---

# Table of Contents

- Overview
- Key Features
- System Architecture
- Technology Stack
- Project Structure
- Backend Application
- Frontend Application
- Multi-Agent Architecture
- API Endpoints
- Installation
- Running the Project
- Environment Variables
- Example Request
- Example Response
- Logging
- Future Enhancements

---

# Overview

The Autonomous Clinical Trial Management Platform streamlines the entire clinical trial lifecycle by leveraging specialized AI agents that collaborate to generate intelligent recommendations for:

- Study Design
- Site Selection
- Site Activation
- Patient Recruitment
- Enrollment Planning
- Budget Planning
- Regulatory Compliance
- Trial Monitoring
- Risk Assessment
- Financial Analysis
- Trial History Management

Instead of using a single LLM prompt, the application distributes responsibilities among multiple expert agents to improve reasoning quality and produce comprehensive clinical trial management plans.

---

# Key Features

## Clinical Trial Management

- Clinical Trial Planning
- Protocol Management
- Study Setup
- Site Selection Strategy
- Site Activation Planning
- Recruitment Strategy
- Enrollment Forecasting
- Risk-Based Monitoring
- Regulatory Compliance
- Budget Planning
- Financial Analysis
- Trial Recommendations

---

## AI Multi-Agent Workflow

Specialized AI agents collaborate to perform different clinical trial tasks.

Examples include:

- Study Setup Agent
- Site Management Agent
- Recruitment Agent
- Monitoring Agent
- Compliance Agent
- Finance Agent

---

## REST API

FastAPI exposes REST endpoints for:

- Trial Management
- Trial History
- Health Check

---

## Frontend Dashboard

React application provides:

- Clinical Trial Management Form
- Trial Recommendation Viewer
- Markdown Response Rendering
- Trial History
- API Integration
- Responsive UI

---

## Enterprise Features

- Modular Architecture
- Service Layer Pattern
- Router Layer
- Request/Response Models
- Logging
- Environment Configuration
- API Error Handling
- Scalable Folder Structure

---

# System Architecture

```
                   React Frontend
                          │
                          ▼
                Axios REST API Calls
                          │
                          ▼
                 FastAPI REST Services
                          │
                          ▼
                  Trial Router Layer
                          │
                          ▼
                 Trial Service Layer
                          │
                          ▼
           Clinical Trial Implementation
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
   Study Setup      Site Planning     Recruitment
       Agent            Agent            Agent
          │               │                │
          └───────────────┼────────────────┘
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
                    Trial Memory
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- AutoGen 0.7.5
- OpenAI API
- Loguru
- Uvicorn
- Python Dotenv
- MLflow (dependency included)

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios
- React Router
- React Markdown
- Remark GFM
- Rehype Highlight

---

# Project Structure

```
Clinical_Trial_Management/

│
├── backend/
│   └── clinical-trial-management-python-app/
│       ├── agents/
│       ├── config/
│       ├── implementation/
│       ├── memory/
│       ├── models/
│       ├── routers/
│       ├── services/
│       ├── tools/
│       ├── utils/
│       ├── logs/
│       └── main.py
│
├── ui/
│   └── reactjs/
│       └── clinical-trial-management-react-app/
│           ├── src/
│           ├── public/
│           ├── package.json
│           └── vite.config.ts
│
└── requirements.txt
```

---

# Backend Application

## Architecture

```
FastAPI
   │
Router
   │
Service
   │
Implementation
   │
AI Agents
   │
Memory
```

---

## Major Components

### Agents

Responsible for specialized AI reasoning:

- Study Setup
- Site Planning
- Recruitment
- Monitoring
- Compliance
- Finance

---

### Routers

Expose REST APIs.

---

### Services

Business logic layer.

---

### Implementation

Coordinates agent execution and workflow orchestration.

---

### Memory

Stores trial history and previous execution context.

---

### Tools

Utility modules supporting:

- CTMS
- Compliance
- Site Operations
- Financial Analysis

---

# Frontend Application

The React application provides an intuitive interface for interacting with the CTMS backend.

## Features

- Trial Management Form
- Trial History
- Markdown Rendering
- API Integration
- Error Handling
- Loading Indicators
- Responsive Layout

---

## Frontend Architecture

```
React

Pages

Components

Services

API Layer

Models

Utilities
```

---

# Multi-Agent Architecture

The backend employs multiple specialized agents that collaborate to generate a complete clinical trial management plan.

### Study Setup Agent

Responsible for:

- Protocol Review
- Trial Design
- Study Objectives

---

### Site Agent

Responsible for:

- Site Identification
- Site Selection
- Site Activation Strategy

---

### Recruitment Agent

Responsible for:

- Recruitment Strategy
- Enrollment Planning
- Patient Retention

---

### Monitoring Agent

Responsible for:

- Monitoring Schedule
- Risk Assessment
- Operational Monitoring

---

### Compliance Agent

Responsible for:

- Regulatory Validation
- Compliance Review
- Documentation Checks

---

### Finance Agent

Responsible for:

- Budget Planning
- Cost Optimization
- Financial Risk Analysis

---

# API Endpoints

## Health Check

```
GET /health
```

---

## Manage Clinical Trial

```
POST /manage-trial
```

Generates a comprehensive AI-powered clinical trial management plan.

---

## Trial History

```
GET /history/{protocol_id}
```

Returns previously managed trial information.

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd Clinical_Trial_Management
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Frontend Dependencies

```bash
cd ui/reactjs/clinical-trial-management-react-app

npm install
```

---

# Running the Backend

```bash
cd backend/clinical-trial-management-python-app

uvicorn main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

# Running the Frontend

```bash
cd ui/reactjs/clinical-trial-management-react-app

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Environment Variables

Backend `.env`

```env
OPENAI_API_KEY=your_api_key

OPENAI_MODEL=gpt-4

OPENAI_BASE_URL=https://api.openai.com/v1
```

Frontend `.env`

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

---

# Example Request

```json
{
  "protocol_id": "CT-1001",
  "trial_name": "Diabetes Phase III Trial",
  "phase": "Phase III",
  "therapeutic_area": "Endocrinology",
  "countries": [
    "USA",
    "India"
  ]
}
```

---

# Example Response

```json
{
  "status": "success",
  "trial_summary": "...",
  "study_setup": "...",
  "site_strategy": "...",
  "recruitment_plan": "...",
  "monitoring_plan": "...",
  "compliance_review": "...",
  "financial_analysis": "...",
  "recommendations": "..."
}
```

---

# Logging

Application logs are automatically generated using **Loguru**.

Example log files:

```
logs/

clinical_trial_management.log

healthcare.log

error.log
```

---

# Future Enhancements

- Database Integration (PostgreSQL / SQL Server)
- Authentication & Authorization (JWT/OAuth2)
- RBAC for Sponsors, CROs, Investigators
- Clinical Trial Dashboard
- Study Milestone Tracking
- AI Chat Assistant
- Vector Database for Protocol Search
- RAG-based Trial Knowledge Base
- ML-based Enrollment Forecasting
- Kubernetes Deployment
- CI/CD Pipelines
- Audit Trail
- Electronic Trial Master File (eTMF) Integration

---

# Highlights

- Enterprise-grade CTMS Architecture
- FastAPI REST Backend
- React TypeScript Frontend
- Multi-Agent AI Workflow
- Modular Service Architecture
- OpenAI Compatible LLM Integration
- Clinical Trial Planning Automation
- Compliance & Financial Analysis
- Trial History Management
- Production-Ready Project Structure

---
```