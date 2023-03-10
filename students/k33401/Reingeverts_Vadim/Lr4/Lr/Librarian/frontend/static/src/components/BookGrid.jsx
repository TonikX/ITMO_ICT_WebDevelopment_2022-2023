import React from "react";
import { Title, TextInput, Container, Grid, Group, Loader } from "@mantine/core";
import { IconSearch } from "@tabler/icons-react";

import { useGetUserData } from "~/hooks";
import BookCard from "~/components/BookCard";

const BookGrid = ({
    queryClient,
    title,
    status,
    readingRoomBooks,
    filters,
    setFilters,
    isCompactViewActive,
}) => {
    const conditionalLoader = status === "loading" ? <Loader size="xs" /> : null;
    const { data: userData, status: userStatus } = useGetUserData();

    return (
        <Container fluid pl={0} pr={isCompactViewActive ? 0 : 32}>
            {isCompactViewActive ? (
                <>
                    <Title>{title}</Title>
                    <TextInput
                        mt="xl"
                        mb="md"
                        placeholder="Search for books..."
                        defaultValue={filters.title}
                        icon={<IconSearch size="0.8rem" />}
                        rightSection={conditionalLoader}
                        onChange={(event) => setFilters({ title: event.currentTarget.value })}
                    />
                </>
            ) : (
                <Group grow position="apart">
                    <Title>{title}</Title>
                    <span />
                    <TextInput
                        mt="xl"
                        mb="md"
                        placeholder="Search for books..."
                        defaultValue={filters.title}
                        icon={<IconSearch size="0.8rem" />}
                        rightSection={conditionalLoader}
                        onChange={(event) => setFilters({ title: event.currentTarget.value })}
                    />
                </Group>
            )}

            <Grid my="lg" gutter={20}>
                {status === "success" &&
                    userStatus === "success" &&
                    readingRoomBooks.map((readingRoomBook) => {
                        const userReservedBook = readingRoomBook.readingroombookuser_set.find(
                            (readingRoomBookUser) =>
                                readingRoomBookUser.user.id === userData.id &&
                                readingRoomBookUser.returned_date === null
                        );
                        const userReturnedBook = readingRoomBook.readingroombookuser_set.find(
                            (readingRoomBookUser) => readingRoomBookUser.user.id === userData.id
                        );

                        const userBook = userReservedBook ?? userReturnedBook;
                        const isReserved = !(userBook?.returned_date !== null);

                        return (
                            <Grid.Col
                                key={readingRoomBook.book.id}
                                span={6}
                                xs={6}
                                sm={4}
                                md={3}
                                lg={3}
                            >
                                <BookCard
                                    isReserved={isReserved}
                                    reservationId={userBook?.id}
                                    queryClient={queryClient}
                                    book={readingRoomBook.book}
                                    readingRoomBookId={readingRoomBook.id}
                                    stock={readingRoomBook.stock}
                                    userData={userData}
                                />
                            </Grid.Col>
                        );
                    })}
            </Grid>
        </Container>
    );
};

export default BookGrid;
