import React, { useEffect } from "react";
import { useDebouncedState } from "@mantine/hooks";

import BookGrid from "~/components/BookGrid";
import { useGetReadingRoomBook, useGetUserData } from "~/hooks";

const ProfileBookCollection = ({ queryClient, isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState(
        { title: "", readingRoomId: "", userId: "-1" },
        200
    );
    const { data: userData, status: userStatus } = useGetUserData();
    const isUserLoaded = userStatus === "success";
    useEffect(
        () => setFilters((filters) => ({ ...filters, userId: userData?.id?.toString() ?? "-1" })),
        [isUserLoaded]
    );

    const { data: readingRoomBooks, status: readingRoomBooksStatus } =
        useGetReadingRoomBook(filters);

    return (
        <BookGrid
            queryClient={queryClient}
            title="Profile"
            status={readingRoomBooksStatus}
            readingRoomBooks={readingRoomBooks}
            filters={filters}
            setFilters={setFilters}
            isCompactViewActive={isCompactViewActive}
        />
    );
};

export default ProfileBookCollection;
