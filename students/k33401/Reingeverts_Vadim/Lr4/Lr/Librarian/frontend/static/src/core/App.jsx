import React, { useState } from "react";
import { MantineProvider, ColorSchemeProvider, AppShell, useMantineTheme } from "@mantine/core";
import { useMediaQuery, useFavicon } from "@mantine/hooks";
import { Notifications } from "@mantine/notifications";

import favicon from "~/images/favicon-96.png";
import Routes from "~/core/Routes";
import Sidebar from "~/components/Sidebar";
import Header from "~/components/Header";
import { useGetLibrariesPublic } from "~/hooks";

const App = ({ queryClient }) => {
    const theme = useMantineTheme();
    useFavicon(favicon);

    // https://github.com/mantinedev/mantine/blob/master/src/mantine-styles/src/theme/default-theme.ts
    const largerThanSm = `(max-width: ${theme.breakpoints.sm})`;
    const isCompactViewActive = useMediaQuery(largerThanSm);

    const [colorScheme, setColorScheme] = useState("dark");
    const toggleColorScheme = (value) =>
        setColorScheme(value || (colorScheme === "dark" ? "light" : "dark"));

    const [sidebarOpened, setSidebarOpened] = useState(false);

    const { data: libraries, status: librariesStatus } = useGetLibrariesPublic();

    return (
        <>
            <ColorSchemeProvider colorScheme={colorScheme} toggleColorScheme={toggleColorScheme}>
                <MantineProvider
                    theme={{
                        colorScheme,
                        colors: {
                            "light-blue-filled": Array(10).fill("#233549"),
                        },
                    }}
                    withGlobalStyles
                    withNormalizeCSS
                >
                    <Notifications />
                    <AppShell
                        padding={32}
                        layout="alt"
                        styles={{
                            main: {
                                background:
                                    colorScheme === "dark"
                                        ? theme.colors.dark[8]
                                        : theme.colors.gray[0],
                            },
                        }}
                        navbarOffsetBreakpoint="sm"
                        asideOffsetBreakpoint="sm"
                        navbar={
                            <Sidebar
                                queryClient={queryClient}
                                libraries={libraries}
                                librariesStatus={librariesStatus}
                                opened={sidebarOpened}
                                setOpened={setSidebarOpened}
                            />
                        }
                        header={
                            isCompactViewActive ? (
                                <Header
                                    sidebarOpened={sidebarOpened}
                                    setSidebarOpened={setSidebarOpened}
                                />
                            ) : null
                        }
                    >
                        <Routes
                            queryClient={queryClient}
                            isCompactViewActive={isCompactViewActive}
                        />
                    </AppShell>
                </MantineProvider>
            </ColorSchemeProvider>
        </>
    );
};

export default App;
