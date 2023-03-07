import React, { useState } from "react";
import { TextInput, Card, Image, Text, Badge, Button, Group } from "@mantine/core";
import { useDebouncedState } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";

import imgUrl from "~/images/favicon-96.png";
import notification from "~/components/Notification";
import BookCard from "~/components/BookCard";
import backendApi from "~/utils/BackendApi";

const useGetReadingRoomBook = (filters) => {
    return useQuery(["readingRoomBook", filters], () => backendApi.fetchReadingRoomBooks(filters), {
        select: (data) => {
            const readingRoomBook = data.json["ReadingRoomBook"];
            return readingRoomBook.filter(({ book }) => book.title.includes(filters.title));
        },
    });
};

const Library = () => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);
    const { data: readingRoomBooks, status } = useGetReadingRoomBook(filters);

    return (
        <>
            <TextInput
                label="Enter value to see debounce effect"
                defaultValue={filters.title}
                onChange={(event) => setFilters({ title: event.currentTarget.value })}
            />
            {status === "success" &&
                readingRoomBooks.map((readingRoomBook) => <BookCard book={readingRoomBook.book} />)}
        </>
    );
};

export default Library;
