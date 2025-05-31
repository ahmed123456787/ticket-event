import { useState } from "react";

const EmailCamNavbar = () => {
  const [selectedTab, setSelectedTab] = useState("Campaigns");

  return (
    <div className="bg-white border-b border-gray-200">
      <nav className="flex gap-8 items-center p-4">
        {/* Campaigns Tab */}
        <h2
          className={`text-lg font-semibold cursor-pointer ${
            selectedTab === "Campaigns"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-700 hover:text-gray-900"
          }`}
          onClick={() => setSelectedTab("Campaigns")}
        >
          Campaigns
        </h2>

        {/* Subscribers List Tab */}
        <h2
          className={`text-lg font-semibold cursor-pointer ${
            selectedTab === "Subscribers List"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-700 hover:text-gray-900"
          }`}
          onClick={() => setSelectedTab("Subscribers List")}
        >
          Subscribers List
        </h2>
      </nav>

      {/* Render Components Based on Selected Tab */}
      <div className="p-4">
        {selectedTab === "Campaigns" && <div>Campaigns Component</div>}
        {selectedTab === "Subscribers List" && (
          <div>Subscribers List Component</div>
        )}
      </div>
    </div>
  );
};

export default EmailCamNavbar;
