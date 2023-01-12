import { createAsyncThunk } from "@reduxjs/toolkit";
import { getPhotosByKeywords } from "../../API/PhotosService";
import { searchSlice } from "../slices/SearchSlice";

export const fetchSearchPhotos = createAsyncThunk(
    "search/fetchSearchPhotos",
    async ({ limit = 30, offset = 0 } = {}, { rejectedWithValue, getState }) => {
        try {
            const { keywords, searchTone, offset } = getState().search;
            return await getPhotosByKeywords({ keywords, limit: 30, tone: searchTone, offset });
        } catch (e) {
            return rejectedWithValue(e.message);
        }
    }
);

export const setKeywords = (searchWord) => {
    return async (dispatch) => {
        try {
            const keywords = searchWord
                .replace(/[^\w\s\']|_/g, "")
                .replace(/\s+/g, " ")
                .split(" ");
            dispatch(searchSlice.actions.setKeywords({ keywords, searchWord }));
        } catch (e) {
            dispatch(searchSlice.actions.setKeywords({ keywords: [], searchWord: "" }));
        }
    };
};

export const setTone = (tone) => {
    return (dispatch) => {
        dispatch(searchSlice.actions.setTone(tone));
    };
};
