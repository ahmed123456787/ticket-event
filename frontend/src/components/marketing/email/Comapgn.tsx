import { ChevronDown, Search } from "lucide-react";
import { useState } from "react";
import NewCampaignContainer from "./NewCampaignContainer";

const Comapgn = () => {
  const [showFilter, setShowFilter] = useState(false);
  const filterOptions = ["Draft", "Published", "Archived"];
  const [showNewCampaign, setShowNewCampaign] = useState(false);
  const [campaignName, setCampaignName] = useState("");

  return (
    <div className="flex flex-col bg-white p-8 rounded-lg shadow-xl w-full relative">
      {/* Header Section */}
      <div className="flex items-center justify-between mb-6">
        {/* Search Input */}
        <div className="flex items-center border border-gray-300 rounded-lg px-4 py-2 w-1/3">
          <Search className="text-gray-400" size={20} />
          <input
            type="text"
            placeholder="Search by name"
            className="ml-3 w-full focus:outline-none text-sm"
          />
        </div>
        {/* Filter Dropdown */}
        <div className="relative">
          <div
            className="flex items-center border border-gray-300 rounded-lg px-4 py-2 gap-4 cursor-pointer hover:bg-gray-100"
            onClick={() => setShowFilter(!showFilter)}
          >
            <span className="text-gray-500 text-sm">Filter by status</span>
            <ChevronDown className="ml-auto text-gray-400" size={20} />
          </div>
          {showFilter && (
            <div className="absolute mt-2 bg-white border border-gray-300 rounded-lg shadow-lg w-full z-10">
              {filterOptions.map((option, index) => (
                <div
                  key={index}
                  className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer"
                >
                  {option}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* New Campaign Button */}
        <button
          className="bg-orange-500 text-white px-5 py-2 rounded-lg hover:bg-orange-600 text-sm font-medium"
          onClick={() => setShowNewCampaign(true)}
        >
          New Campaign
        </button>
      </div>

      {/* New Campaign Container */}
      {showNewCampaign && (
        <div className="z-20 relative">
          <NewCampaignContainer
            campaignName={campaignName}
            setCampaignName={setCampaignName}
            setShowNewCampaign={setShowNewCampaign}
          />
        </div>
      )}

      {/* Campaign Table */}
      <div className="bg-gray-50 border border-gray-200 rounded-lg overflow-hidden">
        {/* Table Header */}
        <div className="grid grid-cols-5 px-6 py-3 border-b border-gray-300 text-sm font-semibold text-gray-600 bg-gray-100">
          <span className="col-span-2">Campaigns</span>
          <span className="text-center">Opened</span>
          <span className="text-center">Clicks</span>
          <span className="text-center">Status</span>
        </div>

        {/* Table Row */}
        <div className="bg-white grid grid-cols-5 px-6 py-4 text-sm text-gray-700 hover:bg-gray-50">
          <div className="flex items-center col-span-2">
            <div className="w-10 h-10 bg-gray-200 rounded-full"></div>
            <span className="ml-4">def@gmail.com</span>
          </div>
          <span className="text-center text-gray-500">--</span>
          <span className="text-center text-gray-500">--</span>
          <span className="text-center">
            <span className="text-xs bg-gray-200 text-gray-600 px-3 py-1 rounded-full">
              Draft
            </span>
          </span>
        </div>
      </div>
    </div>
  );
};

export default Comapgn;
