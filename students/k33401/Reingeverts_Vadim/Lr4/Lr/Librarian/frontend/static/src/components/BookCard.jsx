import React from "react";
import { Card, Text, Badge, Button, Group, useMantineTheme } from "@mantine/core";
import { useMediaQuery } from "@mantine/hooks";
import notification from "~/components/Notification";
import { useMutation } from "@tanstack/react-query";

import { toISOStringLocal } from "~/utils";
import backendApi from "~/utils/BackendApi";
import RandomImage from "~/components/RandomImage";
import cover1 from "~/images/book-cover-1.webp";
import cover2 from "~/images/book-cover-2.webp";
import cover3 from "~/images/book-cover-3.webp";
import cover4 from "~/images/book-cover-4.webp";
import cover5 from "~/images/book-cover-5.webp";

const coverSrcSet = [cover1, cover2, cover3, cover4, cover5];

const BookCard = ({
    isReserved,
    reservationId,
    queryClient,
    book,
    stock,
    readingRoomBookId,
    userData,
}) => {
    const theme = useMantineTheme();

    const largerThanSm = `(max-width: ${theme.breakpoints.sm})`;
    const isSmallerThanSm = useMediaQuery(largerThanSm);

    const postReadingRoomBookUsers = useMutation(backendApi.postReadingRoomBookUsers, {
        onSuccess: ({ json, ok }) => {
            if (ok) {
                queryClient.invalidateQueries("readingRoomBook");
                notification.showSuccess("Book was reserved");
            } else {
                notification.showAlert(json["error"][0]);
            }
        },
        onError: notification.showError,
        retry: 0,
    });
    const patchReadingRoomBookUserDetails = useMutation(
        backendApi.patchReadingRoomBookUserDetails,
        {
            onSuccess: ({ json, ok }) => {
                if (ok) {
                    queryClient.invalidateQueries("readingRoomBookUser");
                    notification.showSuccess("Book was returned");
                } else {
                    notification.showAlert(json["error"][0]);
                }
            },
            onError: notification.showError,
            retry: 0,
        }
    );

    const handleReserveBook = () => {
        postReadingRoomBookUsers.mutate({
            body: {
                ReadingRoomBookUser: {
                    reading_room_book: readingRoomBookId,
                    user: userData.id,
                },
            },
        });
    };

    const handleReturnBook = () => {
        patchReadingRoomBookUserDetails.mutate({
            readingRoomBookUserId: reservationId,
            body: {
                ReadingRoomBookUser: {
                    returned_date: toISOStringLocal(),
                },
            },
        });
    };
    return (
        <Card shadow="sm" padding={isSmallerThanSm ? "xs" : "md"} radius="md" withBorder>
            <Card.Section
                component="a"
                href="https://mantine.dev/"
                style={{ position: "relative" }}
            >
                <Badge
                    color="light-blue-filled"
                    variant="filled"
                    m={2}
                    style={{ position: "absolute", right: 0, zIndex: 2 }}
                >
                    {stock < 99 ? stock : "99+"}
                </Badge>
                <RandomImage srcSet={coverSrcSet} seed={book.title} alt="book cover" />
            </Card.Section>

            <Group position="apart" my="xs">
                <Text fz={isSmallerThanSm ? "md" : "lg"} weight={500} inline>
                    {book.title}
                </Text>
            </Group>

            <Text size="xs" color="dimmed">
                By {book.authors || "Unkown"}
            </Text>

            <Group position="apart" spacing="xs">
                {isReserved ? (
                    <Button
                        variant="light"
                        color="teal"
                        fullWidth
                        mt="sm"
                        radius="md"
                        onClick={handleReturnBook}
                    >
                        Return
                    </Button>
                ) : (
                    <Button
                        variant="light"
                        color="blue"
                        fullWidth
                        mt="sm"
                        radius="md"
                        onClick={handleReserveBook}
                    >
                        Get
                    </Button>
                )}
            </Group>
        </Card>
    );
};

export default BookCard;
