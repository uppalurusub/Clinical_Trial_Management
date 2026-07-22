import type { Trial } from "./Trial";

/**
 * Clinical Trial API Response Model
 */
export interface TrialResponse {
  success: boolean;

  message: string;

  protocol_id: string;

  trial?: Trial;

  data?: Trial | Trial[];

  errors?: string[];

  timestamp?: string;
}

