import React, { useEffect } from "react";
import { useLocalStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const sessionStorageToken = JSON.parse(sessionStorage.getItem("token"));

const Login = ({ queryClient }) => {
    const [token, setToken] = useLocalStorage({ key: "token", defaultValue: sessionStorageToken });
    const isLoggedIn = !!token;
    const isProfileMutating = useIsMutating("profile");

    const { data, status } = useQuery(["profile"], () => backendApi.fetchLogin(), {
        onError: notification.showError,
        retry: 0,
        enabled: isLoggedIn,
    });

    const postLogin = useMutation(backendApi.postLogin, {
        mutationKey: "profile",
        onSuccess: (res) => {
            setToken(res["auth_token"]);
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

    useEffect(() => {
        sessionStorage.setItem("token", JSON.stringify(token));
        queryClient.invalidateQueries("profile");
    }, [isLoggedIn]);

    const handleLogin = () => {
        if (!isLoggedIn && !isProfileMutating) {
            postLogin.mutate({
                username: "cool3",
                password: "cool as well",
            });
        }
    };
    const handleLogout = () => {
        if (isLoggedIn && !isProfileMutating) {
            postLogout.mutate();
        }
    };
    return (
        <>
            User: {isLoggedIn && data && data.username}
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleLogout}>logout</button>
        </>
    );
};

export default Login;
