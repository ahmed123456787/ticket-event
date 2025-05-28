import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import {
  Search,
  ChevronDown,
  MoreVertical,
  Download,
  Eye,
  Edit,
  RefreshCw,
} from "lucide-react";

interface Order {
  id: string;
  date: string;
  buyer: {
    name: string;
    email: string;
  };
  event: string;
  amount: string;
  status: "Completed" | "Cancelled" | "Refunded" | "Pending";
}

const OrdersPage = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [filterBy, setFilterBy] = useState("Buyer");
  const [dateRange, setDateRange] = useState("Past 3 months");
  const [activeOrder, setActiveOrder] = useState<string | null>(null);

  // Sample orders data
  const orders: Order[] = [
    {
      id: "ORD-12345",
      date: "May 25, 2025",
      buyer: {
        name: "Jane Cooper",
        email: "jane@example.com",
      },
      event: "Tech Conference 2025",
      amount: "$250.00",
      status: "Completed",
    },
    {
      id: "ORD-12346",
      date: "May 22, 2025",
      buyer: {
        name: "Robert Fox",
        email: "robert@example.com",
      },
      event: "Music Festival 2025",
      amount: "$120.00",
      status: "Completed",
    },
    {
      id: "ORD-12347",
      date: "May 20, 2025",
      buyer: {
        name: "Esther Howard",
        email: "esther@example.com",
      },
      event: "Leadership Summit",
      amount: "$350.00",
      status: "Refunded",
    },
    {
      id: "ORD-12348",
      date: "May 18, 2025",
      buyer: {
        name: "Cameron Williamson",
        email: "cameron@example.com",
      },
      event: "Digital Marketing Workshop",
      amount: "$75.00",
      status: "Completed",
    },
    {
      id: "ORD-12349",
      date: "May 15, 2025",
      buyer: {
        name: "Brooklyn Simmons",
        email: "brooklyn@example.com",
      },
      event: "Charity Gala Dinner",
      amount: "$500.00",
      status: "Cancelled",
    },
  ];

  const toggleOrderActions = (orderId: string) => {
    setActiveOrder(activeOrder === orderId ? null : orderId);
  };

  const getStatusColor = (status: Order["status"]) => {
    switch (status) {
      case "Completed":
        return "bg-green-100 text-green-800";
      case "Cancelled":
        return "bg-red-100 text-red-800";
      case "Refunded":
        return "bg-orange-100 text-orange-800";
      case "Pending":
        return "bg-blue-100 text-blue-800";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  return (
    <MainLayout>
      <div className="p-6 max-w-6xl mx-auto">
        {/* Header */}
        <h1 className="text-4xl font-bold text-[#27184F] mb-2">
          Order Management
        </h1>
        <p className="text-gray-600 mb-6">
          Manage all orders, including editing buyer info, resending tickets and
          processing refunds. To download a list of orders, view the{" "}
          <a href="#" className="text-blue-500 hover:underline">
            Orders report
          </a>
          .
        </p>

        {/* Search and Filters */}
        <div className="flex flex-col md:flex-row gap-4 mb-10">
          {/* Search box */}
          <div className="relative flex-grow">
            <div className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
              <Search className="h-5 w-5 text-gray-400" />
            </div>
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search order number, email, or name"
              className="pl-10 pr-4 py-2 border border-gray-300 rounded w-full"
            />
          </div>

          {/* Date range */}
          <div className="relative w-full md:w-64">
            <button
              type="button"
              className="flex justify-between items-center w-full px-4 py-2 border border-gray-300 rounded bg-white"
              onClick={() => {
                /* Toggle date options */
              }}
            >
              <span className="text-gray-500 text-sm">Date range</span>
              <div className="flex items-center">
                <span className="mr-2">{dateRange}</span>
                <ChevronDown className="h-4 w-4" />
              </div>
            </button>
          </div>
        </div>

        {/* Order table */}
        {orders.length > 0 && (
          <div className="overflow-x-auto">
            <table className="w-full table-auto border-separate border-spacing-y-2">
              <thead>
                <tr className="text-sm text-gray-500">
                  <th className="text-left py-2 px-4 font-medium">Order #</th>
                  <th className="text-left py-2 px-4 font-medium">Date</th>
                  <th className="text-left py-2 px-4 font-medium">Buyer</th>
                  <th className="text-left py-2 px-4 font-medium">Event</th>
                  <th className="text-left py-2 px-4 font-medium">Amount</th>
                  <th className="text-left py-2 px-4 font-medium">Status</th>
                  <th className="text-right py-2 px-4 font-medium">Actions</th>
                </tr>
              </thead>
              <tbody>
                {orders.map((order) => (
                  <tr
                    key={order.id}
                    className="bg-white hover:bg-gray-50 shadow-sm"
                  >
                    <td className="py-3 px-4 rounded-l-lg">
                      <span className="font-medium text-blue-600">
                        {order.id}
                      </span>
                    </td>
                    <td className="py-3 px-4">{order.date}</td>
                    <td className="py-3 px-4">
                      <div>
                        <div className="">{order.buyer.name}</div>
                        <div className="text-sm text-gray-500">
                          {order.buyer.email}
                        </div>
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <div className="max-w-[200px] truncate">
                        {order.event}
                      </div>
                    </td>
                    <td className="py-3 px-4 ">{order.amount}</td>
                    <td className="py-3 px-4">
                      <span
                        className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${getStatusColor(
                          order.status
                        )}`}
                      >
                        {order.status}
                      </span>
                    </td>
                    <td className="py-3 px-4 rounded-r-lg text-right">
                      <div className="relative inline-block">
                        <button
                          onClick={() => toggleOrderActions(order.id)}
                          className="p-1 hover:bg-gray-100 rounded"
                        >
                          <MoreVertical className="h-5 w-5" />
                        </button>

                        {/* Dropdown menu */}
                        {activeOrder === order.id && (
                          <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg z-10 border">
                            <div className="py-1">
                              <button className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                                <Eye className="h-4 w-4 mr-2" />
                                View order
                              </button>
                              <button className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                                <Edit className="h-4 w-4 mr-2" />
                                Edit buyer info
                              </button>
                              <button className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                                <RefreshCw className="h-4 w-4 mr-2" />
                                Resend tickets
                              </button>
                              <button className="flex items-center w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">
                                <Download className="h-4 w-4 mr-2" />
                                Download tickets
                              </button>
                              {order.status !== "Refunded" &&
                                order.status !== "Cancelled" && (
                                  <button className="flex items-center w-full px-4 py-2 text-sm text-red-600 hover:bg-gray-100">
                                    <span className="h-4 w-4 mr-2">$</span>
                                    Process refund
                                  </button>
                                )}
                            </div>
                          </div>
                        )}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Pagination */}
        {orders.length > 0 && (
          <div className="flex justify-between items-center mt-6">
            <div className="text-sm text-gray-500">
              Showing <span className="font-medium">1-{orders.length}</span> of{" "}
              <span className="font-medium">{orders.length}</span> orders
            </div>
            <div className="flex space-x-2">
              <button className="px-3 py-1 border rounded bg-white text-gray-400 cursor-not-allowed">
                Previous
              </button>
              <button className="px-3 py-1 border rounded bg-white text-blue-600 hover:bg-gray-50">
                Next
              </button>
            </div>
          </div>
        )}
      </div>
    </MainLayout>
  );
};

export default OrdersPage;
