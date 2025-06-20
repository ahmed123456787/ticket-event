import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import DesignSidebar from "../components/marketing/email/design/DesignSidebar";
import { useLocation } from "react-router-dom";
import { emailContext } from "../contexts/emailContext";
import { useContext } from "react";

const EmailCompaign = () => {
  const { subject } = useContext(emailContext);
  const location = useLocation();
  const [sendingTestEmail, setSendingTestEmail] = useState(false);
  const [campaignName, setCampaignName] = useState(
    location.state?.compaignName || "Default Campaign Name"
  );
  const handleSendTest = () => {
    setSendingTestEmail(true);
    // Mock API call
    setTimeout(() => {
      setSendingTestEmail(false);
      alert("Test email sent successfully!");
    }, 1500);
  };

  return (
    <MainLayout>
      <div className="flex h-screen ">
        {/* Left Sidebar */}
        <div className="w-1/3  h-full px-3">
          <DesignSidebar />
        </div>

        {/* Email Preview Content */}
        <div className="flex-1 flex flex-col">
          {/* Top navigation bar */}
          <div className="flex items-center justify-between px-6 py-3 border-b border-gray-200">
            <div className="flex items-center space-x-4">
              <h2 className="font-bold text-xl">{campaignName}</h2>
            </div>
            <div className="flex items-center space-x-2">
              <button
                className="px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-50 font-medium text-gray-600"
                onClick={handleSendTest}
                disabled={sendingTestEmail}
              >
                {sendingTestEmail ? "Sending..." : "Send test email"}
              </button>
            </div>
          </div>

          {/* Email Preview */}
          <div className="flex-1 p-6 min-h-full bg-gray-100">
            <div className="max-w-3xl mx-auto  shadow-lg bg-white rounded-md overflow-hidden">
              {/* Email Header */}
              <div className="p-4">
                <div className="mb-2 text-xs  ">
                  <span className="text-gray-500">Subject:</span>
                  <span className="text-black ml-1">{subject}</span>
                </div>
                <div>
                  <span className="text-xs text-gray-500">From:</span>
                  <span className="text-sm ml-1">AHMED</span>
                </div>
              </div>

              {/* Email Content */}
              <div className="p-8">
                <h1 className="text-3xl text-center mb-6">Email Header</h1>
                <p className="text-sm mb-24 text-center opacity-70">
                  Write the text of your email here.
                  <br />
                  Describe the events in this email and why they can't be
                  missed.
                </p>
              </div>

              {/* Email Footer */}
              <div className="bg-gray-50 p-6 text-center text-sm text-gray-500 border-t border-gray-200">
                <p className="mb-2">AHMED Zater</p>
                <p>def dsfsdfsdkf, sgit, 23444 DZ</p>
                <div className="mt-2">
                  <a href="#" className="text-blue-600 hover:underline">
                    Unsubscribe
                  </a>
                  <span className="mx-2">|</span>
                  <a href="#" className="text-blue-600 hover:underline">
                    Privacy Policy
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </MainLayout>
  );
};

export default EmailCompaign;
