/**
 * ==========================================================
 * Clinical Trial Management System
 * Application Constants
 * ==========================================================
 */

/* ==========================================
   API Endpoints
========================================== */

export const API_ENDPOINTS = {
  HEALTH: "/health",
  MANAGE_TRIAL: "/manage-trial",
  GET_ALL_TRIALS: "/trials",
  GET_HISTORY: "/history",
  DELETE_TRIAL: "/delete",
  DASHBOARD: "/dashboard",
};

/* ==========================================
   Application Routes
========================================== */

export const ROUTES = {
  HOME: "/",
  HEALTH: "/health",
  DASHBOARD: "/dashboard",
  MANAGE_TRIAL: "/trial/manage",
  TRIAL_LIST: "/trial/list",
  TRIAL_HISTORY: "/trial/history",
};

/* ==========================================
   Trial Status
========================================== */

export const TRIAL_STATUS = [
  "Planned",
  "Recruiting",
  "Active",
  "Completed",
  "Suspended",
  "Terminated",
  "Withdrawn",
];

/* ==========================================
   Trial Phase
========================================== */

export const TRIAL_PHASES = [
  "Phase I",
  "Phase II",
  "Phase III",
  "Phase IV",
];

/* ==========================================
   Study Type
========================================== */

export const STUDY_TYPES = [
  "Interventional",
  "Observational",
  "Expanded Access",
];

/* ==========================================
   Therapeutic Areas
========================================== */

export const THERAPEUTIC_AREAS = [
  "Oncology",
  "Cardiology",
  "Neurology",
  "Endocrinology",
  "Dermatology",
  "Pulmonology",
  "Gastroenterology",
  "Nephrology",
  "Immunology",
  "Infectious Diseases",
];

/* ==========================================
   Regulatory Status
========================================== */

export const REGULATORY_STATUS = [
  "Pending",
  "Submitted",
  "Approved",
  "Rejected",
];

/* ==========================================
   Countries
========================================== */

export const COUNTRIES = [
  "India",
  "United States",
  "United Kingdom",
  "Germany",
  "France",
  "Canada",
  "Australia",
  "Japan",
  "Singapore",
];

/* ==========================================
   Dashboard Cards
========================================== */

export const DASHBOARD_CARDS = [
  "Total Trials",
  "Active Trials",
  "Completed Trials",
  "Recruiting Trials",
  "Subjects Enrolled",
  "Study Sites",
];

/* ==========================================
   Default Pagination
========================================== */

export const PAGINATION = {
  DEFAULT_PAGE: 1,
  DEFAULT_PAGE_SIZE: 10,
  PAGE_SIZE_OPTIONS: [10, 20, 50, 100],
};

/* ==========================================
   Date Formats
========================================== */

export const DATE_FORMAT = {
  DISPLAY: "DD-MMM-YYYY",
  API: "YYYY-MM-DD",
};

/* ==========================================
   Success Messages
========================================== */

export const SUCCESS_MESSAGES = {
  CREATE: "Clinical trial created successfully.",
  UPDATE: "Clinical trial updated successfully.",
  DELETE: "Clinical trial deleted successfully.",
  FETCH: "Data loaded successfully.",
};

/* ==========================================
   Error Messages
========================================== */

export const ERROR_MESSAGES = {
  SERVER: "Internal Server Error.",
  NETWORK: "Unable to connect to the server.",
  FETCH: "Failed to load data.",
  DELETE: "Failed to delete trial.",
  SAVE: "Failed to save clinical trial.",
};

/* ==========================================
   Local Storage Keys
========================================== */

export const STORAGE_KEYS = {
  TOKEN: "access_token",
  USER: "logged_in_user",
  THEME: "application_theme",
};

/* ==========================================
   Application Information
========================================== */

export const APP_INFO = {
  NAME: "Clinical Trial Management System",
  VERSION: "1.0.0",
  COMPANY: "Clinical Research Organization",
};

/* ==========================================
   Validation Rules
========================================== */

export const VALIDATION = {
  PROTOCOL_MIN_LENGTH: 5,
  PROTOCOL_MAX_LENGTH: 30,
  TRIAL_NAME_MAX_LENGTH: 150,
  DESCRIPTION_MAX_LENGTH: 1000,
};

/* ==========================================
   Bootstrap Colors
========================================== */

export const COLORS = {
  PRIMARY: "primary",
  SUCCESS: "success",
  WARNING: "warning",
  DANGER: "danger",
  INFO: "info",
  SECONDARY: "secondary",
};

