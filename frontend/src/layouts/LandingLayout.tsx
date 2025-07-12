import Service from "../components/home/Service";
import Demo from "../components/home/Demo";
import TopBar from "../components/home/TopBar";
import Work from "../components/home/Work";
import { ReactNode } from "react";

const LandingLayout = ({ children }: { children: ReactNode }) => {
  return (
    <div className="w-full min-h-screen overflow-x-hidden">
      <TopBar />
      <main className="w-full px-4 sm:px-0">
        <Demo />
        <Service />
        <Work />
        {/* <div className="py-4 sm:py-6 md:py-8">{children}</div> */}
      </main>
    </div>
  );
};

export default LandingLayout;
