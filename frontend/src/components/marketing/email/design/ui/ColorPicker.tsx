import React, { useState } from "react";

interface ColorPickerProps {
  color: string;
  onChange: (color: string) => void;
}

const ColorPicker: React.FC<ColorPickerProps> = ({ color, onChange }) => {
  const [showPicker, setShowPicker] = useState(false);

  const handleColorChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onChange(e.target.value);
  };

  return (
    <div className="relative">
      <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
        <div 
          className="w-10 h-8" 
          style={{ backgroundColor: color }}
        ></div>
        <input 
          type="text"
          value={color}
          onChange={(e) => onChange(e.target.value)}
          className="px-3 py-2 flex-1 border-l border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="button"
          onClick={() => setShowPicker(!showPicker)}
          className="px-3 py-2 bg-gray-100 border-l border-gray-300 hover:bg-gray-200"
        >
          Select
        </button>
      </div>
      
      {showPicker && (
        <div className="absolute mt-1 z-10 bg-white border border-gray-300 p-2 rounded-md shadow-lg">
          <input
            type="color"
            value={color}
            onChange={handleColorChange}
            className="w-full h-32 cursor-pointer"
          />
          <div className="flex justify-end mt-2">
            <button
              type="button"
              onClick={() => setShowPicker(false)}
              className="px-3 py-1 text-sm bg-gray-200 rounded-md hover:bg-gray-300"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ColorPicker;