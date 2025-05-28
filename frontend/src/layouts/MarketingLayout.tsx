import MainLayout from "./MainLayout";
import MarketingNavbar from "../components/marketing/MarketingNavbar";
import { ReactNode } from "react";

const MarketingLayout = ({ children }: { children: ReactNode }) => {
  return (
    <MainLayout>
      <h2 className="text-4xl font-semibold">Marketing Tools</h2>
      <div className="mt-10">
        <MarketingNavbar />
      </div>
      {children}
    </MainLayout>
  );
};

export default MarketingLayout;
