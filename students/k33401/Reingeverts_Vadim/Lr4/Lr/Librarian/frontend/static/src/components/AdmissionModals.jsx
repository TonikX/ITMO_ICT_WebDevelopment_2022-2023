import React, { useEffect, useState } from "react";
import { useLocalStorage, useDisclosure, useToggle } from "@mantine/hooks";
import { useQuery, useMutation, useIsMutating } from "@tanstack/react-query";
import { Text, TextInput, PasswordInput, Group, Box, Modal, Button } from "@mantine/core";

import LoginForm from "~/components/LoginForm";
import SignupForm from "~/components/SignupForm";
import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";
import { getSessionStorageToken } from "~/utils/Token";

const AdmissionModals = ({ queryClient, isLoggedIn, isUserMutating, setToken }) => {
    const [opened, { open, close }] = useDisclosure(false);
    const [admissionType, setAdmissionType] = useToggle(["Sign Up", "Log In"]);
    const admissionForm =
        admissionType === "Log In" ? (
            <LoginForm
                isLoggedIn={isLoggedIn}
                isUserMutating={isUserMutating}
                setToken={setToken}
            />
        ) : (
            <SignupForm
                queryClient={queryClient}
                isLoggedIn={isLoggedIn}
                isUserMutating={isUserMutating}
                closeModal={close}
            />
        );

    const handleLogin = () => {
        open();
        setAdmissionType("Sign Up");
    };
    const handleSignup = () => {
        open();
        setAdmissionType("Log In");
    };

    return (
        <>
            <Modal
                size={admissionType === "Sign Up" ? "xl" : null}
                opened={opened}
                onClose={close}
                title={
                    <Text fz="xl" fw={500}>
                        {admissionType}
                    </Text>
                }
            >
                {admissionForm}
            </Modal>

            <Group>
                <Button onClick={handleSignup} variant="light">
                    Log In
                </Button>
                <Button onClick={handleLogin} variant="subtle">
                    Sign Up
                </Button>
            </Group>
        </>
    );
};

export default AdmissionModals;
