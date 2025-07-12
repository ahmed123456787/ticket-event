import { useState } from "react";
import Comapgn from "./Comapgn";
import SubsList from "./SubsList";

const EmailCamNavbar = () => {
  const [selectedTab, setSelectedTab] = useState("Campaigns");

  return (
    <div className="bg-white border-b border-gray-200">
      <nav className="flex gap-8 items-center p-4 ">
        {/* Campaigns Tab */}
        <h2
          className={`text-sm font-semibold cursor-pointer ${
            selectedTab === "Campaigns"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-500 hover:text-gray-900"
          }`}
          onClick={() => setSelectedTab("Campaigns")}
        >
          Campaigns
        </h2>

        {/* Subscribers List Tab */}
        <h2
          className={`text-sm font-semibold cursor-pointer ${
            selectedTab === "Subscribers List"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-500 hover:text-gray-900"
          }`}
          onClick={() => setSelectedTab("Subscribers List")}
        >
          Subscribers List
        </h2>
      </nav>

      {/* Render Components Based on Selected Tab */}
      <div className="p-4">
        {selectedTab === "Campaigns" && <Comapgn />}
        {selectedTab === "Subscribers List" && <SubsList />}
      </div>
    </div>
  );
};

export default EmailCamNavbar;
