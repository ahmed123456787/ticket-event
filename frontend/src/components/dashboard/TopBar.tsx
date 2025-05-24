import { Plus } from "lucide-react";
import Profile from "../user/profile";
const TopBar = () => {
  return (
    <div className="flex items-center justify-between bg-[var(--bgBeigeColor)]  px-6">
      <img src="/logo.png" className="w-16" />
      <div className="flex space-x-6">
        <button className="flex items-center text-[#bc821f] font-semibold border border-[var(--bgBlueColor)] my-4 px-4 py-1 text-sm rounded-xl">
          <Plus className="w-4 h-4 items-center" />
          create
        </button>
        <Profile />
      </div>
    </div>
  );
};

export default TopBar;
