import { useState } from "react";
import { Link } from "react-router-dom";
import {
  House,
  Calendar1,
  BookText,
  BadgeDollarSign,
  ChartColumnIncreasing,
  Settings,
} from "lucide-react";

const iconSize = 26;
const iconStrokeWidth = 2;
const BASE_ROUTE = "/organizations";

const menuItems = [
  {
    title: "Home",
    icon: <House size={iconSize} strokeWidth={iconStrokeWidth} />,
    path: "/dashboard",
  },
  {
    title: "Events",
    icon: <Calendar1 size={iconSize} strokeWidth={iconStrokeWidth} />,
    path: "/events",
  },
  {
    title: "Orders",
    icon: <BookText size={iconSize} strokeWidth={iconStrokeWidth} />,
    path: "/orders",
  },
  {
    title: "Marketing",
    icon: <BadgeDollarSign size={iconSize} strokeWidth={iconStrokeWidth} />,
    path: "/marketing",
  },
  {
    title: "Reporting",
    icon: (
      <ChartColumnIncreasing size={iconSize} strokeWidth={iconStrokeWidth} />
    ),
    path: "/reporting",
  },
  {
    title: "Settings",
    icon: <Settings size={iconSize} strokeWidth={iconStrokeWidth} />,
    path: "/settings",
  },
];

const Sidebar = () => {
  const [activeItem, setActiveItem] = useState("Home");
  const [hoveredItem, setHoveredItem] = useState<string | null>(null);

  return (
    <div className="bg-gray-800 text-white flex  flex-col h-full fixed">
      <nav className="flex-1 overflow-y-auto ">
        <ul className="py-4">
          {menuItems.map((item) => (
            <li key={item.title}>
              <Link
                to={`${BASE_ROUTE}${item.path}`}
                className={`flex items-center justify-center m-2  p-1 rounded-lg mb-4 ${
                  activeItem === item.title
                    ? "bg-blue-600"
                    : "hover:bg-gray-700"
                }`}
                onClick={() => setActiveItem(item.title)}
                onMouseEnter={() => setHoveredItem(item.title)}
                onMouseLeave={() => setHoveredItem(null)}
              >
                {item.icon}
                {hoveredItem === item.title && (
                  <div className="absolute left-full ml-2 bg-gray-900 px-3 py-1 rounded text-sm ">
                    {item.title}
                  </div>
                )}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};
export default Sidebar;
