import React from "react";
import { useDebouncedState } from "@mantine/hooks";

import { useGetReadingRoomBook } from "~/hooks";
import BookGrid from "~/components/BookGrid";

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
