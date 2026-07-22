import api from "../api/axios";
import type { TrialRequest } from "../models/TrialRequest";

class TrialService {

    async health() {
        return await api.get("/health");
    }

    async getAllTrials() {
        return await api.get("/trials");
    }

    async manageTrial(request: TrialRequest) {
        return await api.post("/manage-trial", request);
    }

    async getHistory(protocolId: string) {
        return await api.get(`/history/${protocolId}`);
    }

    async deleteTrial(protocolId: string) {
        return await api.delete(`/delete/${protocolId}`);
    }

    async dashboard(protocolId: string) {
        return await api.get(`/dashboard/${protocolId}`);
    }
}

export default new TrialService();