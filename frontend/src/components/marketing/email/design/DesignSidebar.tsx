import { useState } from "react";
import BasicInfoTab from "./tabs/BasicInfoTab";
import ContentTab from "./tabs/ContentTab";
import StyleTab from "./tabs/StyleTab";

const DesignSidebar = ({
  campaignName,
  setCampaignName,
}: {
  campaignName: string | undefined;
  setCampaignName: (name: string) => void;
}) => {
  const [activeTab, setActiveTab] = useState<"basicInfo" | "content" | "style">(
    "basicInfo"
  );

  return (
    <div className="w-full max-w-lg border-r border-gray-300 bg-white h-full">
      {/* Tab Navigation */}
      <div className="flex border-b border-gray-300">
        <button
          className={`py-4 px-6 text-base font-medium ${
            activeTab === "basicInfo"
              ? "text-blue-500 border-b-2 border-blue-600"
              : "text-gray-600 hover:text-gray-900"
          }`}
          onClick={() => setActiveTab("basicInfo")}
        >
          Basic Info
        </button>
        <button
          className={`py-4 px-6 text-base font-medium ${
            activeTab === "content"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-600 hover:text-gray-900"
          }`}
          onClick={() => setActiveTab("content")}
        >
          Content
        </button>
        <button
          className={`py-4 px-6 text-base font-medium ${
            activeTab === "style"
              ? "text-blue-600 border-b-2 border-blue-600"
              : "text-gray-600 hover:text-gray-900"
          }`}
          onClick={() => setActiveTab("style")}
        >
          Style
        </button>
      </div>

      {/* Tab Content */}
      <div className=" pt-2">
        {activeTab === "basicInfo" && (
          <BasicInfoTab
            campaignName={campaignName || ""}
            setCampaignName={setCampaignName}
          />
        )}
        {activeTab === "content" && <ContentTab />}
        {activeTab === "style" && <StyleTab />}
      </div>
    </div>
  );
};

export default DesignSidebar;
