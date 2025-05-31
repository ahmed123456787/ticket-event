import { Circle } from "lucide-react";
import { useState } from "react";

const AllowedEmail = () => {
  const [numberOfEmails] = useState(0);

  return (
    <div className="h-16 bg-gray-50 flex items-center justify-between px-8 border border-gray-200 rounded-md">
      {/* Left Section: Circle and Email Info */}
      <div className="flex items-center">
        <Circle className="text-gray-400" size={32} />
        <div className="ml-4">
          <span className="text-sm font-medium text-gray-600">Daily limit</span>
          <p className="text-lg font-semibold text-gray-300">
            {numberOfEmails} <span className="text-gray-800">/250</span>
          </p>
        </div>
      </div>

      {/* Middle Section: Informational Text */}
      <div className="text-sm text-gray-600">
        Send emails to more people when you{" "}
        <span className="text-blue-600 font-medium cursor-pointer">
          subscribe to Eventbrite Pro.
        </span>
      </div>

      {/* Right Section: Subscribe Button */}
      <button className="border border-gray-300 text-gray-700 px-4 py-2 rounded hover:bg-gray-100">
        Subscribe now
      </button>
    </div>
  );
};

export default AllowedEmail;
