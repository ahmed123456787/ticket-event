import React from "react";

interface NewCampaignContainerProps {
  campaignName: string;
  setCampaignName: (name: string) => void;
  setShowNewCampaign: (show: boolean) => void;
}

const NewCampaignContainer: React.FC<NewCampaignContainerProps> = ({
  campaignName,
  setCampaignName,
  setShowNewCampaign,
}) => {
  return (
    <div className="fixed inset-0 flex items-center justify-center  bg-opacity-50">
      <div className="bg-white p-6 rounded-md shadow-lg w-1/3">
        <h2 className="text-lg font-semibold mb-4">Create New Campaign</h2>
        <input
          type="text"
          value={campaignName}
          onChange={(e) => setCampaignName(e.target.value)}
          placeholder="Campaign Name"
          className="border border-gray-300 rounded-md px-3 py-2 w-full mb-4 focus:outline-none"
        />
        <div className="flex justify-end gap-4">
          <button
            className="bg-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-400"
            onClick={() => setShowNewCampaign(false)}
          >
            Cancel
          </button>
          <button className="bg-orange-600 text-white px-4 py-2 rounded-md hover:bg-orange-700">
            Create
          </button>
        </div>
      </div>
    </div>
  );
};

export default NewCampaignContainer;
