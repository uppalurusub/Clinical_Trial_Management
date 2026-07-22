/**
 * Clinical Trial Request Model
 */
export interface Site {

    site_id:string;

    site_name:string;

    country:string;

    city:string;

    principal_investigator:string;

    target_enrollment:number;

}

export interface Recruitment{

    target_patients:number;

    inclusion_criteria:string[];

    exclusion_criteria:string[];

    recruitment_channels:string[];

}

export interface Monitoring{

    monitoring_type:string;

    monitoring_frequency:string;

    remote_monitoring:boolean;

}

export interface Budget{

    total_budget:number;

    site_budget:number;

    monitoring_budget:number;

    recruitment_budget:number;

    contingency_budget:number;

}

export interface Compliance{

    regulatory_authorities:string[];

    ich_gcp_required:boolean;

    audit_required:boolean;

}

export interface TrialRequest{

    protocol_id:string;

    study_name:string;

    sponsor_name:string;

    therapeutic_area:string;

    indication:string;

    phase:string;

    study_design:string;

    start_date:string;

    end_date:string;

    countries:string[];

    sites:Site[];

    recruitment:Recruitment;

    monitoring:Monitoring;

    budget:Budget;

    compliance:Compliance;

    objectives:string[];

    primary_endpoint:string;

    secondary_endpoints:string[];

    expected_duration_months:number;

    created_by:string;

}