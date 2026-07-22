import "../../styles/Footer.css"

function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="footer">

            <div className="footer-left">
                © {currentYear} Clinical Trial Management System
            </div>

            <div className="footer-center">
                Version 1.0.0
            </div>

            <div className="footer-right">
                Powered by React • TypeScript • FastAPI
            </div>

        </footer>
    );
}

export default Footer;