import React, { useEffect } from "react";
import { useLocalStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";
import { useForm } from "@mantine/form";
import { TextInput, PasswordInput, Group, Button, Box } from "@mantine/core";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const sessionStorageToken = JSON.parse(sessionStorage.getItem("token"));

const Signup = ({ queryClient, isLoggedIn, isUserMutating, closeModal }) => {
    const postUsers = useMutation(backendApi.postUsers, {
        onSuccess: ({ json, ok }) => {
            if (ok) {
                queryClient.invalidateQueries("users");
                notification.showSuccess("Sign Up complete. You can login now.");
                closeModal();
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

    const form = useForm({
        initialValues: {
            username: "",
            password: "",
            confirmPassword: "",
        },

        validate: {
            username: (value) => (value.length === 0 ? "Please, enter your username" : null),
            password: (value) => (value.length === 0 ? "Please, enter your password" : null),
            confirmPassword: (value, values) =>
                value !== values.password ? "Passwords did not match" : null,
        },
    });

    const handleSignupSubmit = ({ username, password }) => {
        if (!isLoggedIn && !isUserMutating) {
            postUsers.mutate({
                body: {
                    User: { username, password },
                },
            });
        }
    };

    return (
        <Box maw={340} mx="auto" mb="xs">
            <form onSubmit={form.onSubmit(handleSignupSubmit)}>
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

                <PasswordInput
                    mt="sm"
                    label="Confirm password"
                    placeholder="Confirm password"
                    {...form.getInputProps("confirmPassword")}
                />

                <Group position="right" mt="xl">
                    <Button variant="light" type="submit">
                        Submit
                    </Button>
                </Group>
            </form>
        </Box>
    );
};

export default Signup;
