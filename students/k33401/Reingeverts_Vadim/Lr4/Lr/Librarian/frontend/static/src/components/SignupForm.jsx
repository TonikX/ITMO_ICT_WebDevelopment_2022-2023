import React, { useState } from "react";
import { useToggle, useDidUpdate } from "@mantine/hooks";
import { DateInput } from "@mantine/dates";
import { useQuery, useMutation } from "@tanstack/react-query";
import { useForm } from "@mantine/form";
import { Stepper, TextInput, PasswordInput, Group, Button, Box, Code } from "@mantine/core";

import FormStep from "~/components/FormStep";
import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const fieldsToCheckAtStep = {
    0: ["username", "email"],
    1: ["date_of_birth", "phone_number"],
    2: [],
};

const Signup = ({ queryClient, isLoggedIn, isUserMutating, closeModal }) => {
    const [nonFieldErrors, setNonFieldErrors] = useState([]);

    const [step, setStep] = useState(0);
    const [currentStepStatus, toggleCurrentStepStatus] = useToggle([
        "unchecked",
        "checked",
        "checking",
    ]);

    const handleFieldErrors = (json) => {
        const { non_field_errors, ...fieldErrors } = json;
        if (non_field_errors) {
            setNonFieldErrors(json["non_field_errors"]);
        }
        form.setErrors(fieldErrors);
    };

    const postUsers = useMutation(backendApi.postUsers, {
        onSuccess: ({ json, ok }) => {
            if (ok) {
                queryClient.invalidateQueries("users");
                notification.showSuccess("Sign Up complete. You can login now.");
                closeModal();
            } else {
                handleFieldErrors(json);
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const postCheckField = useMutation(backendApi.postCheckField, {
        onSuccess: ({ json, ok }) => {
            console.log("response", json, ok);
            if (ok) {
                setNonFieldErrors([]);
                toggleCurrentStepStatus("checked");
            } else {
                handleFieldErrors(json);
                toggleCurrentStepStatus("unchecked");
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const form = useForm({
        initialValues: {
            username: "",
            email: "",
            password: "",
            confirmPassword: "",

            first_name: "",
            last_name: "",
            middle_name: "",
            date_of_birth: "",
            phone_number: "",

            address: "",
            passport: "",
            education_level: "",
            academic_degree: "",
        },

        validate: (fields) => {
            if (step === 0) {
                return {
                    username: fields.username.length === 0 ? "Please, enter your username" : null,
                    email: /^\S+@\S+$/.test(fields.email) ? null : "Invalid email",

                    password: fields.password.length === 0 ? "Please, enter your password" : null,
                    confirmPassword:
                        fields.password !== fields.confirmPassword
                            ? "Passwords did not match"
                            : null,
                };
            }

            if (step === 1) {
                return {
                    first_name:
                        fields.first_name.trim().length < 2
                            ? "First name must include at least 2 characters"
                            : null,
                    last_name:
                        fields.last_name.trim().length < 2
                            ? "Last name must include at least 2 characters"
                            : null,
                };
            }

            return {};
        },
    });

    const handleSignupSubmit = (fields) => {
        const cleanedFields = Object.fromEntries(
            Object.entries(fields).filter(([_, v]) => v !== "")
        );
        delete cleanedFields["confirmPassword"];
        console.log(cleanedFields["date_of_birth"]);

        console.log("can submit?", !isLoggedIn && !isUserMutating);
        console.log("submitting body...", {
            User: cleanedFields,
        });
        if (!isLoggedIn && !isUserMutating) {
            postUsers.mutate({
                body: {
                    User: cleanedFields,
                },
            });
        }
    };

    const nextStep = () => {
        if (form.validate().hasErrors || currentStepStatus === "checking") {
            return;
        }

        const doesStepRequiresChecking = fieldsToCheckAtStep[step].length !== 0;
        if (currentStepStatus === "unchecked" && doesStepRequiresChecking) {
            const fieldsToCheck = Object.fromEntries(
                Object.entries(form.values).filter(
                    ([key, value]) => fieldsToCheckAtStep[step].includes(key) && value !== ""
                )
            );

            const areFieldValuesNonEmpty = fieldsToCheck.length !== 0;
            console.log("areFieldValuesNonEmpty", areFieldValuesNonEmpty, fieldsToCheck);
            if (areFieldValuesNonEmpty) {
                toggleCurrentStepStatus((curr) => {
                    console.log(curr, "curr, but checking");
                    return "checking";
                });

                console.log("checking those", fieldsToCheck);
                postCheckField.mutate({
                    body: {
                        User: fieldsToCheck,
                    },
                });
                return;
            }
        }

        toggleCurrentStepStatus("unchecked");
        setStep((current) => (current < 2 ? current + 1 : current));
    };

    useDidUpdate(() => {
        if (currentStepStatus === "checked") {
            console.log("autosteppping", currentStepStatus);
            nextStep();
        }
    }, [currentStepStatus]);

    const prevStep = () =>
        setStep((current) => {
            toggleCurrentStepStatus("unchecked");
            return current > 0 ? current - 1 : current;
        });

    return (
        <>
            <Stepper mx="xl" active={step} breakpoint="sm">
                <Stepper.Step
                    label="First step"
                    description="Account information"
                    loading={step === 0 && currentStepStatus === "checking"}
                >
                    <FormStep nonFieldErrors={nonFieldErrors}>
                        <TextInput
                            label="Username"
                            placeholder="Username"
                            {...form.getInputProps("username")}
                        />
                        <TextInput
                            mt="md"
                            label="Email"
                            placeholder="Email"
                            {...form.getInputProps("email")}
                        />
                        <PasswordInput
                            mt="md"
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
                    </FormStep>
                </Stepper.Step>

                <Stepper.Step
                    label="Second step"
                    description="Personal information"
                    loading={step === 1 && currentStepStatus === "checking"}
                >
                    <FormStep nonFieldErrors={nonFieldErrors}>
                        <TextInput
                            label="Last name"
                            placeholder="Last name"
                            {...form.getInputProps("last_name")}
                        />
                        <TextInput
                            label="First name"
                            placeholder="First name"
                            {...form.getInputProps("first_name")}
                        />
                        <TextInput
                            label="Middle name"
                            placeholder="Middle name"
                            {...form.getInputProps("middle_name")}
                        />
                        <DateInput
                            label="Date of birth"
                            placeholder="30.12.1990"
                            // valueFormat="YYYY-MM-DD"
                            valueFormat="DD.MM.YYYY"
                            {...form.getInputProps("date_of_birth")}
                        />
                        <TextInput
                            label="Phone number"
                            placeholder="+7 (900) 111 22-33"
                            {...form.getInputProps("phone_number")}
                        />
                    </FormStep>
                </Stepper.Step>

                <Stepper.Step
                    label="Final step"
                    description="Additional information"
                    loading={step === 2 && currentStepStatus === "checking"}
                >
                    <FormStep nonFieldErrors={nonFieldErrors}>
                        <TextInput
                            label="Address"
                            placeholder="Address"
                            {...form.getInputProps("address")}
                        />
                        <TextInput
                            label="Passport"
                            placeholder="Passport"
                            {...form.getInputProps("passport")}
                        />
                        <TextInput
                            label="Education level"
                            placeholder="Education level"
                            {...form.getInputProps("education_level")}
                        />
                        <TextInput
                            label="Academic degree"
                            placeholder="Academic degree"
                            {...form.getInputProps("academic_degree")}
                        />
                    </FormStep>
                </Stepper.Step>
                {/* <Stepper.Completed>
                    Completed! Form values:
                    <Code block mt="xl">
                        {JSON.stringify(form.values, null, 2)}
                    </Code>
                </Stepper.Completed> */}
            </Stepper>

            <Group position="right" mt="xl">
                {step !== 0 && (
                    <Button variant="default" onClick={prevStep}>
                        Back
                    </Button>
                )}
                {step < 2 && (
                    <Button variant="light" onClick={nextStep}>
                        Next
                    </Button>
                )}
                {step === 2 && (
                    <Button
                        variant="light"
                        type="submit"
                        onClick={form.onSubmit(handleSignupSubmit)}
                    >
                        Sign Up
                    </Button>
                )}
            </Group>
        </>
    );
};

export default Signup;
