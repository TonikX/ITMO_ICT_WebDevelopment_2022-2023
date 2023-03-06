import React from "react";
import { Button } from "@mantine/core";
import { useMutation } from "@tanstack/react-query";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const LogoutButton = ({ isLoggedIn, isUserMutating, setToken }) => {
    const postLogout = useMutation(backendApi.postLogout, {
        mutationKey: "user",
        onSuccess: ({ json, ok }) => {
            console.log("LOGOUT");
            console.log("json", json, "ok", ok);
            if (ok) {
                setToken(null);
                notification.showSuccess("Logged Out");
            } else {
                notification.showError(json);
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const handleLogout = () => {
        if (isLoggedIn && !isUserMutating) {
            postLogout.mutate();
        }
    };

    return (
        <Button variant="light" color="red" onClick={handleLogout}>
            Log Out
        </Button>
    );
};

export default LogoutButton;
