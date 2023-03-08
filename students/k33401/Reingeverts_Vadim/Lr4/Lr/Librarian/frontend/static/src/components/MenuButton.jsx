import React from "react";
import { useNavigate, useLocation } from "react-router-dom";

import { ThemeIcon, UnstyledButton, Group, Text } from "@mantine/core";

const MenuButton = ({ icon, color, label, to }) => {
    const navigate = useNavigate();
    const location = useLocation();

    const isActive = location.pathname === to;

    return (
        <UnstyledButton
            sx={(theme) => ({
                display: "block",
                width: "100%",
                padding: theme.spacing.xs,
                borderRadius: theme.radius.sm,
                color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.black,

                "&:hover": {
                    backgroundColor:
                        theme.colorScheme === "dark" ? theme.colors.dark[5] : theme.colors.blue[1],
                },
                ...(isActive && {
                    backgroundColor:
                        theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.colors.blue[0],
                }),
            })}
            onClick={() => navigate(to)}
            mt="xs"
        >
            <Group>
                <ThemeIcon color={color} variant="light">
                    {icon}
                </ThemeIcon>

                <Text size="sm">{label}</Text>
            </Group>
        </UnstyledButton>
    );
};

export default MenuButton;
