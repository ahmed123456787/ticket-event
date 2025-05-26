import { useState } from "react";
import { Activity } from "../../../types/index";
import { ChevronDown } from "lucide-react";

const RecentActivity = () => {
  const [filter, setFilter] = useState("orders");

  const activities: Activity[] = [];

  return (
    <div className="bg-white rounded-lg shadow-sm p-4 border border-gray-100">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center pb-4">
        <h2 className="text-xl font-semibold mb-2 md:mb-0">Recent activity</h2>
        <div className="relative">
          <button
            className="border border-gray-300 rounded px-4 py-1 text-sm bg-white flex items-center"
            onClick={() => {}}
          >
            Orders only
            <ChevronDown />
          </button>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-gray-200">
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Time
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Name
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Event or store
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Value
              </th>
            </tr>
          </thead>
          <tbody>
            {activities.length > 0 ? (
              activities.map((activity) => (
                <tr
                  key={activity.id}
                  className="border-b border-gray-100 hover:bg-gray-50"
                >
                  <td className="py-3 px-4">{activity.time}</td>
                  <td className="py-3 px-4">{activity.name}</td>
                  <td className="py-3 px-4">{activity.eventOrStore}</td>
                  <td className="py-3 px-4">{activity.value}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={4} className="py-8 text-center text-gray-500">
                  No recent activity.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default RecentActivity;
