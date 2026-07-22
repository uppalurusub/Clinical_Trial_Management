import api from "./axios";

import type { TrialRequest } from "../models/TrialRequest";
import type { TrialResponse } from "../models/TrialResponse";
import type { Trial } from "../models/Trial";

/**
 * ==========================================
 * Health Check
 * GET /health
 * ==========================================
 */
export const getHealth = async () => {
  const response = await api.get("/health");
  return response.data;
};

/**
 * ==========================================
 * Create / Update Clinical Trial
 * POST /manage-trial
 * ==========================================
 */
export const manageTrial = async (
  request: TrialRequest
): Promise<TrialResponse> => {

  const response =
    await api.post<TrialResponse>(
      "/manage-trial",
      request
    );

  return response.data;
};

/**
 * ==========================================
 * Get Trial History
 * GET /history/{protocol_id}
 * ==========================================
 */
export const getTrialHistory = async (
  protocolId: string
) => {

  const response =
    await api.get(
      `/history/${protocolId}`
    );

  return response.data;
};

/**
 * ==========================================
 * Get All Clinical Trials
 * GET /trials
 * ==========================================
 */
export const getAllTrials = async (): Promise<Trial[]> => {

  const response =
    await api.get<Trial[]>(
      "/trials"
    );

  return response.data;
};

/**
 * ==========================================
 * Delete Clinical Trial
 * DELETE /delete/{protocol_id}
 * ==========================================
 */
export const deleteTrial = async (
  protocolId: string
) => {

  const response =
    await api.delete(
      `/delete/${protocolId}`
    );

  return response.data;
};

/**
 * ==========================================
 * Dashboard
 * GET /dashboard/{protocol_id}
 * ==========================================
 */
export const getDashboard = async (
  protocolId: string
) => {

  const response =
    await api.get(
      `/dashboard/${protocolId}`
    );

  return response.data;
};

