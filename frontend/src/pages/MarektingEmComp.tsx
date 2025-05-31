import EmailCamNavbar from "../components/marketing/email/EmailCamNavbar";
import AllowedEmail from "../components/marketing/email/AllowedEmail";
import MarketingLayout from "../layouts/MarketingLayout";

const MarektingEmComp = () => {
  return (
    <MarketingLayout>
      <p className="mt-4 font-normal">
        Connect with your audience through custom newsletters and event
        announcements
      </p>
      <div className="mt-14">
        <AllowedEmail />
      </div>
      <div className="mt-10">
        <EmailCamNavbar />
      </div>
    </MarketingLayout>
  );
};

export default MarektingEmComp;
