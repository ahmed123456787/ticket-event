import { Link } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";

const EventsPage = () => {
  // Mock events data
  const events = [
    { id: 1, title: "Concert in the Park", date: "2025-06-15" },
    { id: 2, title: "Tech Conference 2025", date: "2025-07-22" },
    { id: 3, title: "Food Festival", date: "2025-08-10" },
  ];

  return (
    <MainLayout>
      <div className="p-4">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold">Events</h1>
          <Link
            to="/organizations/events/create"
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
          >
            Create New Event
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {events.map((event) => (
            <div key={event.id} className="border rounded-lg p-4 shadow-sm">
              <h3 className="text-lg font-semibold">{event.title}</h3>
              <p className="text-gray-600 mb-3">Date: {event.date}</p>
              <Link
                to={`/organizations/events/${event.id}`}
                className="text-blue-500 hover:underline"
              >
                View Details
              </Link>
            </div>
          ))}
        </div>
      </div>
    </MainLayout>
  );
};

export default EventsPage;
