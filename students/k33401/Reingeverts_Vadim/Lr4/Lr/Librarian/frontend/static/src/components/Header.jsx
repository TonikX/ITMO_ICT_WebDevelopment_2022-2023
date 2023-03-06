import React from "react";
import { Header as MantineHeader, MediaQuery, Burger, useMantineTheme } from "@mantine/core";

import BrandLogo from "~/components/BrandLogo";

const Header = ({ sidebarOpened, setSidebarOpened }) => {
    const theme = useMantineTheme();

    return (
        <MediaQuery largerThan="sm" styles={{ display: "none" }}>
            <MantineHeader height={{ base: 77.5 }} p="md">
                <div style={{ display: "flex", alignItems: "center", height: "100%" }}>
                    <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                        <Burger
                            opened={sidebarOpened}
                            onClick={() => setSidebarOpened((o) => !o)}
                            size="sm"
                            color={theme.colors.gray[6]}
                            mr="xl"
                        />
                    </MediaQuery>

                    <BrandLogo />
                </div>
            </MantineHeader>
        </MediaQuery>
    );
};

export default Header;
