import React, { useEffect, useState } from "react";
import { useLocalStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";
import { useForm } from "@mantine/form";
import { Text, TextInput, PasswordInput, Group, Button, Box } from "@mantine/core";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const sessionStorageToken = JSON.parse(sessionStorage.getItem("token"));

const Login = ({ queryClient }) => {
    const [token, setToken] = useLocalStorage({ key: "token", defaultValue: sessionStorageToken });
    const isLoggedIn = !!token;
    const isProfileMutating = useIsMutating("profile");
    const [nonFieldErrors, setNonFieldErrors] = useState([]);

    const form = useForm({
        initialValues: {
            username: "",
            password: "",
        },
        validate: {
            // username: (value) => (value.length === 0 ? "Please, enter your username" : null),
            // password: (value) => (value.length === 0 ? "Please, enter your password" : null),
        },
        validateInputOnBlur: true,
    });

    const { data, status } = useQuery(["profile"], () => backendApi.fetchLogin(), {
        onError: () => {
            console.log("token is invalid");
            setToken(null);
            notification.showSuccess("Logged Out");
        },
        retry: 0,
        enabled: isLoggedIn,
    });

    const postLogin = useMutation(backendApi.postLogin, {
        mutationKey: "profile",
        onSuccess: ({ json, ok }) => {
            if (ok) {
                setToken(json["auth_token"]);
                notification.showSuccess("Logged In");
            } else {
                const { non_field_errors, ...fieldErrors } = json;
                if (non_field_errors) {
                    setNonFieldErrors(json["non_field_errors"]);
                }
                form.setErrors(fieldErrors);
            }
        },
        onError: notification.showError,
        retry: 0,
    });
    const postLogout = useMutation(backendApi.postLogout, {
        mutationKey: "profile",
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

    useEffect(() => {
        sessionStorage.setItem("token", JSON.stringify(token));
        queryClient.invalidateQueries("profile");
    }, [isLoggedIn]);

    const handleLogin = ({ username, password }) => {
        if (!isLoggedIn && !isProfileMutating) {
            postLogin.mutate({
                username,
                password,
            });
        }
    };
    const handleLogout = () => {
        if (isLoggedIn && !isProfileMutating) {
            postLogout.mutate();
        }
    };

    if (!isLoggedIn) {
        return (
            <Box maw={340} mx="auto">
                {nonFieldErrors &&
                    nonFieldErrors.map((nonFieldError, index) => (
                        <Text key={index} color="red">
                            {nonFieldError}
                        </Text>
                    ))}
                <form onSubmit={form.onSubmit(handleLogin)}>
                    <TextInput
                        mt="sm"
                        label="Username"
                        placeholder="Username"
                        {...form.getInputProps("username")}
                    />
                    <PasswordInput
                        mt="sm"
                        label="Password"
                        placeholder="Password"
                        {...form.getInputProps("password")}
                    />

                    <Group position="right" mt="md">
                        <Button type="submit">Submit</Button>
                    </Group>
                </form>
            </Box>
        );
    } else {
        return (
            <>
                <button onClick={handleLogout}>logout</button>
            </>
        );
    }
};

export default Login;
