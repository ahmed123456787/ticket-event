import { useSelector } from "react-redux";
import { RootState } from "../../../../../redux/store";
import FormInput from "../ui/FormInput";
import FormSection from "../ui/FormSection";
import { useState } from "react";

interface CampaignInfoProps {
  campaignName: string;
  setCampaignName: (name: string) => void;
}

const BasicInfoTab = ({ campaignName, setCampaignName }: CampaignInfoProps) => {
  const { email, userName, organizationName } = useSelector(
    (state: RootState) => state.user
  );

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = e.target;
    setCampaignName(value);
  };

  return (
    <div className="space-y-8">
      {/* Campaign information section */}
      <FormSection title="Campaign information">
        <FormInput
          label="Campaign name"
          name="campaignName"
          value={campaignName || ""}
          onChange={(e) => setCampaignName(e.target.value)}
          required
        />
        <FormInput
          label="From"
          name="from"
          value={campaignName}
          onChange={(e) => setCampaignName(e.target.value)}
          required
        />
        <FormInput
          label="Reply-to email address"
          name="replyToEmail"
          value={email}
          onChange={handleInputChange}
          required
        />
      </FormSection>

      {/* Footer section */}
      <FormSection title="Footer">
        <p className="text-sm text-gray-600 mb-4">
          To help your email go through to inboxes instead of spam, the best
          practice is to have these filled out.
        </p>

        <FormInput
          label="Organizer name"
          name="organizerName"
          placeholder={organizationName}
          onChange={() => {}}
          required
        />

        <FormInput
          label="Address 1"
          name="address1"
          placeholder="def"
          onChange={() => {}}
          required
        />

        <FormInput
          label="Address 2"
          name="address2"
          placeholder="dsfsdfsdfdf"
          onChange={() => {}}
        />

        <FormInput
          label="City"
          name="city"
          placeholder="sgit"
          onChange={() => {}}
          required
        />

        <div className="grid grid-cols-2 gap-4">
          <FormInput
            label="State/Province"
            name="state"
            placeholder=""
            onChange={() => {}}
          />

          <FormInput
            label="Postal Code"
            name="postalCode"
            placeholder="23444"
            onChange={() => {}}
            required
          />
        </div>
      </FormSection>
    </div>
  );
};

export default BasicInfoTab;
