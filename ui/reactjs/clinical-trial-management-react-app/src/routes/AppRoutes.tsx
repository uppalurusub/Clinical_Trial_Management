import { Routes, Route } from "react-router-dom";


import ManageTrialPage from "../pages/ManageTrialPage";
import TrialHistoryPage from "../pages/TrialHistoryPage";
import HealthPage from "../pages/HealthPage";
import TrialRepositoryPage from "../pages/TrialRepositoryPage";



function AppRoutes() {

    return (

        <Routes>

            

            <Route
                path="/manage-trial"
                element={<ManageTrialPage />}
            />

            <Route
                path="/trials"
                element={<TrialRepositoryPage />}
            />

            <Route
                path="/history"
                element={<TrialHistoryPage />}
            />

            <Route
                path="/history/:protocolId"
                element={<TrialHistoryPage />}
            />

            <Route
                path="/health"
                element={<HealthPage />}
            />

        </Routes>

    );

}

export default AppRoutes;