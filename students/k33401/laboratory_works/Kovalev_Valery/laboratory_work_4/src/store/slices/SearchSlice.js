import { createSlice } from "@reduxjs/toolkit";
import { fetchSearchPhotos } from "../actions/searchActions";

const initialState = {
    searchWord: "",
    keywords: [],
    searchTone: "",
    photos: [],
    count: 0,
    offset: 0,
    limit: 30,
    isLoading: false,
    error: "",
};

export const searchSlice = createSlice({
    name: "search",
    initialState,
    reducers: {
        setKeywords: (state, action) => {
            state.keywords = action.payload.keywords;
            state.searchWord = action.payload.searchWord;
            state.photos = [];
            state.offset = 0;
            state.count = 0;
        },
        setTone: (state, action) => {
            state.searchTone = action.payload;
            state.photos = [];
            state.offset = 0;
            state.count = 0;
        },
        clear: (state) => {
            state.photos = [];
            state.offset = 0;
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchSearchPhotos.fulfilled, (state, action) => {
                state.photos = [...state.photos, ...action.payload.results];
                state.count = action.payload.count;
                state.offset += action.payload.results.length;
                state.error = "";
                state.isLoading = false;
            })
            .addCase(fetchSearchPhotos.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(fetchSearchPhotos.rejected, (state, action) => {
                state.error = action.payload;
                state.isLoading = false;
            });
    },
});

export const searchReducer = searchSlice.reducer;
export default searchReducer;
