import React from "react";

import { Navbar } from "@mantine/core";
import { IconBook, IconUser } from "@tabler/icons-react";

import Brand from "~/components/Brand";
import MenuButton from "~/components/MenuButton";
import User from "~/components/User";

const data = [
    { icon: <IconBook size="1rem" />, color: "blue", label: "Library", to: "/" },
    { icon: <IconUser size="1rem" />, color: "teal", label: "Profile", to: "/profile" },
];

const Sidebar = ({ queryClient, libraries, librariesStatus, opened, setOpened }) => {
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
                <User
                    queryClient={queryClient}
                    libraries={libraries}
                    librariesStatus={librariesStatus}
                />
            </Navbar.Section>
        </Navbar>
    );
};

export default Sidebar;
