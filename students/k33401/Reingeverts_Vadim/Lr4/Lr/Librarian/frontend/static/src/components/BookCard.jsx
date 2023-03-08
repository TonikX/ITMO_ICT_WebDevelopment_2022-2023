import React from "react";
import { Card, Text, Badge, Button, Group, useMantineTheme } from "@mantine/core";
import { useMediaQuery } from "@mantine/hooks";

import RandomImage from "~/components/RandomImage";
import cover1 from "~/images/book-cover-1.webp";
import cover2 from "~/images/book-cover-2.webp";
import cover3 from "~/images/book-cover-3.webp";
import cover4 from "~/images/book-cover-4.webp";
import cover5 from "~/images/book-cover-5.webp";

const coverSrcSet = [cover1, cover2, cover3, cover4, cover5];

const BookCard = ({ book, stock }) => {
    const theme = useMantineTheme();

    const largerThanSm = `(max-width: ${theme.breakpoints.sm})`;
    const isSmallerThanSm = useMediaQuery(largerThanSm);

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
                {book.authors}
            </Text>

            <Group position="apart" spacing="xs">
                <Button variant="light" color="blue" fullWidth mt="sm" radius="md">
                    Get
                </Button>
            </Group>
        </Card>
    );
};

export default BookCard;
