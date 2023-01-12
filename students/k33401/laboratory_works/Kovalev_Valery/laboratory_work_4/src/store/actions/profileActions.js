import { createAsyncThunk } from "@reduxjs/toolkit";
import {
    getCollections,
    getLikes,
    likePhoto as apiLikePhoto,
    unlikePhoto as apiUnlikePhoto,
    createCollection as apiCreateCollection,
    deleteCollection as apiDeleteCollection,
    updateCollection as apiUpdateCollection
} from "../../API/ProfileService";

export const fetchLikes = createAsyncThunk("profile/fetchLikes", async (_, { rejectedWithValue, getState }) => {
    try {
        const { token } = getState().auth;
        return await getLikes(token);
    } catch (e) {
        return rejectedWithValue(e.massage);
    }
});

export const likePhoto = createAsyncThunk(
    "profile/likePhoto",
    async ({ photo_id }, { rejectedWithValue, getState }) => {
        try {
            const { token } = getState().auth;
            await apiLikePhoto(token, photo_id);
            return await getLikes(token);
        } catch (e) {
            return rejectedWithValue(e.massage);
        }
    }
);

export const unlikePhoto = createAsyncThunk(
    "profile/unlikePhoto",
    async ({ photo_id }, { rejectedWithValue, getState }) => {
        try {
            const { token } = getState().auth;
            const { likes } = getState().profile;
            const like = likes.find((e) => e.photo.photo_id === photo_id);
            await apiUnlikePhoto(token, like.id);
            return await getLikes(token);
        } catch (e) {
            return rejectedWithValue(e.massage);
        }
    }
);

export const fetchCollections = createAsyncThunk("profile/fetchCollections", async (_, { rejectedWithValue, getState }) => {
    try {
        const { token } = getState().auth;
        return await getCollections(token);
    } catch (e) {
        return rejectedWithValue(e.massage);
    }
});

export const createCollection = createAsyncThunk(
    "profile/createCollection",
    async ({ title, photo_ids= [] } = {}, { rejectedWithValue, getState }) => {
        try {
            const { token } = getState().auth;
            await apiCreateCollection(token, title, photo_ids);
            return await getCollections(token);
        } catch (e) {
            return rejectedWithValue(e.massage);
        }
    }
);

export const updateCollection = createAsyncThunk(
    "profile/updateCollection",
    async ({ title, photo_ids= [], collection_id } = {}, { rejectedWithValue, getState }) => {
        try {
            const { token } = getState().auth;
            await apiUpdateCollection(token, collection_id, title, photo_ids);
            return await getCollections(token);
        } catch (e) {
            return rejectedWithValue(e.massage);
        }
    }
);

export const deleteCollection = createAsyncThunk(
    "profile/deleteCollection",
    async ({ collection_id }, { rejectedWithValue, getState }) => {
        try {
            const { token } = getState().auth;
            await apiDeleteCollection(token, collection_id);
            return await getCollections(token);
        } catch (e) {
            return rejectedWithValue(e.massage);
        }
    }
);
