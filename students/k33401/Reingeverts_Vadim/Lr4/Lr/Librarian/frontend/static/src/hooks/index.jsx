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
            const readingRoomBooks = data.json["ReadingRoomBook"];
            return readingRoomBooks
                .filter((readingRoomBook) => {
                    const readingRoomId = parseInt(filters.readingRoomId);
                    return (
                        readingRoomBook.reading_room.id === readingRoomId || isNaN(readingRoomId)
                    );
                })
                .filter(({ book }) =>
                    book.title.toLowerCase().includes(filters.title.toLowerCase())
                );
        },
        keepPreviousData: true,
    });
};

export const useGetUserData = (logout = null) => {
    return useQuery(["user"], backendApi.fetchLogin, {
        select: (data) => {
            return data.json["User"];
        },
        onError: () => {
            if (logout) logout();
        },
        retry: 0,
    });
};
