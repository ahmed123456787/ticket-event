import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import DashboardPage from "./pages/DashboardPage";
import EventsPage from "./pages/EventsPage";
import EventCreatePage from "./pages/EventCreatePage";
import EventDetailsPage from "./pages/EventDetailsPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="organizations/dashboard" element={<DashboardPage />} />
        <Route path="organizations/events" element={<EventsPage />} />
        <Route
          path="organizations/events/create"
          element={<EventCreatePage />}
        />
        <Route
          path="organizations/events/:eventId"
          element={<EventDetailsPage />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
