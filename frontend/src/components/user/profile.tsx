import { useState } from "react";
import { Settings, LogOut } from "lucide-react";

const Profile = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen((prev) => !prev);
  };

  return (
    <div className="relative flex items-center ">
      {/* Profile Button */}
      <button
        onClick={toggleDropdown}
        className="flex items-center space-x-2 px- py-1 rounded-3xl bg-gray-200 hover:bg-gray-300 transition"
      >
        <div className="flex items-center justify-center w-8 h-8 rounded-full bg-blue-500 text-white text-xs font-bold ">
          AH
        </div>
        <span className="hidden sm:block text-sm ">Ahmed</span>
      </button>

      {/* Dropdown Menu */}
      {isOpen && (
        <div className="absolute right-0 top-full mt-2 mr-5 w-48 bg-white border rounded-lg shadow-lg z-50">
          <ul className="py-2">
            <li className="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer">
              <Settings className="w-4 h-4 mr-2" />
              Account Settings
            </li>
            <li className="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer">
              <LogOut className="w-4 h-4 mr-2" />
              Log Out
            </li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default Profile;
