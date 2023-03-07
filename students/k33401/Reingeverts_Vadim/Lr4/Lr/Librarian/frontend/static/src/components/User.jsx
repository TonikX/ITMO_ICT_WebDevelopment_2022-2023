import React, { useEffect } from "react";
import { UnstyledButton, Box, useMantineTheme, rem, Popover, MediaQuery } from "@mantine/core";
import { IconChevronRight } from "@tabler/icons-react";
import { useLocalStorage } from "@mantine/hooks";
import { useIsMutating } from "@tanstack/react-query";

import UserContent from "~/components/UserContent";
import LogoutButton from "~/components/LogoutButton";
import AdmissionModals from "~/components/AdmissionModals";
import { getSessionStorageToken, setSessionStorageToken } from "~/utils/Token";

const getUserContainerSx = (theme) => {
    return {
        display: "block",
        width: "100%",
        padding: theme.spacing.xs,
        borderRadius: theme.radius.sm,
        color: theme.colorScheme === "dark" ? theme.colors.dark[0] : theme.black,

        "&:hover": {
            backgroundColor:
                theme.colorScheme === "dark" ? theme.colors.dark[6] : theme.colors.gray[0],
        },
    };
};

const User = ({ queryClient }) => {
    const theme = useMantineTheme();

    const [token, setToken] = useLocalStorage({
        key: "token",
        defaultValue: getSessionStorageToken(),
    });
    const isLoggedIn = !!token;
    const logout = () => setToken(null);

    const isUserMutating = useIsMutating("user");

    useEffect(() => {
        setSessionStorageToken(token);
        queryClient.invalidateQueries("user");
    }, [isLoggedIn]);

    return (
        <Box
            sx={{
                paddingTop: theme.spacing.sm,
                borderTop: `${rem(1)} solid ${
                    theme.colorScheme === "dark" ? theme.colors.dark[4] : theme.colors.gray[2]
                }`,
            }}
        >
            {isLoggedIn && (
                <>
                    <MediaQuery smallerThan="sm" styles={{ display: "none" }}>
                        <Popover position="right" shadow="md" radius="sm" offset={8}>
                            <Popover.Target>
                                <UnstyledButton sx={getUserContainerSx(theme)}>
                                    <UserContent right={<IconChevronRight size={rem(18)} />} />
                                </UnstyledButton>
                            </Popover.Target>
                            <Popover.Dropdown>
                                <LogoutButton
                                    isLoggedIn={isLoggedIn}
                                    isUserMutating={isUserMutating}
                                    logout={logout}
                                />
                            </Popover.Dropdown>
                        </Popover>
                    </MediaQuery>
                    <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                        <Box sx={getUserContainerSx(theme)}>
                            <UserContent
                                right={
                                    <LogoutButton
                                        isLoggedIn={isLoggedIn}
                                        isUserMutating={isUserMutating}
                                        setToken={setToken}
                                    />
                                }
                            />
                        </Box>
                    </MediaQuery>
                </>
            )}
            {!isLoggedIn && (
                <AdmissionModals
                    queryClient={queryClient}
                    isLoggedIn={isLoggedIn}
                    isUserMutating={isUserMutating}
                    setToken={setToken}
                />
            )}
        </Box>
    );
};

export default User;
