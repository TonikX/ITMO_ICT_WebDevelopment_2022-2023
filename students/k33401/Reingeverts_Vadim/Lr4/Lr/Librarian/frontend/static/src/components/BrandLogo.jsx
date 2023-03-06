import React from "react";
import { Group, Image, Title } from "@mantine/core";

import logo from "~/images/favicon-96.png";
const BrandLogo = () => {
    return (
        <Group spacing="xs">
            <Image maw={30} mx="auto" radius="xs" src={logo} />
            <Title size="h3">Librarian</Title>
        </Group>
    );
};

export default BrandLogo;
