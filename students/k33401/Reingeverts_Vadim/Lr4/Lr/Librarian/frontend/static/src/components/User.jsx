import React, { useEffect } from "react";
import {
    UnstyledButton,
    Group,
    Avatar,
    Box,
    useMantineTheme,
    rem,
    Popover,
    Text,
    Button,
    MediaQuery,
} from "@mantine/core";
import { IconChevronRight, IconChevronLeft } from "@tabler/icons-react";
import { useLocalStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";

import UserContent from "~/components/UserContent";
import LogoutButton from "~/components/LogoutButton";
import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";
import { getSessionStorageToken } from "~/utils/Token";
import AdmissionModals from "~/components/AdmissionModals";

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
    const isUserMutating = useIsMutating("user");

    const { data, status } = useQuery(["user"], () => backendApi.fetchLogin(), {
        onError: () => {
            console.log("token is invalid");
            setToken(null);
            notification.showSuccess("Logged Out");
        },
        retry: 0,
        enabled: isLoggedIn,
    });
    const showUser = isLoggedIn && status === "success";

    useEffect(() => {
        sessionStorage.setItem("token", JSON.stringify(token));
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
            {showUser && (
                <>
                    <MediaQuery smallerThan="sm" styles={{ display: "none" }}>
                        <Popover position="right" shadow="md" radius="sm" offset={8}>
                            <Popover.Target>
                                <UnstyledButton sx={getUserContainerSx(theme)}>
                                    <UserContent
                                        data={data}
                                        right={<IconChevronRight size={rem(18)} />}
                                    />
                                </UnstyledButton>
                            </Popover.Target>
                            <Popover.Dropdown>
                                <LogoutButton
                                    isLoggedIn={isLoggedIn}
                                    isUserMutating={isUserMutating}
                                    setToken={setToken}
                                />
                            </Popover.Dropdown>
                        </Popover>
                    </MediaQuery>
                    <MediaQuery largerThan="sm" styles={{ display: "none" }}>
                        <Box sx={getUserContainerSx(theme)}>
                            <UserContent
                                data={data}
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
            {!showUser && (
                <AdmissionModals
                    isLoggedIn={isLoggedIn}
                    isUserMutating={isUserMutating}
                    setToken={setToken}
                />
            )}
        </Box>
    );
};

export default User;
