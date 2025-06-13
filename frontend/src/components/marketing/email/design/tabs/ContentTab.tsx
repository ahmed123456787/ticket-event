import { useState } from "react";
import FormSection from "../ui/FormSection";
import TextEditor from "../editor/TextEditor";
import { Search } from "lucide-react";

const ContentTab = () => {
  const [subject, setSubject] = useState(
    "You're invited to test (July 7, 2025)"
  );

  return (
    <div className="space-y-8">
      <h2 className="mt-4 ">Choose your events</h2>
      <div className="mb-4">
        <div className="flex items-center border border-gray-300 px-3 py-2 space-x-2">
          <Search className="w-4" />
          <input
            type="text"
            id="search"
            name="search"
            placeholder="search for events"
            className="flex-1 focus:outline-none text-xs text-gray-500"
          />
        </div>
      </div>
      <FormSection title="Email Content">
        <div className="mb-4">
          <label
            htmlFor="subject"
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            Subject
          </label>
          <input
            type="text"
            id="subject"
            name="subject"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div className="mb-4">
          <p className="text-sm font-medium text-gray-700 mb-2">Email Body</p>
          <TextEditor />
          <div className="bg-gray-100 p-4 rounded-md">
            <p className="text-sm text-gray-600">
              Email content editing will be available in the preview pane.
            </p>
          </div>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Personalization Options
          </label>
          <div className="flex flex-wrap gap-2">
            <button className="bg-gray-200 px-3 py-1 rounded-md text-sm hover:bg-gray-300">
              First Name
            </button>
            <button className="bg-gray-200 px-3 py-1 rounded-md text-sm hover:bg-gray-300">
              Last Name
            </button>
            <button className="bg-gray-200 px-3 py-1 rounded-md text-sm hover:bg-gray-300">
              Organization
            </button>
            <button className="bg-gray-200 px-3 py-1 rounded-md text-sm hover:bg-gray-300">
              Event Name
            </button>
          </div>
        </div>
      </FormSection>
    </div>
  );
};

export default ContentTab;
