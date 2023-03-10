import React, { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "@mantine/form";
import { TextInput, PasswordInput, Group, Button, Box } from "@mantine/core";

import notification from "~/components/Notification";
import NonFieldErrors from "~/components/NonFieldErrors";
import backendApi from "~/utils/BackendApi";

const LoginForm = ({ isLoggedIn, isUserMutating, setToken }) => {
    const [nonFieldErrors, setNonFieldErrors] = useState([]);

    const form = useForm({
        initialValues: {
            username: "",
            password: "",
        },
        validate: {
            username: (value) => (value.length === 0 ? "Please, enter your username" : null),
            password: (value) => (value.length === 0 ? "Please, enter your password" : null),
        },
        validateInputOnBlur: true,
    });

    const handleFieldErrors = (json) => {
        const { non_field_errors, ...fieldErrors } = json;
        if (non_field_errors) {
            setNonFieldErrors(json["non_field_errors"]);
        }
        form.setErrors(fieldErrors);
    };

    const postLogin = useMutation(backendApi.postLogin, {
        mutationKey: "user",
        onSuccess: ({ json, ok }) => {
            if (ok) {
                setToken(json["auth_token"]);
                notification.showSuccess("Logged In.");
            } else {
                handleFieldErrors(json);
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const handleLoginSubmit = ({ username, password }) => {
        if (!isLoggedIn && !isUserMutating) {
            postLogin.mutate({
                username,
                password,
            });
        }
    };
    return (
        <Box maw={340} mx="auto" mb="xs">
            <NonFieldErrors errors={nonFieldErrors} />
            <form onSubmit={form.onSubmit(handleLoginSubmit)}>
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

                <Group position="right" mt="xl">
                    <Button variant="light" type="submit">
                        Log In
                    </Button>
                </Group>
            </form>
        </Box>
    );
};

export default LoginForm;
