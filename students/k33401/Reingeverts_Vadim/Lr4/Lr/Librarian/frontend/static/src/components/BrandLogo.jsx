import React from "react";
import { Group, Image, Title, UnstyledButton } from "@mantine/core";
import { useNavigate } from "react-router-dom";

import logo from "~/images/logo-256.webp";

const BrandLogo = ({ setSidebarOpened }) => {
    const navigate = useNavigate();

    const handleHomeClick = () => {
        setSidebarOpened(false);
        navigate("/");
    };

    return (
        <UnstyledButton onClick={handleHomeClick}>
            <Group spacing="xs">
                <Image maw={30} mx="auto" radius="xs" src={logo} />
                <Title size="h3">Librarian</Title>
            </Group>
        </UnstyledButton>
    );
};

export default BrandLogo;
