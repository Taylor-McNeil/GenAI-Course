import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/home";
import Words from "./pages/words";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

const App = () => {
  return (
    
    <Router>
      <SidebarProvider>
        <AppSidebar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/words" element={<Words />} />
          </Routes>
        </main>
      </SidebarProvider>
    </Router>
  )};

export default App;
