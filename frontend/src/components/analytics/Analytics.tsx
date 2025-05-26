import { useState } from "react";
import StatCard from "./cards/StatCard";
import PublishedEvents from "./cards/PublishedEvents";
import RecentActivity from "./cards/RecentActivity";
import {
  FiUsers,
  FiShoppingBag,
  FiCreditCard,
  FiDollarSign,
} from "react-icons/fi";

const Analytics = () => {
  const [selectedFilter, setSelectedFilter] = useState("today");

  const filters = [
    { id: "today", label: "Today" },
    { id: "yesterday", label: "Yesterday" },
    { id: "week", label: "This Week" },
    { id: "month", label: "This Month" },
    { id: "year", label: "This Year" },
  ];

  // Mock data for demonstration
  const analyticsData = {
    today: {
      users: { value: 342, change: 12, trend: "up" },
      orders: { value: 85, change: 5.7, trend: "up" },
      ticketsSold: { value: 128, change: -2.3, trend: "down" },
      revenue: { value: "$4,265", change: 8.2, trend: "up" },
    },
    yesterday: {
      users: { value: 305, change: 4, trend: "up" },
      orders: { value: 81, change: -1.2, trend: "down" },
      ticketsSold: { value: 131, change: 3.5, trend: "up" },
      revenue: { value: "$3,940", change: -1.8, trend: "down" },
    },
    week: {
      users: { value: 1245, change: 15.3, trend: "up" },
      orders: { value: 382, change: 11.2, trend: "up" },
      ticketsSold: { value: 648, change: 9.8, trend: "up" },
      revenue: { value: "$18,675", change: 12.7, trend: "up" },
    },
    month: {
      users: { value: 4826, change: 23.6, trend: "up" },
      orders: { value: 1658, change: 17.5, trend: "up" },
      ticketsSold: { value: 2843, change: 14.2, trend: "up" },
      revenue: { value: "$78,426", change: 18.3, trend: "up" },
    },
    year: {
      users: { value: 28457, change: 43.2, trend: "up" },
      orders: { value: 9268, change: 37.8, trend: "up" },
      ticketsSold: { value: 15643, change: 32.6, trend: "up" },
      revenue: { value: "$342,896", change: 45.1, trend: "up" },
    },
  };

  const currentData =
    analyticsData[selectedFilter as keyof typeof analyticsData];

  const handleFilterChange = (filterId: string) => {
    setSelectedFilter(filterId);
  };

  return (
    <div className="flex flex-col space-y-6">
      {/* The analytics stats section */}
      <div className="flex flex-col bg-white p-4 rounded-lg shadow-sm">
        {/* The analytics title and filter */}
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center pb-6 border-b">
          <h2 className="text-xl font-bold mb-4 md:mb-0">Analytics</h2>
          <div className="flex flex-wrap w-full md:w-auto space-x-1 bg-gray-100 rounded-lg p-1">
            {filters.map((filter) => (
              <button
                key={filter.id}
                className={`px-3 py-1 text-sm rounded-md transition-all ${
                  selectedFilter === filter.id
                    ? "bg-white shadow-sm text-blue-600 font-medium"
                    : "text-gray-500 hover:text-gray-700"
                }`}
                onClick={() => handleFilterChange(filter.id)}
              >
                {filter.label}
              </button>
            ))}
          </div>
        </div>

        {/* Stats grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          <StatCard
            title="Total Users"
            value={currentData.users.value}
            icon={<FiUsers size={20} />}
            change={currentData.users.change}
            trend={currentData.users.trend as "up" | "down" | "neutral"}
          />

          <StatCard
            title="Orders"
            value={currentData.orders.value}
            icon={<FiShoppingBag size={20} />}
            change={currentData.orders.change}
            trend={currentData.orders.trend as "up" | "down" | "neutral"}
          />

          <StatCard
            title="Tickets Sold"
            value={currentData.ticketsSold.value}
            icon={<FiCreditCard size={20} />}
            change={currentData.ticketsSold.change}
            trend={currentData.ticketsSold.trend as "up" | "down" | "neutral"}
          />

          <StatCard
            title="Total Revenue"
            value={currentData.revenue.value}
            icon={<FiDollarSign size={20} />}
            change={currentData.revenue.change}
            trend={currentData.revenue.trend as "up" | "down" | "neutral"}
          />
        </div>
      </div>

      {/* Activity and Events section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <RecentActivity />
        <PublishedEvents />
      </div>
    </div>
  );
};

export default Analytics;
