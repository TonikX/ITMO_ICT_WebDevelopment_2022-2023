import React from "react";

import { Navbar, Divider } from "@mantine/core";
import { IconBook, IconUser } from "@tabler/icons-react";
import { MANTINE_COLORS } from "@mantine/styles";

import Brand from "~/components/Brand";
import MenuButton from "~/components/MenuButton";
import User from "~/components/User";
import chooseWeightedIndex from "~/utils/ChooseRandom";
import { useGetUserData } from "~/hooks";

const initData = [
    { icon: <IconUser size="1rem" />, color: "teal", label: "Profile", to: "/profile" },
];

const Sidebar = ({ queryClient, libraries, librariesStatus, opened, setOpened }) => {
    const { data: user, status: userStatus } = useGetUserData();

    let data = [];
    if (userStatus === "success" && librariesStatus === "success") {
        const userLibrary = libraries.find(
            (library) => library.id === user.library || library.id === user.library?.id
        );
        if (userLibrary) {
            data = userLibrary.readingroom_set.map(({ id, name }) => {
                const choice = chooseWeightedIndex(MANTINE_COLORS, name);
                const randomColor = MANTINE_COLORS[choice];
                return {
                    icon: <IconBook size="1rem" />,
                    color: randomColor,
                    label: name,
                    to: "/" + id,
                };
            });
        }
    }

    return (
        <Navbar p="md" hiddenBreakpoint="sm" hidden={!opened} width={{ sm: 240, lg: 300 }}>
            <Navbar.Section mt="xs">
                <Brand sidebarOpened={opened} setSidebarOpened={setOpened} />
            </Navbar.Section>

            <Navbar.Section grow mt="md">
                {initData &&
                    initData.map((link) => (
                        <div key={link.label}>
                            <MenuButton {...link} setSidebarOpened={setOpened} />
                        </div>
                    ))}
                <Divider my="sm" label="Reading rooms" labelPosition="center" />
                {data &&
                    data.map((link) => (
                        <div key={link.label}>
                            <MenuButton {...link} setSidebarOpened={setOpened} />
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
