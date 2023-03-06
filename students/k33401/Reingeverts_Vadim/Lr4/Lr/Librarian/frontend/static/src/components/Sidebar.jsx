import React from "react";

import { Navbar } from "@mantine/core";

import {
    IconGitPullRequest,
    IconAlertCircle,
    IconMessages,
    IconDatabase,
} from "@tabler/icons-react";

import Brand from "~/components/Brand";
import MenuButton from "~/components/MenuButton";
import User from "~/components/User";

const data = [
    { icon: <IconGitPullRequest size="1rem" />, color: "blue", label: "Pull Requests" },
    { icon: <IconAlertCircle size="1rem" />, color: "teal", label: "Open Issues" },
    { icon: <IconMessages size="1rem" />, color: "violet", label: "Discussions" },
    { icon: <IconDatabase size="1rem" />, color: "grape", label: "Databases" },
];

const Sidebar = ({ queryClient, opened, setOpened }) => {
    return (
        <Navbar p="md" hiddenBreakpoint="sm" hidden={!opened} width={{ sm: 240, lg: 300 }}>
            <Navbar.Section mt="xs">
                <Brand sidebarOpened={opened} setSidebarOpened={setOpened} />
            </Navbar.Section>

            <Navbar.Section grow mt="md">
                {data.map((link) => (
                    <div key={link.label}>
                        <MenuButton {...link} />
                    </div>
                ))}
            </Navbar.Section>

            <Navbar.Section>
                <User queryClient={queryClient} />
            </Navbar.Section>
        </Navbar>
    );
};

export default Sidebar;
