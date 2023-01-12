import {createSlice} from "@reduxjs/toolkit";
import {
    deleteCollection,
    fetchCollections,
    fetchLikes,
    likePhoto,
    unlikePhoto,
    updateCollection
} from "../actions/profileActions";

const initialState = {
    likes: [],
    likedPhotos: [],
    collections: [],
    isLoading: false,
    error: "",
};

export const profileSlice = createSlice({
    name: "profile",
    initialState,
    reducers: {
        clearProfile: (state) => {
            state.likes = [];
            state.likedPhotos = [];
            state.collections = [];
            state.isLoading = false;
            state.error = "";
        },
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchLikes.fulfilled, (state, action) => {
                state.likes = action.payload;
                state.likedPhotos = action.payload.map((e) => e.photo);
                state.isLoading = false;
            })
            .addCase(fetchLikes.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(fetchLikes.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            .addCase(likePhoto.fulfilled, (state, action) => {
                state.likes = action.payload;
                state.likedPhotos = action.payload.map((e) => e.photo);
                state.isLoading = false;
            })
            .addCase(likePhoto.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(likePhoto.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            .addCase(unlikePhoto.fulfilled, (state, action) => {
                state.likes = action.payload;
                state.likedPhotos = action.payload.map((e) => e.photo);
                state.isLoading = false;
            })
            .addCase(unlikePhoto.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(unlikePhoto.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload;
            })
            .addCase(fetchCollections.fulfilled, (state, action) => {
                state.collections = action.payload;
                state.isLoading = false;
            })
            .addCase(fetchCollections.pending, (state) => {
                state.isLoading = true;
            }).addCase(fetchCollections.rejected, (state, action) => {
            state.isLoading = false;
            state.error = action.payload;
        }).addCase(updateCollection.fulfilled, (state, action) => {
            state.collections = action.payload;
            state.isLoading = false;
        })
            .addCase(updateCollection.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(updateCollection.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload;
            }).addCase(deleteCollection.fulfilled, (state, action) => {
            state.collections = action.payload;
            state.isLoading = false;
        })
            .addCase(deleteCollection.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(deleteCollection.rejected, (state, action) => {
                state.isLoading = false;
                state.error = action.payload;
            });
    },
});

export const profileReducer = profileSlice.reducer;
export const {clearProfile} = profileSlice.actions
export default profileReducer;
