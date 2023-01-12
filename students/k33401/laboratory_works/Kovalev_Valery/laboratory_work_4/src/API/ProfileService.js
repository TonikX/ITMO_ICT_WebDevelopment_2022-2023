import { API } from ".";

export const likePhoto = async (token, photo_id) => {
    await API.post(
        "user/likes/create",
        {
            photo: photo_id,
        },
        {
            headers: {
                Authorization: `Token ${token}`,
            },
        }
    );
};

export const getLikes = async (token) => {
    const response = await API.get("user/likes/", {
        headers: {
            Authorization: `Token ${token}`,
        },
    });
    return response.data;
};

export const unlikePhoto = async (token, photo_id) => {
    await API.delete(`user/likes/${photo_id}`, {
        headers: {
            Authorization: `Token ${token}`,
        },
    });
};


export const getCollections = async (token) => {
    const response = await API.get('user/collections/', {
        headers: {
            Authorization: `Token ${token}`,
        }
    })
    return response.data
}

export const createCollection = async (token, title, photo_ids) => {
    await API.post('user/collections/create', {title, photos:photo_ids}, {
        headers: {
            Authorization: `Token ${token}`,
        }
    })
}

export const deleteCollection = async (token, collection_id) => {
    await API.delete(`user/collections/${collection_id}`, {
        headers: {
            Authorization: `Token ${token}`,
        }
    })
}

export const updateCollection = async (token, collection_id, title, photo_ids) => {
    await API.put(`user/collections/${collection_id}`, {title, photos:photo_ids}, {
        headers: {
            Authorization: `Token ${token}`,
        }
    })
}
