import React from "react";
import { useDebouncedState } from "@mantine/hooks";

import { useGetUserData, useGetUserBooks } from "~/hooks";
import BookGrid from "~/components/BookGrid";

const ProfileBookCollection = ({ isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);

    const { data: bookData, status: bookStatus } = useGetUserBooks(userData?.id);

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

export default ProfileBookCollection;
