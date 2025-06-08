import React, { ReactNode } from "react";

interface FormSectionProps {
  title: string;
  children: ReactNode;
}

const FormSection: React.FC<FormSectionProps> = ({ title, children }) => {
  return (
    <div className=" border-gray-200 pb-6 mb-6 last:border-b-0 last:mb-0 last:pb-0">
      <h3 className="text-lg font-semibold  mb-4">{title}</h3>
      <div className="space-y-2 mx-3">{children}</div>
    </div>
  );
};

export default FormSection;
