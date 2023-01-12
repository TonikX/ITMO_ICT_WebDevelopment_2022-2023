import {createSlice} from "@reduxjs/toolkit";
import {login, fetchUser, logOut, register} from "../actions/authActions";

const initialState = {
    user: {},
    token: localStorage.getItem("token") ?? "",
    isLoading: false,
    error: "",
};

export const authSlice = createSlice({
    name: "auth",
    initialState,
    extraReducers: {
        [login.pending]: (state) => {
            state.isLoading = true;
        },
        [login.fulfilled]: (state, action) => {
            state.token = action.payload.token;
            state.user = action.payload.user;
            state.error = "";
        },
        [login.rejected]: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
        [fetchUser.pending]: (state) => {
            state.isLoading = true;
        },
        [fetchUser.fulfilled]: (state, action) => {
            state.user = action.payload;
            state.isLoading = false;
            state.error = "";
        },
        [fetchUser.rejected]: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
        [logOut.pending]: (state) => {
            state.isLoading = true;
        },
        [logOut.fulfilled]: (state) => {
            state.user = {};
            state.isLoading = false;
            state.error = "";
        },
        [logOut.rejected]: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
        [register.pending]: (state) => {
            state.isLoading = true;
        },
        [register.fulfilled]: (state, action) => {
            state.token = action.payload.token;
            state.user = action.payload.user;
            state.isLoading = false;
            state.error = "";
        },
        [register.rejected]: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
    },
});

export const authReducer = authSlice.reducer;
export default authReducer;
