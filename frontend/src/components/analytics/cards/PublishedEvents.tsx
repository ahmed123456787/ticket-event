import { useState } from "react";
import { Event } from "../../../types/index";
import { Link } from "react-router";

const PublishedEvents = () => {
  const [filter, setFilter] = useState("all");

  const events: Event[] = [];

  const draftCount = 1; 

  return (
    <div className="bg-white rounded-lg shadow-sm p-4 border border-gray-100">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center pb-4">
        <h2 className="text-xl font-semibold mb-2 md:mb-0">Published events</h2>
        <div className="flex space-x-2">
          <select
            className="border border-gray-300 rounded px-3 py-1 text-sm bg-white"
            value={filter}
            onChange={(e) => setFilter(e.target.value)}
          >
            <option value="all">All events</option>
            <option value="upcoming">Upcoming</option>
            <option value="past">Past</option>
          </select>
          <Link to="/organizations/events/create">
            <button className="bg-gray-900 text-white rounded px-4 py-1 text-sm hover:bg-gray-800">
              Add new event
            </button>
          </Link>
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-gray-200">
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Event
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Issued
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Remaining
              </th>
              <th className="text-left py-3 px-4 font-medium text-gray-600">
                Revenue
              </th>
            </tr>
          </thead>
          <tbody>
            {events.length > 0 ? (
              events.map((event) => (
                <tr
                  key={event.id}
                  className="border-b border-gray-100 hover:bg-gray-50"
                >
                  <td className="py-3 px-4">{event.name}</td>
                  <td className="py-3 px-4">{event.issued}</td>
                  <td className="py-3 px-4">{event.remaining}</td>
                  <td className="py-3 px-4">{event.revenue}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={4} className="py-8 text-center text-gray-500">
                  No published events.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {draftCount > 0 && (
        <div className="mt-6 text-center text-gray-700">
          You have {draftCount}{" "}
          <span className="text-blue-600 hover:underline cursor-pointer">
            draft event
          </span>
          .
        </div>
      )}
    </div>
  );
};

export default PublishedEvents;
