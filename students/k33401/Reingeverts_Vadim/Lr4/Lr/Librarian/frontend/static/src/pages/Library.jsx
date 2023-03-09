import React from "react";
import { useDebouncedState } from "@mantine/hooks";

import BookGrid from "~/components/BookGrid";
import { useGetReadingRoomBook } from "~/hooks";

const Library = ({ isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);
    const { data: readingRoomBooks, status: readingRoomBooksStatus } =
        useGetReadingRoomBook(filters);

    return (
        <BookGrid
            title="Library"
            status={readingRoomBooksStatus}
            readingRoomBooks={readingRoomBooks}
            filters={filters}
            setFilters={setFilters}
            isCompactViewActive={isCompactViewActive}
        />
    );
};

export default Library;
