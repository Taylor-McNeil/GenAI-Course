import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import Words from "./pages/words";
import WordDetail from "./pages/wordDetail";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import Breadcrumbs from "./components/BreadCrumbs"; // ✅ Correct Import

const App = () => {
  return (
    <Router>
      <SidebarProvider>
        <div className="flex">
          {/* Sidebar on the left */}
          <AppSidebar />

          {/* Main Content Area */}
          <div className="flex flex-col w-full">
            {/* Breadcrumbs at the top */}
           
            <Breadcrumbs />

            {/* Page Content Wrapper */}
            <div className="p-6 mt-4"> {/* ✅ Added padding and margin-top */}
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/words" element={<Words />} />
                <Route path="/words/:wordId" element={<WordDetail />} /> {/* Nested route */}
              </Routes>
            </div>
          </div>
        </div>
      </SidebarProvider>
    </Router>
  );
};

export default App;
