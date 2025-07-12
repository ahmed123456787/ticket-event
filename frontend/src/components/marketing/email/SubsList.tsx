import { Search, MoreHorizontal } from "lucide-react";
import { Import, UserRoundCheck, UserX } from "lucide-react";

const SubsList = () => {
  const subscribers = [
    { name: "Def", email: "def@test", activeSubscribers: 0 },
    { name: "Tet", email: "tety", activeSubscribers: 0 },
  ];

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      {/* Header Cards */}

      <div className="grid grid-cols-4 gap-6 mb-4">
        <div className="flex flex-col items-center justify-center bg-white rounded-md shadow-md p-4">
          <Import />
          <h3 className="text-xs font-medium">Import a list</h3>
          <p className="text-xs text-gray-500 text-center">
            Upload a CSV or import an existing list
          </p>
        </div>
        <div className="flex flex-col items-center justify-center bg-white rounded-md shadow-md p-4">
          <UserRoundCheck />
          <h3 className="text-xs font-medium">All subscribers</h3>
          <p className="text-xs text-gray-500 text-center">
            Search for people across all lists
          </p>
        </div>
        <div className="flex flex-col items-center justify-center bg-white rounded-md shadow-md p-4">
          <UserX />
          <h3 className="text-xs font-medium">Unsubscribed users</h3>
          <p className="text-xs text-gray-500 text-center">
            View or delete unsubscribers
          </p>
        </div>
        <button className="bg-orange-600 text-white px-2 py-1 rounded m-7  hover:bg-orange-700">
          New List
        </button>
      </div>

      {/* Search Bar */}
      <div className="flex items-center border border-gray-300 rounded-md px-3 py-2 mb-4">
        <Search className="text-gray-400" size={16} />
        <input
          type="text"
          placeholder="Search by name"
          className="ml-2 w-full focus:outline-none"
        />
      </div>

      {/* Subscriber List Table */}
      <div className="bg-white border border-gray-200 rounded-md shadow-md">
        {/* Table Header */}
        <div className="grid grid-cols-3 px-4 py-2 border-b border-gray-200 text-sm font-medium text-gray-500">
          <span>List</span>
          <span className="text-center">Active Subscribers</span>
          <span className="text-right"></span>
        </div>

        {/* Table Rows */}
        {subscribers.map((subscriber, index) => (
          <div
            key={index}
            className="grid grid-cols-3 px-4 py-3 text-sm text-gray-700 items-center"
          >
            <div className="flex items-center">
              <div className="w-8 h-8 bg-purple-700 text-white rounded-full flex items-center justify-center">
                {subscriber.name[0]}
              </div>
              <span className="ml-3">{subscriber.email}</span>
            </div>
            <span className="text-center text-gray-500">
              {subscriber.activeSubscribers}
            </span>
            <div className="text-right text-gray-400 cursor-pointer">
              <MoreHorizontal />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SubsList;
