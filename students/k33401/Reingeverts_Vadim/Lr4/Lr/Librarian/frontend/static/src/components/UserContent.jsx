import React from "react";
import { Group, Avatar, Box, Text } from "@mantine/core";

const UserContent = ({ data, right }) => {
    const user = data.json;
    let name = [user?.first_name, user?.last_name].join(" ");
    name = name === " " ? "Anonymous User" : name;

    return (
        <Group spacing="xs">
            <Avatar
                src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=255&q=80"
                radius="xl"
            />
            <Box sx={{ flex: 1 }}>
                <Text size="sm" weight={500}>
                    {name}
                </Text>
                <Text color="dimmed" size="xs">
                    {user.username}
                </Text>
            </Box>
            {right}
        </Group>
    );
};

export default UserContent;
