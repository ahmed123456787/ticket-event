import Analytics from "../components/analytics/Analytics";
import MainLayout from "../layouts/MainLayout";

const DashboardPage = () => {
  return (
    <MainLayout>
      <div className="flex flex-col ">
        <div className="flex items-center justify-between">
          <h2 className="text-2xl">
            Welcome back,
            <span className="bg-[#F9C8BD] ml-3 rounded-md px-1 font-semibold text-3xl">
              AHMED
            </span>
          </h2>
          <img src="/welcome.svg" alt="Welcome" className="w-32 h-32" />
        </div>
        <Analytics />
      </div>
    </MainLayout>
  );
};

export default DashboardPage;
