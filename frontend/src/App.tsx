import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import DashboardPage from "./pages/DashboardPage";
import EventsPage from "./pages/EventsPage";
import EventCreatePage from "./pages/EventCreatePage";
import EventDetailsPage from "./pages/EventDetailsPage";
import OrdersPage from "./pages/OrdersPage";
import MarketingPage from "./pages/MarketingPage";
import MarektingEmComp from "./pages/MarektingEmComp";
import EmailCompaign from "./pages/EmailCompaign";

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
        <Route path="organizations/orders" element={<OrdersPage />} />
        <Route path="organizations/marketing" element={<MarketingPage />} />
        <Route
          path="organizations/marketing/email-campaigns"
          element={<MarektingEmComp />}
        />
        <Route
          path="organizations/marketing/email-campaigns/:campaignId"
          element={<EmailCompaign />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
