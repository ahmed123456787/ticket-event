const MarketingAnalyticsOverview = () => {
  const analyticsData = [
    {
      title: "Campaign Performance",
      value: "85%",
      description: "Overall success rate of campaigns.",
    },
    {
      title: "Click-Through Rate",
      value: "4.5%",
      description: "Average CTR across campaigns.",
    },
    {
      title: "Engagement",
      value: "1.2K",
      description: "Total user interactions.",
    },
  ];

  return (
    <div className="grid grid-cols-3 gap-4 p-4 bg-white shadow rounded">
      {analyticsData.map((data, index) => (
        <div key={index} className="p-4 border rounded">
          <h3 className="text-lg font-bold">{data.title}</h3>
          <p className="text-2xl text-blue-500 font-semibold">{data.value}</p>
          <p className="text-sm text-gray-500">{data.description}</p>
        </div>
      ))}
    </div>
  );
};

export default MarketingAnalyticsOverview;
