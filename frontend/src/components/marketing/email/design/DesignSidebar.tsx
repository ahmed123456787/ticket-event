import { useSelector } from "react-redux";
import { RootState } from "../../../../redux/store";

const DesignSidebar = () => {
  const { email, organizationName, userName } = useSelector(
    (state: RootState) => state.user
  );

  return (
    <div>
      DesignSidebar: {email}, {organizationName}, {userName}
    </div>
  );
};

export default DesignSidebar;
