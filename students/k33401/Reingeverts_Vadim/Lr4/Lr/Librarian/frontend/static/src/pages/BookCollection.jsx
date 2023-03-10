import React from "react";
import { Loader } from "@mantine/core";
import { useDebouncedState, useDidUpdate } from "@mantine/hooks";
import { useParams } from "react-router-dom";

import BookGrid from "~/components/BookGrid";
import { useGetReadingRoomBook } from "~/hooks";

const BookCollection = ({ queryClient, isCompactViewActive }) => {
    let { id } = useParams();
    const [filters, setFilters] = useDebouncedState(
        { title: "", readingRoomId: id, userId: "" },
        200
    );
    useDidUpdate(() => setFilters((filters) => ({ ...filters, readingRoomId: id })), [id]);

    const { data: readingRoomBooks, status: readingRoomBooksStatus } =
        useGetReadingRoomBook(filters);

    return (
        <BookGrid
            queryClient={queryClient}
            title={readingRoomBooks?.[0]?.reading_room.name ?? <Loader variant="dots" />}
            status={readingRoomBooksStatus}
            readingRoomBooks={readingRoomBooks}
            filters={filters}
            setFilters={setFilters}
            isCompactViewActive={isCompactViewActive}
        />
    );
};

export default BookCollection;
