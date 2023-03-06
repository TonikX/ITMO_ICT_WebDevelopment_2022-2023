import React from "react";
import {
    UnstyledButton,
    Group,
    Avatar,
    Box,
    useMantineTheme,
    rem,
    Popover,
    Text,
    Button,
    MediaQuery,
} from "@mantine/core";
import { IconChevronRight, IconChevronLeft } from "@tabler/icons-react";

const LogoutButton = () => <Button color="red">Log Out</Button>;

const getUserContainerSx = (theme) => {
    return {
        display: "block",
        width: "100%",
        padding: theme.spacing.xs,
        borderRadius: theme.radius.sm,
        color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.black,

        "&:hover": {
            backgroundColor:
                theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.colors.gray[0],
        },
    };
};

const UserContent = ({ right }) => {
    const theme = useMantineTheme();

    return (
        <Group spacing="xs">
            <Avatar
                src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=255&q=80"
                radius="xl"
            />
            <Box sx={{ flex: 1 }}>
                <Text size="sm" weight={500}>
                    Amy Horsefighter
                </Text>
                <Text color="dimmed" size="xs">
                    ahorsefighter
                </Text>
            </Box>
            {right}
        </Group>
    );
};

const User = () => {
    const theme = useMantineTheme();

    return (
        <Box
            sx={{
                paddingTop: theme.spacing.sm,
                borderTop: `${rem(1)} solid ${
                    theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[2]
                }`,
            }}
        >
            <MediaQuery smallerThan="sm" styles={{ display: "none" }}>
                <Popover position="right" shadow="md" radius="sm" offset={8}>
                    <Popover.Target>
                        <UnstyledButton sx={getUserContainerSx(theme)}>
                            <UserContent right={<IconChevronRight size={rem(18)} />} />
                        </UnstyledButton>
                    </Popover.Target>
                    <Popover.Dropdown>
                        <LogoutButton />
                    </Popover.Dropdown>
                </Popover>
            </MediaQuery>
            <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                <Box sx={getUserContainerSx(theme)}>
                    <UserContent right={<LogoutButton />} />
                </Box>
            </MediaQuery>
        </Box>
    );
};

export default User;
