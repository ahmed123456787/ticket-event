import { createSlice } from "@reduxjs/toolkit";

export interface UserState {
  userId: string;
  userName: string;
  email: string;
  organizationName: string;
}

const initialState: UserState = {
  userId: "",
  userName: "mohamed",
  email: "def@gmail.com",
  organizationName: "dechong",
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUsername: (state, action) => {
      state.userName = action.payload;
    },
    setEmail: (state, action) => {
      state.email = action.payload;
    },
    setOrganizationName: (state, action) => {
      state.organizationName = action.payload;
    },
  },
});
export const { setUsername, setEmail, setOrganizationName } = userSlice.actions;

export default userSlice.reducer;
