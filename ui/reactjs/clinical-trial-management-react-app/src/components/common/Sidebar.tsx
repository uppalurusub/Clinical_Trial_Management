import { NavLink } from "react-router-dom";
import "../../styles/Sidebar.css"

function Sidebar() {

    return (

        <aside className="sidebar">

            <div className="logo">

                <h2>🧬 CTMS</h2>

            </div>

            <nav>

                

                <NavLink
                    to="/manage-trial"
                    className="menu-item"
                >
                    📝 Manage Trial
                </NavLink>

                <NavLink
                    to="/trials"
                    className="menu-item"
                >
                    📚 Trial Repository
                </NavLink>


                
                <NavLink 
                    to="/history"
                    className="menu-item"
                >
                    📖 Trial History
                </NavLink>

                <NavLink
                    to="/health"
                    className="menu-item"
                >
                    ❤️ System Health
                </NavLink>

            </nav>

        </aside>

    );

}

export default Sidebar;