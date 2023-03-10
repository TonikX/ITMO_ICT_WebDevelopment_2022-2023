import React from "react";
import { useDisclosure, useToggle } from "@mantine/hooks";
import { Text, Group, Modal, Button } from "@mantine/core";

import LoginForm from "~/components/LoginForm";
import SignupForm from "~/components/SignupForm";

const AdmissionModals = ({
    queryClient,
    isLoggedIn,
    isUserMutating,
    setToken,
    libraries,
    librariesStatus,
}) => {
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
                libraries={libraries}
                librariesStatus={librariesStatus}
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
