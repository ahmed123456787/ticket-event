import MarketingLayout from "../layouts/MarketingLayout";
import MarketingAnalyticsOverview from "../components/analytics/MarketingAnalyticsOverview";

const MarketingPage = () => {
  return (
    <MarketingLayout>
      <div className="marketing-page-container">
        <h1 className="text-3xl font-bold m-4">Marketing Dashboard</h1>
        <MarketingAnalyticsOverview />
        {/* Add other marketing-related components here */}
      </div>
    </MarketingLayout>
  );
};

export default MarketingPage;
