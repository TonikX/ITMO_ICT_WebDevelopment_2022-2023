import {createAsyncThunk} from "@reduxjs/toolkit";
import {getToken, getUser, logOut as apiLogout, register as apiRegister} from "../../API/AuthService";

export const fetchUser = createAsyncThunk("auth/fetchUser", async (_, {rejectWithValue, getState}) => {
    try {
        const user = await getUser({token: getState().auth.token});
        return user;
    } catch (e) {
        return rejectWithValue(e.message);
    }
});

export const login = createAsyncThunk("auth/login", async ({username, password}, {rejectWithValue}) => {
    try {
        const {auth_token} = await getToken({username, password});
        const user = await getUser({token: auth_token});
        localStorage.setItem("token", auth_token);
        return {token: auth_token, user};
    } catch (e) {
        localStorage.removeItem("token");
        return rejectWithValue(e.message);
    }
});

export const logOut = createAsyncThunk("auth/logOut", async (_, {rejectWithValue, getState}) => {
    try {
        await apiLogout({token: getState().auth.token});
    } catch (e) {
        rejectWithValue(e.message)
    }
})

export const register = createAsyncThunk("auth/register", async ({username, password}, {rejectWithValue}) => {
    try {
        await apiRegister({username, password});
        const {auth_token} = await getToken({username, password});
        const user = await getUser({token: auth_token});
        localStorage.setItem("token", auth_token);
        return {token: auth_token, user};
    } catch (e) {
        localStorage.removeItem("token");
        return rejectWithValue(e.message);
    }
});
