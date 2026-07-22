/**
 * Clinical Trial Domain Model
 */
export interface Trial {
  id?: number;

  protocol_id: string;

  trial_name: string;

  sponsor: string;

  indication: string;

  therapeutic_area: string;

  phase: string;

  study_type: string;

  status: string;

  start_date: string;

  end_date: string;

  planned_subjects: number;

  enrolled_subjects: number;

  completed_subjects: number;

  principal_investigator: string;

  study_site: string;

  country: string;

  regulatory_status: string;

  ethics_approval: boolean;

  description: string;

  created_at?: string;

  updated_at?: string;
}

