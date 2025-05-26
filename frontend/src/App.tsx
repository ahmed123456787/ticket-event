import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import DashboardPage from "./pages/DashboardPage";
import EventsPage from "./pages/EventsPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="organizations/dashboard" element={<DashboardPage />} />
        <Route path="/organizations/events" element={<EventsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
