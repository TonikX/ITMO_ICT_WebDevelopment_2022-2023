import React from "react";
import { Group, Avatar, Box, Text, LoadingOverlay } from "@mantine/core";

const UserPane = ({
    primaryText = "",
    secondaryText = "",
    loading = false,
    imgSrc = null,
    right = null,
}) => {
    return (
        <Group spacing="xs" style={{ position: "relative" }}>
            <LoadingOverlay
                radius="md"
                visible={loading}
                overlayBlur={2}
                transitionDuration={1500}
            />

            <Avatar src={imgSrc} radius="xl" />
            <Box sx={{ flex: 1 }}>
                <Text size="sm" weight={500}>
                    {primaryText}
                </Text>
                <Text color="dimmed" size="xs">
                    {secondaryText}
                </Text>
            </Box>
            {right}
        </Group>
    );
};

export default UserPane;
