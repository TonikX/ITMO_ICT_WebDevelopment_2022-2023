import { API } from ".";

export const getCategories = async ({ limit = 5, offset = 0 } = {}) => {
    const response = await API.get("keywords/", {
        params: {
            limit,
            offset,
        },
    });
    return response.data;
};

export const getPhotosByKeywords = async ({ keywords, limit = 3, offset = 0, tone = "" } = {}) => {
    const response = await API.get("search/", {
        params: {
            limit,
            offset,
            "keywords[]": keywords,
            random: 5,
            tone,
        },
    });
    return response.data;
};
