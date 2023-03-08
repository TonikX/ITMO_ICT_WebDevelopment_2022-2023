import React from "react";
import { Title, TextInput, Container, Grid, Group } from "@mantine/core";
import { useDebouncedState } from "@mantine/hooks";
import { useQuery } from "@tanstack/react-query";

import BookCard from "~/components/BookCard";
import backendApi from "~/utils/BackendApi";

const useGetReadingRoomBook = (filters) => {
    return useQuery(["readingRoomBook", filters], () => backendApi.fetchReadingRoomBooks(filters), {
        select: (data) => {
            const readingRoomBook = data.json["ReadingRoomBook"];
            return readingRoomBook.filter(({ book }) =>
                book.title.toLowerCase().includes(filters.title.toLowerCase())
            );
        },
        notifyOnChangeProps: ["data", "error"],
        keepPreviousData: true,
    });
};

const Library = ({ isCompactViewActive }) => {
    const [filters, setFilters] = useDebouncedState({ title: "" }, 200);
    const { data: readingRoomBooks, status } = useGetReadingRoomBook(filters);

    return (
        <Container fluid pl={0} pr={isCompactViewActive ? 0 : 32}>
            {isCompactViewActive ? (
                <>
                    <Title>Library</Title>
                    <TextInput
                        mt="xl"
                        mb="md"
                        placeholder="Search for books..."
                        defaultValue={filters.title}
                        onChange={(event) => setFilters({ title: event.currentTarget.value })}
                    />
                </>
            ) : (
                <Group grow position="apart">
                    <Title>Library</Title>
                    <span />
                    <TextInput
                        mt="xl"
                        mb="md"
                        placeholder="Search for books..."
                        defaultValue={filters.title}
                        onChange={(event) => setFilters({ title: event.currentTarget.value })}
                    />
                </Group>
            )}

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
