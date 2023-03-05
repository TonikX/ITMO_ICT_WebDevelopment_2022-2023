import React, { useState } from "react";
import {
    AppShell,
    Navbar,
    Header,
    Footer,
    Aside,
    Text,
    MediaQuery,
    Burger,
    useMantineTheme,
} from "@mantine/core";

import Routes from "~/core/Routes";

const App = ({ queryClient }) => {
    const theme = useMantineTheme();
    const [opened, setOpened] = useState(false);

    return (
        <>
            <AppShell
                styles={{
                    main: {
                        background:
                            theme.colorScheme === "dark"
                                ? theme.colors.dark[8]
                                : theme.colors.gray[0],
                    },
                }}
                navbarOffsetBreakpoint="sm"
                navbar={
                    <Navbar
                        p="md"
                        hiddenBreakpoint="sm"
                        hidden={!opened}
                        width={{ sm: 200, lg: 300 }}
                    >
                        {/* First section with normal height (depends on section content) */}
                        <Navbar.Section>First section</Navbar.Section>

                        {/* Grow section will take all available space that is not taken by first and last sections */}
                        <Navbar.Section grow>Grow section</Navbar.Section>

                        {/* Last section with normal height (depends on section content) */}
                        <Navbar.Section>Last section</Navbar.Section>
                    </Navbar>
                }
            >
                <Routes queryClient={queryClient} />
            </AppShell>
        </>
    );
};

export default App;
