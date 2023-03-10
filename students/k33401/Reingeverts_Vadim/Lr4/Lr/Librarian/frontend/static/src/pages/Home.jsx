import React from "react";
import { Container, Group, Center, Stack, Title, Text } from "@mantine/core";

const Home = ({ isCompactViewActive, title }) => {
    return (
        <Container fluid pl={0} pr={isCompactViewActive ? 0 : 32} py="xl">
            {isCompactViewActive ? (
                <>
                    <Title>{title}</Title>
                    <span />
                </>
            ) : (
                <Group grow position="apart">
                    <Title>{title}</Title>
                    <span />
                    <span />
                </Group>
            )}
            <Center mt={80}>
                <Stack>
                    <Title>Welcome to the Librarian!</Title>
                    <Text>
                        After signing up, you can reserve books in a library of your choice.
                    </Text>
                </Stack>
            </Center>
        </Container>
    );
};

export default Home;
