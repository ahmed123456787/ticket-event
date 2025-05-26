import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { Calendar, Clock, Upload, Info } from "lucide-react";

const EventCreatePage = () => {
  const [eventData, setEventData] = useState({
    name: "",
    startDate: "",
    startTime: "",
    endDate: "",
    endTime: "",
    isRecurring: false,
    venueName: "",
    venuePostcode: "",
    venueCountry: "United States",
    isOnline: false,
    description: "",
    selectedImage: null,
  });

  // Sample event images for selection
  const eventImages = [
    "/event-1.jpg",
    "/event-2.jpeg",
    "/event-3.jpg",
    "/event-4.jpeg",
    "/event5.png",
    "/event-6.jpg",
    "/welcome.svg",
    "/work.png",
    "/logo.png",
  ];

  const handleInputChange = (
    e: React.ChangeEvent<
      HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement
    >
  ) => {
    const { name, value, type } = e.target;

    if (type === "checkbox") {
      const checked = (e.target as HTMLInputElement).checked;
      setEventData((prev) => ({ ...prev, [name]: checked }));
    } else {
      setEventData((prev) => ({ ...prev, [name]: value }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Event data submitted:", eventData);
    // Here you would typically send the data to your backend
  };

  return (
    <MainLayout>
      <div className="p-4 max-w-5xl mx-auto">
        <h1 className="text-2xl font-semibold mb-6">Add event info</h1>

        <form onSubmit={handleSubmit} className="space-y-8">
          {/* Event Name */}
          <div className="space-y-2">
            <label htmlFor="name" className="block font-medium">
              Event name <span className="text-red-500">*</span>
            </label>
            <input
              type="text"
              id="name"
              name="name"
              placeholder="Enter the name of your event"
              value={eventData.name}
              onChange={handleInputChange}
              required
              className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Date and Time Section */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Starts */}
            <div>
              <label className="block font-medium mb-2">
                Starts <span className="text-red-500">*</span>
              </label>
              <div className="flex space-x-3">
                <div className="relative flex-grow">
                  <input
                    type="date"
                    name="startDate"
                    value={eventData.startDate}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <Calendar
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400"
                    size={18}
                  />
                </div>
                <div className="relative flex-grow">
                  <input
                    type="time"
                    name="startTime"
                    value={eventData.startTime}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <Clock
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400"
                    size={18}
                  />
                </div>
              </div>
            </div>

            {/* Ends */}
            <div>
              <label className="block font-medium mb-2">
                Ends <span className="text-red-500">*</span>
              </label>
              <div className="flex space-x-3">
                <div className="relative flex-grow">
                  <input
                    type="date"
                    name="endDate"
                    value={eventData.endDate}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <Calendar
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400"
                    size={18}
                  />
                </div>
                <div className="relative flex-grow">
                  <input
                    type="time"
                    name="endTime"
                    value={eventData.endTime}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <Clock
                    className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400"
                    size={18}
                  />
                </div>
              </div>
            </div>
          </div>

          {/* Recurring Event Checkbox */}
          <div className="flex items-center">
            <input
              type="checkbox"
              id="isRecurring"
              name="isRecurring"
              checked={eventData.isRecurring}
              onChange={handleInputChange}
              className="h-4 w-4 text-blue-600 border-gray-300 rounded"
            />
            <label
              htmlFor="isRecurring"
              className="ml-2 text-sm font-medium text-gray-700"
            >
              This is a recurring event
            </label>
            <button
              type="button"
              className="ml-2 text-sm text-blue-600 hover:text-blue-800 underline"
            >
              Learn more
            </button>
          </div>

          {/* Venue Information */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Venue Name */}
            <div>
              <label htmlFor="venueName" className="block font-medium mb-2">
                Venue name
              </label>
              <input
                type="text"
                id="venueName"
                name="venueName"
                placeholder="e.g. Riven Bar"
                value={eventData.venueName}
                onChange={handleInputChange}
                className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Venue Postcode */}
            <div>
              <label htmlFor="venuePostcode" className="block font-medium mb-2">
                Venue postcode / zip
              </label>
              <input
                type="text"
                id="venuePostcode"
                name="venuePostcode"
                placeholder="e.g. E1 6JD"
                value={eventData.venuePostcode}
                onChange={handleInputChange}
                className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Venue Country */}
            <div className="md:col-span-1">
              <label htmlFor="venueCountry" className="block font-medium mb-2">
                Venue country
              </label>
              <select
                id="venueCountry"
                name="venueCountry"
                value={eventData.venueCountry}
                onChange={handleInputChange}
                className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="United States">United States</option>
                <option value="United Kingdom">United Kingdom</option>
                <option value="Canada">Canada</option>
                <option value="Australia">Australia</option>
                <option value="Algeria">Algeria</option>
                <option value="France">France</option>
                <option value="Germany">Germany</option>
                <option value="Japan">Japan</option>
                <option value="Other">Other</option>
              </select>
            </div>
          </div>

          {/* Online Event Checkbox */}
          <div className="flex items-center">
            <input
              type="checkbox"
              id="isOnline"
              name="isOnline"
              checked={eventData.isOnline}
              onChange={handleInputChange}
              className="h-4 w-4 text-blue-600 border-gray-300 rounded"
            />
            <label
              htmlFor="isOnline"
              className="ml-2 text-sm font-medium text-gray-700"
            >
              This is an online event
            </label>
          </div>

          {/* Description */}
          <div>
            <label htmlFor="description" className="block font-medium mb-2">
              Description
            </label>
            <div className="border border-gray-300 rounded overflow-hidden">
              {/* Text editor toolbar */}
              <div className="flex flex-wrap gap-1 p-2 bg-gray-50 border-b">
                {/* Text formatting tools */}
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span className="font-bold">B</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span className="italic">I</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span className="underline">U</span>
                </button>
                <span className="mx-1 text-gray-300">|</span>

                {/* Alignment tools */}
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>≡</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>≡</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>≡</span>
                </button>
                <span className="mx-1 text-gray-300">|</span>

                {/* List tools */}
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>•</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>1.</span>
                </button>
                <span className="mx-1 text-gray-300">|</span>

                {/* Insert tools */}
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>🔗</span>
                </button>
                <button type="button" className="p-1 hover:bg-gray-200 rounded">
                  <span>—</span>
                </button>
              </div>

              {/* Text area */}
              <textarea
                id="description"
                name="description"
                rows={6}
                value={eventData.description}
                onChange={handleInputChange}
                placeholder="Add a description for your event"
                className="w-full p-3 focus:outline-none"
              />
            </div>
          </div>

          {/* Event Image */}
          <div>
            <label className="block font-medium mb-3">
              Choose or upload an image
            </label>
            <div className="overflow-x-auto pb-2">
              <div className="flex space-x-3">
                {eventImages.map((img, index) => (
                  <div
                    key={index}
                    onClick={() =>
                      setEventData((prev) => ({ ...prev, selectedImage: img }))
                    }
                    className={`w-16 h-16 rounded cursor-pointer border-2 flex-shrink-0 ${
                      eventData.selectedImage === img
                        ? "border-blue-500"
                        : "border-transparent"
                    }`}
                  >
                    <img
                      src={img}
                      alt={`Event background ${index + 1}`}
                      className="w-full h-full object-cover rounded"
                    />
                  </div>
                ))}
              </div>
            </div>

            {/* Upload controls */}
            <div className="flex items-center mt-4 space-x-4">
              <button
                type="button"
                className="flex items-center px-4 py-2 border border-gray-300 rounded bg-white hover:bg-gray-50"
              >
                <Upload size={18} className="mr-2" />
                Upload
              </button>
              <span className="text-gray-500 text-sm">No image</span>
            </div>
          </div>

          {/* Ticket Types Section */}
          <div className="mt-8">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold">Create ticket types</h2>
              <button
                type="button"
                className="text-xs text-blue-600 hover:text-blue-800 underline"
              >
                Use seating chart
              </button>
            </div>

            {/* Ticket buttons */}
            <div className="flex flex-wrap gap-3 mb-4">
              <button
                type="button"
                className="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-700 flex items-center"
              >
                <Plus size={16} className="mr-1" />
                Add a new ticket type
              </button>
              <button
                type="button"
                className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
              >
                Add a new ticket group
              </button>
              <button
                type="button"
                className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
              >
                Add a new bundle
              </button>
            </div>

            {/* Ticket info message */}
            <div className="bg-amber-50 border-l-4 border-amber-400 p-4 flex items-start">
              <Info size={18} className="text-amber-500 mt-0.5" />
              <p className="ml-2 text-sm text-amber-800">
                Click the Add a new ticket type button above to add a ticket to
                your event.
              </p>
            </div>
          </div>

          {/* Event Settings */}
          <div className="mt-8">
            <h2 className="text-xl font-semibold mb-4">Event settings</h2>

            {/* Timezone setting */}
            <div className="mb-4">
              <label htmlFor="timezone" className="block font-medium mb-2">
                Timezone <span className="text-red-500">*</span>
              </label>
              <select
                id="timezone"
                name="timezone"
                className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="GMT+01:00">
                  GMT+01:00) West Central Africa
                </option>
                <option value="GMT">GMT) Greenwich Mean Time</option>
                <option value="EST">EST) Eastern Standard Time</option>
                <option value="PST">PST) Pacific Standard Time</option>
                <option value="CST">CST) Central Standard Time</option>
              </select>
            </div>

            {/* Currency setting */}
            <div className="mb-4">
              <label htmlFor="currency" className="block font-medium mb-2">
                Currency
              </label>
              <div className="relative">
                <select
                  id="currency"
                  name="currency"
                  className="w-full p-2 pl-8 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="USD">$ United States Dollar</option>
                  <option value="EUR">€ Euro</option>
                  <option value="GBP">£ British Pound</option>
                  <option value="CAD">$ Canadian Dollar</option>
                  <option value="AUD">$ Australian Dollar</option>
                </select>
                <span className="absolute left-3 top-1/2 transform -translate-y-1/2">
                  $
                </span>
              </div>
            </div>

            {/* Donation option */}
            <div className="flex items-center mb-4">
              <input
                type="checkbox"
                id="allowDonation"
                name="allowDonation"
                className="h-4 w-4 text-blue-600 border-gray-300 rounded"
              />
              <label
                htmlFor="allowDonation"
                className="ml-2 text-sm font-medium text-gray-700"
              >
                Allow customers to make a donation
              </label>
            </div>

            {/* Advanced settings */}
            <div className="border-t pt-4 mt-6">
              <button
                type="button"
                className="text-sm font-semibold flex items-center"
              >
                Advanced settings
              </button>
            </div>
          </div>

          {/* Form Submit Button */}
          <div className="mt-8 flex justify-end">
            <button
              type="submit"
              className="px-6 py-2 bg-green-600 text-white font-medium rounded hover:bg-green-700"
            >
              Create Event
            </button>
          </div>
        </form>
      </div>
    </MainLayout>
  );
};

// Plus icon component for the "Add ticket type" button
const Plus = ({ size = 24, className = "" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
    className={className}
  >
    <line x1="12" y1="5" x2="12" y2="19"></line>
    <line x1="5" y1="12" x2="19" y2="12"></line>
  </svg>
);

export default EventCreatePage;
