import React from "react";
import { useSessionStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const Login = ({ queryClient }) => {
    const [token, setToken] = useSessionStorage({ key: "token" });
    const isProfileMutating = useIsMutating("profile");

    const { data, status } = useQuery(["profile"], () => backendApi.fetchLogin(), {
        onError: notification.showError,
        retry: 0,
        enabled: !!token,
    });

    const postLogin = useMutation(backendApi.postLogin, {
        mutationKey: "profile",
        onSuccess: (res) => {
            setToken(res["auth_token"]);
            queryClient.invalidateQueries("profile");
        },
        onError: notification.showError,
        retry: 0,
    });
    const postLogout = useMutation(backendApi.postLogout, {
        mutationKey: "profile",
        onSuccess: () => {
            setToken(null);
        },
        onError: notification.showError,
        retry: 0,
    });

    const handleLogin = () => {
        if (!token && !isProfileMutating) {
            postLogin.mutate({
                username: "cool3",
                password: "cool as well",
            });
        }
    };
    const handleLogout = () => {
        if (token && !isProfileMutating) {
            postLogout.mutate();
        }
    };
    return (
        <>
            User: {token && data && data.username}
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleLogout}>logout</button>
        </>
    );
};

export default Login;
