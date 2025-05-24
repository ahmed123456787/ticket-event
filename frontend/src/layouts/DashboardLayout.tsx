import TopBar from "../components/dashboard/TopBar";

const DashboardLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex flex-col h-screen ">
      <TopBar />
      {children}
    </div>
  );
};

export default DashboardLayout;
