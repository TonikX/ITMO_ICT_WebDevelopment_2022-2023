import { useQuery } from "@tanstack/react-query";

import backendApi from "~/utils/BackendApi";

export const useGetLibrariesPublic = () => {
    return useQuery(["libraries"], backendApi.fetchLibrariesPublic, {
        select: (data) => {
            const libraries = data.json["Library"];
            return libraries;
        },
        // keepPreviousData: true,
    });
};

export const useGetReadingRoomBook = (filters) => {
    return useQuery(["readingRoomBook", filters], () => backendApi.fetchReadingRoomBooks(filters), {
        select: (data) => {
            const readingRoomBook = data.json["ReadingRoomBook"];
            return readingRoomBook.filter(({ book }) =>
                book.title.toLowerCase().includes(filters.title.toLowerCase())
            );
        },
        keepPreviousData: true,
    });
};

export const useGetUserData = () => {
    return useQuery(["user"], backendApi.fetchLogin, {
        select: (data) => {
            return data.json["User"];
        },
        retry: 0,
    });
};
