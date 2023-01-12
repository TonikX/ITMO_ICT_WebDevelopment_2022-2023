import {createSlice} from "@reduxjs/toolkit";

const initialState = {
    open: false,
    selectedPhoto: {}
}

const collectionModalSilce = createSlice({
    name: "collectionModal",
    initialState,
    reducers: {
        openCollectionModal: (state, action) => {
            state.open =  true
            state.selectedPhoto = action.payload.photo
        },
        closeCollectionModal: (state) => {
            state.open =  false
            state.selectedPhoto = {}
        }
    }
})

export const collectionModalReducer = collectionModalSilce.reducer;
export const { openCollectionModal, closeCollectionModal } = collectionModalSilce.actions;
export default collectionModalReducer;
