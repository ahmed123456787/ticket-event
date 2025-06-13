import { createContext, useState, ReactNode } from "react";

interface EmailContextProps {
  subject: string;
  setSubject: (subject: string) => void;
  campaignName: string;
  setCampaignName: (name: string) => void;
  sendingTestEmail: boolean;
  setSendingTestEmail: (sending: boolean) => void;
  handleSendTest: () => void;
  content: string;
  setContent: (content: string) => void;
  editor: any;
}

const emailContext = createContext<EmailContextProps>({
  subject: "",
  setSubject: () => {},
  campaignName: "",
  setCampaignName: () => {},
  sendingTestEmail: false,
  setSendingTestEmail: () => {},
  handleSendTest: () => {},
  content: "",
  setContent: () => {},
  editor: null,
});

const EmailProvider = ({ children }: { children: ReactNode }) => {
  const [subject, setSubject] = useState(
    "You're invited to test (June 7, 2025)"
  );
  const [campaignName, setCampaignName] = useState("");
  const [sendingTestEmail, setSendingTestEmail] = useState(false);
  const [content, setContent] = useState("");
  const [editor, setEditor] = useState(null);

  const handleSendTest = () => {
    // Logic for sending a test email
  };

  return (
    <emailContext.Provider
      value={{
        subject,
        setSubject,
        campaignName,
        setCampaignName,
        sendingTestEmail,
        setSendingTestEmail,
        handleSendTest,
        content,
        setContent,
        editor,
      }}
    >
      {children}
    </emailContext.Provider>
  );
};

export { emailContext, EmailProvider };
