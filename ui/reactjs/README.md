# Clinical Trial Management System (CTMS)
## React JS + TypeScript + Vite

A modern Clinical Trial Management System (CTMS) frontend developed using **React JS**, **TypeScript**, **Vite**, and **React Router**. The application provides a responsive user interface for managing clinical trials, monitoring trial health, viewing historical information, and maintaining trial repositories.

---

# Table of Contents

- Overview
- Features
- Technology Stack
- Project Architecture
- Application Flow
- Folder Structure
- Routing
- Component Architecture
- API Layer
- Models
- Services
- Utilities
- Styling
- Installation
- Running the Project
- Build
- Future Enhancements

---

# Overview

This application follows a modular architecture where each responsibility is separated into its own layer.

The application consists of

- Common reusable UI components
- Feature specific Trial components
- Page components
- API layer
- Service layer
- Models
- Routing
- Layouts
- Utilities

The project follows React best practices by separating UI from business logic.

---

# Features

- Clinical Trial Repository
- Trial Management
- Trial History
- Trial Monitoring
- Trial Recruitment
- Trial Objectives
- Trial Budget
- Trial Compliance
- Trial Endpoints
- Trial Countries
- Trial Sites
- Health Monitoring Dashboard
- Responsive Layout
- Modular Architecture
- TypeScript Type Safety

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| React 19 | UI Library |
| TypeScript | Type Safety |
| Vite | Development Server & Build Tool |
| React Router | Client Side Routing |
| Axios | REST API Communication |
| CSS | Styling |

---

# Project Architecture

```
                    Browser

                       │

                  main.tsx
                       │

                    App.tsx
                       │

             BrowserRouter
                       │

              MainLayout.tsx
         ┌────────────┼────────────┐
         │            │            │
      Header       Sidebar      Footer
                       │
                       │
                 AppRoutes.tsx
                       │
        ┌──────────────┼────────────────┐
        │              │                │
 Manage Trial      Trial Repository   Health
        │              │                │
        │              │                │
   Feature Components  API Calls    Status Components
        │
   TrialService
        │
     trialApi
        │
      Axios
        │
 REST Backend API
```

---

# Application Flow

```
main.tsx

      ↓

App.tsx

      ↓

BrowserRouter

      ↓

MainLayout

      ↓

AppRoutes

      ↓

Page Component

      ↓

Feature Components

      ↓

Service Layer

      ↓

API Layer

      ↓

Backend REST API

      ↓

Response

      ↓

Models

      ↓

React Components

      ↓

UI Rendering
```

---

# Folder Structure

```
src
│
├── api
│   ├── axios.ts
│   └── trialApi.ts
│
├── assets
│
├── components
│   │
│   ├── common
│   │      Header
│   │      Sidebar
│   │      Footer
│   │      Loader
│   │
│   ├── health
│   │      HealthStatus
│   │
│   └── trial
│          TrialCard
│          TrialList
│          TrialForm
│          TrialBudget
│          TrialMonitoring
│          TrialCompliance
│          TrialCountries
│          TrialEndpoints
│          TrialObjectives
│          TrialRecruitment
│          TrialHistory
│          TrialActions
│          TrialBasicInfo
│          TrialSiteTable
│
├── layouts
│      MainLayout
│
├── models
│      Trial
│      TrialRequest
│      TrialResponse
│
├── pages
│      ManageTrialPage
│      TrialRepositoryPage
│      TrialHistoryPage
│      HealthPage
│
├── response
│      SummaryCard
│      AgentStatusCard
│      StrategyCard
│      ResponseDashboard
│
├── routes
│      AppRoutes.tsx
│
├── services
│      TrialService.ts
│
├── styles
│
├── utils
│      constants.ts
│      helpers.ts
│
├── App.tsx
├── main.tsx
└── index.css
```

---

# Routing

The application uses **React Router**.

| Route | Description |
|--------|-------------|
| /manage-trial | Trial Management |
| /trials | Trial Repository |
| /history | Trial History |
| /history/:protocolId | Trial History by Protocol |
| /health | Application Health |

---

# Component Architecture

The UI is divided into reusable components.

## Common Components

Reusable components shared across the application.

- Header
- Sidebar
- Footer
- Loader

---

## Trial Components

Domain specific components.

- Trial Form
- Trial Card
- Trial List
- Trial Budget
- Trial Compliance
- Trial Monitoring
- Trial Recruitment
- Trial Objectives
- Trial Endpoints
- Trial Countries
- Trial Site Table
- Trial History
- Trial Actions

---

## Health Components

Responsible for application health monitoring.

- Health Status

---

# Layout Architecture

```
MainLayout

├── Header

├── Sidebar

├── Main Content

└── Footer
```

The layout remains constant while only the page content changes.

---

# Service Layer

```
Page

   ↓

TrialService

   ↓

trialApi

   ↓

Axios

   ↓

Backend API
```

Responsibilities

- Business Logic
- API Calls
- Data Transformation
- Exception Handling

---

# API Layer

Located under

```
src/api
```

Contains

- Axios Configuration
- REST Endpoints
- API Requests

Example

```
Component

↓

TrialService

↓

trialApi.ts

↓

axios.ts

↓

REST API
```

---

# Models

The project uses TypeScript interfaces for strong typing.

Examples

```
Trial

TrialRequest

TrialResponse
```

Benefits

- Compile-time validation
- IntelliSense
- Reduced runtime errors
- Better maintainability

---

# Utilities

Located under

```
src/utils
```

Contains

- Application Constants
- Helper Functions

Purpose

- Avoid duplicate code
- Centralize reusable logic

---

# Styling

CSS files are organized under

```
src/styles
```

Each module has its own stylesheet.

Example

```
Header.css

Footer.css

MainLayout.css

HealthPage.css
```

This keeps styles modular and maintainable.

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate

```bash
cd project-folder
```

Install dependencies

```bash
npm install
```

---

# Running the Project

Development mode

```bash
npm run dev
```

Production build

```bash
npm run build
```

Preview production build

```bash
npm run preview
```

---

# Development Workflow

```
Create Component

        ↓

Create Service

        ↓

Create API

        ↓

Create Model

        ↓

Add Route

        ↓

Test

        ↓

Deploy
```

---

# Design Principles

The application follows

- Component Based Architecture
- Separation of Concerns
- Single Responsibility Principle
- Modular Development
- Reusable Components
- Strong Type Safety
- Responsive Layout
- Clean Folder Structure

---

# Advantages

- Easy to maintain
- Highly reusable
- Scalable architecture
- Better testing
- Easier debugging
- Type-safe development
- Faster development using reusable components

---

# Future Enhancements

- Authentication & Authorization (JWT/OAuth)
- Redux Toolkit or Zustand for State Management
- React Query / TanStack Query
- Form Validation using React Hook Form + Zod
- Lazy Loading
- Code Splitting
- Error Boundaries
- Unit Testing (Jest + React Testing Library)
- End-to-End Testing (Cypress/Playwright)
- Theme Support (Dark/Light Mode)
- Internationalization (i18n)
- Dashboard Analytics
- Notifications
- File Uploads
- Real-time Updates (WebSocket)

---

# Author

Clinical Trial Management System

Developed using

- React JS
- TypeScript
- Vite
- React Router
- Axios

Designed with a modular and scalable architecture suitable for enterprise healthcare and clinical research applications.