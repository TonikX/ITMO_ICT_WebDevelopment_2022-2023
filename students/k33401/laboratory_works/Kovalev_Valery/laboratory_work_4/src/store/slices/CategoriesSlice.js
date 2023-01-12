import { createSlice } from "@reduxjs/toolkit";
import { fetchCategories } from "../actions/categoriesActions";

const initialState = {
    categories: {}, // {categort: {photos:[], total:Int}}
    isLoading: false,
    count: 0,
    offset: 0,
    page: 1,
    limit: 12,
    error: "",
};

export const categoriesSlice = createSlice({
    name: "categories",
    initialState,
    reducers: {
        changePage: (state, action) => {
            state.offset = (action.payload - 1) * state.limit;
            state.page = action.payload;
        },
        changeLimit: (state, action) => {
            state.limit = action.payload.limit;
            state.page = action.payload.page;
            state.offset = (action.payload.page - 1) * action.payload.limit;
        },
    },
    extraReducers: {
        [fetchCategories.pending]: (state) => {
            state.isLoading = true;
        },
        [fetchCategories.fulfilled]: (state, action) => {
            state.categories = action.payload.categories;
            state.isLoading = false;
            state.count = action.payload.count;
            state.error = "";
        },
        [fetchCategories.rejected]: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
    },
});

export const authReducer = categoriesSlice.reducer;
export const { changePage, changeLimit } = categoriesSlice.actions;
export default authReducer;
