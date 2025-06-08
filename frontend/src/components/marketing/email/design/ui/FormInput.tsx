import React, { useState } from "react";

interface FormInputProps {
  label: string;
  name: string;
  value?: string;
  placeholder?: string;
  required?: boolean;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const FormInput: React.FC<FormInputProps> = ({
  label,
  name,
  value,
  placeholder,
  required = false,
  onChange,
}) => {
  const [isFocused, setIsFocused] = useState(false);

  const handleFocus = () => setIsFocused(true);
  const handleBlur = () => setIsFocused(false);

  const isActive = isFocused || value;

  return (
    <div className="mb-4 relative">
      <div className="relative">
        <input
          type="text"
          id={name}
          name={name}
          value={value}
          placeholder={isActive ? placeholder : ""}
          onChange={onChange}
          onFocus={handleFocus}
          onBlur={handleBlur}
          className="w-full px-3 pt-5 pb-2 border-[0.1px] border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-700 peer"
        />
        <label
          htmlFor={name}
          className="absolute left-3 transition-all duration-200 pointer-events-none 
            text-xs top-1 text-gray-400"
        >
          {label} {required && <span className="text-red-500">*</span>}
        </label>
      </div>
    </div>
  );
};

export default FormInput;
