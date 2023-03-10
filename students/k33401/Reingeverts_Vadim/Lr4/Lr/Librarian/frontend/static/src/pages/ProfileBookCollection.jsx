import React from "react";
import { useDebouncedState } from "@mantine/hooks";

import BookGrid from "~/components/BookGrid";
import { useGetReadingRoomBook } from "~/hooks";

const BookCollection = ({ queryClient, isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState(
        { title: "", readingRoomId: "", userId: "50" },
        200
    );

    const { data: readingRoomBooks, status: readingRoomBooksStatus } =
        useGetReadingRoomBook(filters);

    return (
        <BookGrid
            queryClient={queryClient}
            title="profile"
            status={readingRoomBooksStatus}
            readingRoomBooks={readingRoomBooks}
            filters={filters}
            setFilters={setFilters}
            isCompactViewActive={isCompactViewActive}
        />
    );
};

export default BookCollection;
