import React from "react";
import {
    Group,
    ActionIcon,
    useMantineColorScheme,
    Box,
    rem,
    Burger,
    MediaQuery,
    useMantineTheme,
} from "@mantine/core";
import { IconSun, IconMoonStars } from "@tabler/icons-react";

import BrandLogo from "~/components/BrandLogo";

const Brand = ({ sidebarOpened, setSidebarOpened }) => {
    const theme = useMantineTheme();

    const { colorScheme, toggleColorScheme } = useMantineColorScheme();
    return (
        <Box
            sx={(theme) => ({
                paddingLeft: theme.spacing.xs,
                paddingRight: theme.spacing.xs,
                paddingBottom: theme.spacing.lg,
                borderBottom: `${rem(1)} solid ${
                    theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[2]
                }`,
            })}
        >
            <Group position="apart">
                <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                    <Burger
                        opened={sidebarOpened}
                        onClick={() => setSidebarOpened((o) => !o)}
                        size="sm"
                        color={theme.colors.gray[6]}
                    />
                </MediaQuery>
                <BrandLogo />

                <ActionIcon variant="default" onClick={() => toggleColorScheme()} size={30}>
                    {colorScheme === "dark" ? (
                        <IconSun size="1rem" />
                    ) : (
                        <IconMoonStars size="1rem" />
                    )}
                </ActionIcon>
            </Group>
        </Box>
    );
};

export default Brand;
