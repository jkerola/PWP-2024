import { configureStore, createSlice } from "@reduxjs/toolkit";

export const authSlice = createSlice({
  name: "auth",
  initialState: { token: null, user: null },

  reducers: {
    storeToken: (state, action) => {
      state.token = action.payload;
    },
    removeToken: (state) => {
      state.token = null;
    },
    storeUser: (state, action) => {
      state.user = action.payload;
    },
    removeUser: (state, action) => {
      state.user = null;
    },
  },
});

export const store = configureStore({
  reducer: {
    auth: authSlice.reducer,
  },
});

export const { storeToken, removeToken, storeUser, removeUser } =
  authSlice.actions;
