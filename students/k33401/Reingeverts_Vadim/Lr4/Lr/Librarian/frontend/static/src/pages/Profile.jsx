import React from "react";
import { useDebouncedState } from "@mantine/hooks";
import { useQuery } from "@tanstack/react-query";

import BookGrid from "~/components/BookGrid";
import backendApi from "~/utils/BackendApi";

const useGetReadingRoomBook = (filters) => {
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

const Profile = ({ isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);
    const { data: readingRoomBooks, status } = useGetReadingRoomBook(filters);

    return (
        <BookGrid
            title="Profile"
            status={status}
            readingRoomBooks={readingRoomBooks}
            filters={filters}
            setFilters={setFilters}
            isCompactViewActive={isCompactViewActive}
        />
    );
};

export default Profile;
