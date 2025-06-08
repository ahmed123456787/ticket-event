import { useState } from "react";
import MainLayout from "../layouts/MainLayout";
import DesignSidebar from "../components/marketing/email/design/DesignSidebar";
import { useParams } from "react-router";

const EmailCompaign = () => {
  const { campaignId } = useParams<{ campaignId: string }>();
  const [campaignName, setCampaignName] = useState(campaignId);
  const [subject, setSubject] = useState(
    "You're invited to test (July 7, 2025)"
  );
  const [sendingTestEmail, setSendingTestEmail] = useState(false);

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
      {/* Override the MainLayout padding with negative margin and full width */}
      <div className="flex h-screen overflow-hidden md:-mr-16">
        {/* Left Sidebar */}
        <div className="w-96 border-r border-gray-200">
          <DesignSidebar
            campaignName={campaignName}
            setCampaignName={setCampaignName}
          />
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
          <div className="flex-1 p-6 overflow-y-auto bg-gray-100">
            <div className="max-w-3xl mx-auto bg-white shadow-lg rounded-md overflow-hidden">
              {/* Email Header */}
              <div className="p-4 bg-gray-50 border-b border-gray-200">
                <div className="mb-2">
                  <span className="text-sm font-medium text-gray-500">
                    Subject:
                  </span>
                  <span className="text-sm ml-1">{subject}</span>
                </div>
                <div>
                  <span className="text-sm font-medium text-gray-500">
                    From:
                  </span>
                  <span className="text-sm ml-1">AHMED</span>
                </div>
              </div>

              {/* Email Content */}
              <div className="p-8">
                <h1 className="text-3xl font-bold mb-6">Email Header</h1>
                <p className="text-gray-700 mb-4">
                  Write the text of your email here. Describe the events in this
                  email and why they can't be missed.
                </p>
                <div className="text-center my-8">
                  <button className="px-6 py-3 bg-blue-600 text-white rounded-md font-medium hover:bg-blue-700">
                    Call to Action
                  </button>
                </div>
                <p className="text-gray-700">
                  Additional information can go here to provide more details
                  about your event, organization, or offerings.
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
