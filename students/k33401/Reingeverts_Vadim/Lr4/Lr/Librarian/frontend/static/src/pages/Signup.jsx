import React, { useEffect } from "react";
import { useLocalStorage } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";
import { useForm } from "@mantine/form";
import { TextInput, PasswordInput, Group, Button, Box } from "@mantine/core";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const sessionStorageToken = JSON.parse(sessionStorage.getItem("token"));

const Signup = () => {
    const form = useForm({
        initialValues: {
            username: "",
            password: "",
            confirmPassword: "",
        },

        validate: {
            confirmPassword: (value, values) =>
                value !== values.password ? "Passwords did not match" : null,
        },
    });

    // https://mantine.dev/form/recipes/#form-with-multiple-steps
    return (
        <Box maw={340} mx="auto">
            <form onSubmit={form.onSubmit((values) => console.log(values))}>
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

                <Group position="right" mt="md">
                    <Button type="submit">Submit</Button>
                </Group>
            </form>
        </Box>
    );
};

export default Signup;
