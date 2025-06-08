import TopBar from "../components/dashboard/TopBar";
import Sidebar from "../components/dashboard/Sidebar";

const MainLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex flex-col h-screen">
      <TopBar />
      <div className="flex flex-1 overflow-hidden">
        <div className=" flex-shrink-0">
          <Sidebar />
        </div>
        <main className="flex-1  sm:px-0 md:px-16  mt-12 overflow-y-auto ">
          {children}
        </main>
      </div>
    </div>
  );
};

export default MainLayout;
