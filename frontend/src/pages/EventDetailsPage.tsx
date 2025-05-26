import { useParams } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";

const EventDetailsPage = () => {
  const { eventId } = useParams();

  return (
    <MainLayout>
      <div className="p-4">
        <h1 className="text-2xl font-bold mb-4">Event Details</h1>
        <p>Details for event ID: {eventId}</p>
        {/* Event details content will go here */}
      </div>
    </MainLayout>
  );
};

export default EventDetailsPage;
