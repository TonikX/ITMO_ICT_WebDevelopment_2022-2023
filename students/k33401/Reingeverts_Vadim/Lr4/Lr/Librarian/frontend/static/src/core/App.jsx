import React, { useState } from "react";
import { MantineProvider, ColorSchemeProvider, AppShell, useMantineTheme } from "@mantine/core";
import { Notifications } from "@mantine/notifications";

import Routes from "~/core/Routes";
import Sidebar from "~/components/Sidebar";
import Header from "~/components/Header";

const App = ({ queryClient }) => {
    const theme = useMantineTheme();
    const [colorScheme, setColorScheme] = useState("dark");
    const toggleColorScheme = (value) =>
        setColorScheme(value || (colorScheme === "dark" ? "light" : "dark"));

    const [sidebarOpened, setSidebarOpened] = useState(false);

    return (
        <>
            <ColorSchemeProvider colorScheme={colorScheme} toggleColorScheme={toggleColorScheme}>
                <MantineProvider theme={{ colorScheme }} withGlobalStyles withNormalizeCSS>
                    <Notifications />
                    <AppShell
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
                        navbar={<Sidebar opened={sidebarOpened} setOpened={setSidebarOpened} />}
                        header={
                            <Header
                                sidebarOpened={sidebarOpened}
                                setSidebarOpened={setSidebarOpened}
                            />
                        }
                    >
                        <Routes queryClient={queryClient} />
                    </AppShell>
                </MantineProvider>
            </ColorSchemeProvider>
        </>
    );
};

export default App;
