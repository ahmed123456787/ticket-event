import TopBar from "../components/dashboard/TopBar";
import Sidebar from "../components/dashboard/Sidebar";

const MainLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex flex-col h-screen">
      <TopBar />
      <div className="flex">
        <div className="w-16">
          <Sidebar />
        </div>
        <main className="flex-1 px-44 sm:px-6 md:px-24  mt-12">{children}</main>
      </div>
    </div>
  );
};

export default MainLayout;
