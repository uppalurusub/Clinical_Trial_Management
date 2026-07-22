import "../../styles/Header.css"

function Header() {
    return (
        <header className="header">

            <div className="header-left">
                <h2>🧬 CTMS</h2>
                <span>Clinical Trial Management System</span>
            </div>

            <div className="header-center">
                <input
                    type="text"
                    placeholder="Search protocol..."
                />
            </div>

            <div className="header-right">

                <button>🔔 3</button>

                <button>❤️ Health</button>

                <button>👤 Admin ▼</button>

            </div>

        </header>
    );
}

export default Header;