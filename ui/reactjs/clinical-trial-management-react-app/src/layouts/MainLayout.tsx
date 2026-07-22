import { ReactNode } from "react";
import "../styles/MainLayout.css"
import Header from "../components/common/Header";
import Sidebar from "../components/common/Sidebar";
import Footer from "../components/common/Footer";



interface Props {
    children: ReactNode;
}

function MainLayout({ children }: Props) {

    return (

        <div className="app-container">

            <Header />

            <div className="body-container">

                <Sidebar />

                <main className="main-content">

                    {children}

                </main>

            </div>

            <Footer />

        </div>

    );

}

export default MainLayout;