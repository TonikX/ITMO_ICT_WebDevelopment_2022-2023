import React, { useState } from "react";
import { TextInput, Container, Grid, Card, Image, Text, Badge, Button, Group } from "@mantine/core";
import { useDebouncedState } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";

import notification from "~/components/Notification";
import BookCard from "~/components/BookCard";
import backendApi from "~/utils/BackendApi";
import InputGroup from "~/components/InputGroup";

const useGetReadingRoomBook = (filters) => {
    return useQuery(["readingRoomBook", filters], () => backendApi.fetchReadingRoomBooks(filters), {
        select: (data) => {
            const readingRoomBook = data.json["ReadingRoomBook"];
            return readingRoomBook.filter(({ book }) => book.title.includes(filters.title));
        },
        notifyOnChangeProps: ["data", "error"],
        keepPreviousData: true,
    });
};

const Library = () => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);
    const { data: readingRoomBooks, status } = useGetReadingRoomBook(filters);
    console.log("readingRoomBooks", readingRoomBooks);
    return (
        <Container fluid>
            <InputGroup>
                <TextInput
                    mt="xl"
                    mb="md"
                    placeholder="Search for books..."
                    defaultValue={filters.title}
                    onChange={(event) => setFilters({ title: event.currentTarget.value })}
                />
            </InputGroup>

            <Grid mt="lg" gutter={20}>
                {status === "success" &&
                    readingRoomBooks.map((readingRoomBook) => (
                        <Grid.Col
                            key={readingRoomBook.book.id}
                            span={6}
                            xs={6}
                            sm={4}
                            md={3}
                            lg={3}
                        >
                            <BookCard book={readingRoomBook.book} stock={readingRoomBook.stock} />
                        </Grid.Col>
                    ))}
            </Grid>
        </Container>
    );
};

export default Library;
