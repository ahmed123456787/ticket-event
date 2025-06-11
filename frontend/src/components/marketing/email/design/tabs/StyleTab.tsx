import { useState } from "react";
import FormSection from "../ui/FormSection";
import ColorPicker from "../ui/ColorPicker";

const StyleTab = () => {
  const [styles, setStyles] = useState({
    headerColor: "#363636",
    backgroundColor: "#FFFFFF",
    textColor: "#333333",
    buttonColor: "#FF5722",
    buttonTextColor: "#FFFFFF",
    fontFamily: "Arial",
  });

  const handleColorChange = (name: string, value: string) => {
    setStyles((prev) => ({ ...prev, [name]: value }));
  };

  const fontOptions = [
    "Arial",
    "Helvetica",
    "Georgia",
    "Times New Roman",
    "Courier New",
  ];

  return (
    <div className="space-y-8">
      <FormSection title="Email Style">
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Header Color
            </label>
            <ColorPicker
              color={styles.headerColor}
              onChange={(color) => handleColorChange("headerColor", color)}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Background Color
            </label>
            <ColorPicker
              color={styles.backgroundColor}
              onChange={(color) => handleColorChange("backgroundColor", color)}
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Text Color
            </label>
            <ColorPicker
              color={styles.textColor}
              onChange={(color) => handleColorChange("textColor", color)}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Button Color
            </label>
            <ColorPicker
              color={styles.buttonColor}
              onChange={(color) => handleColorChange("buttonColor", color)}
            />
          </div>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Font Family
          </label>
          <select
            value={styles.fontFamily}
            onChange={(e) =>
              setStyles((prev) => ({ ...prev, fontFamily: e.target.value }))
            }
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {fontOptions.map((font) => (
              <option key={font} value={font}>
                {font}
              </option>
            ))}
          </select>
        </div>
      </FormSection>

      <FormSection title="Layout Options">
        <div className="space-y-4">
          <div className="flex items-center">
            <input
              type="checkbox"
              id="showHeader"
              className="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"
              defaultChecked
            />
            <label htmlFor="showHeader" className="ml-2 text-sm text-gray-700">
              Show header image
            </label>
          </div>

          <div className="flex items-center">
            <input
              type="checkbox"
              id="showFooter"
              className="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"
              defaultChecked
            />
            <label htmlFor="showFooter" className="ml-2 text-sm text-gray-700">
              Show footer
            </label>
          </div>

          <div className="flex items-center">
            <input
              type="checkbox"
              id="showSocialIcons"
              className="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"
              defaultChecked
            />
            <label
              htmlFor="showSocialIcons"
              className="ml-2 text-sm text-gray-700"
            >
              Show social icons
            </label>
          </div>
        </div>
      </FormSection>
    </div>
  );
};

export default StyleTab;
