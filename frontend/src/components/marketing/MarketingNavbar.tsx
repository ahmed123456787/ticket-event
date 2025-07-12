import { Link, useLocation } from "react-router";
const BASE_URL = "/organizations/marketing";

const MarketingNavbar = () => {
  const location = useLocation();
  const navItems = [
    { name: "Dashboard", link: "" },
    { name: "Email Campaigns", link: "/email-campaigns" },
    { name: "Social Media", link: "/social-media" },
    { name: "Settings", link: "/settings" },
  ];

  const isActive = (path: string) => {
    return location.pathname === `${BASE_URL}${path}`;
  };

  return (
    <div className="flex space-x-12">
      {navItems.map((item) => (
        <Link
          to={`${BASE_URL}${item.link}`}
          key={item.name}
          className={`text-sm transition-colors ${
            isActive(item.link)
              ? "text-blue-500 border-b-2 border-blue-600 font-medium"
              : "text-gray-500 hover:text-black"
          }`}
        >
          {item.name}
        </Link>
      ))}
    </div>
  );
};

export default MarketingNavbar;
