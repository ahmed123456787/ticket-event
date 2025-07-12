interface StatCardProps {
  title: string;
  value: string | number;
  icon?: React.ReactNode;
  change?: number;
  trend?: "up" | "down" | "neutral";
}

const StatCard = ({ title, value, icon, change, trend }: StatCardProps) => {
  return (
    <div className="bg-white p-5 rounded-lg shadow-sm border border-gray-100 flex flex-col h-full hover:shadow-md transition-all">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-medium text-gray-600">{title}</h3>
        {icon && <div className="text-blue-500">{icon}</div>}
      </div>
      <div className="flex-1">
        <h3 className="text-2xl font-bold text-gray-800 mb-1">{value}</h3>
        {change !== undefined && (
          <div className="flex items-center">
            <span
              className={`text-xs font-medium ${
                trend === "up"
                  ? "text-green-500"
                  : trend === "down"
                  ? "text-red-500"
                  : "text-gray-500"
              }`}
            >
              {change > 0 ? "+" : ""}
              {change}%{trend === "up" && " ↑"}
              {trend === "down" && " ↓"}
            </span>
            <span className="text-xs text-gray-500 ml-1">vs last period</span>
          </div>
        )}
      </div>
    </div>
  );
};

export default StatCard;
