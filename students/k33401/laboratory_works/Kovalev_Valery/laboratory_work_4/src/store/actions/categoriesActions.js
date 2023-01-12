import { createAsyncThunk } from "@reduxjs/toolkit";
import { getCategories, getPhotosByKeywords } from "../../API/PhotosService";

export const fetchCategories = createAsyncThunk(
    "categories/fetchCategories",
    async (_, { rejectWithValue, getState }) => {
        try {
            const { offset, limit } = getState().categories;
            const response = await getCategories({ limit, offset });
            const categories = {};
            for (const { keyword, total } of response.results) {
                categories[keyword] = { photos: [], total };
                const response = await getPhotosByKeywords({ keywords: [keyword] });
                categories[keyword].photos = response.results;
            }
            return { categories, count: response.count };
        } catch (e) {
            return rejectWithValue(e.message);
        }
    }
);
