import React, { useEffect, useState } from "react";
import {
    Stepper,
    TextInput,
    Select,
    NativeSelect,
    PasswordInput,
    Group,
    Button,
    Loader,
} from "@mantine/core";
import { useToggle, useDidUpdate, useSetState } from "@mantine/hooks";
import { DateInput } from "@mantine/dates";
import { useForm } from "@mantine/form";
import { useMutation } from "@tanstack/react-query";

import InputGroup from "~/components/InputGroup";
import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const fieldsToCheckAtStep = {
    0: ["username", "email"],
    1: ["date_of_birth", "phone_number"],
    2: [],
};

const filedsWithChoices = ["academic_degree"];

const listToObject = (keys = [], value = "") => {
    // https://stackoverflow.com/a/36388401
    return keys.reduce((a, v) => ({ ...a, [v]: value }), {});
};

const Signup = ({
    queryClient,
    isLoggedIn,
    isUserMutating,
    closeModal,
    libraries,
    librariesStatus,
}) => {
    const [nonFieldErrors, setNonFieldErrors] = useState([]);
    const [fieldChoices, setFieldChoices] = useSetState({});

    const [step, setStep] = useState(0);
    const [currentStepStatus, toggleCurrentStepStatus] = useToggle([
        "unchecked",
        "checked",
        "checking",
    ]);

    const handleFieldErrors = (errors) => {
        const { non_field_errors, ...fieldErrors } = errors;
        if (non_field_errors) {
            setNonFieldErrors(errors["non_field_errors"]);
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
                handleFieldErrors(json["field_errors"]);
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const postCheckField = useMutation(backendApi.postCheckField, {
        onSuccess: ({ json, ok }) => {
            const didReturnChoices = Object.keys(json["field_choices"]).length !== 0;
            if (!didReturnChoices) {
                if (ok) {
                    setNonFieldErrors([]);
                    toggleCurrentStepStatus("checked");
                } else {
                    handleFieldErrors(json["field_errors"]);
                    toggleCurrentStepStatus("unchecked");
                }
            } else {
                const inputChoices = convertDjangoChoices(json["field_choices"]);
                setFieldChoices(inputChoices);
            }
        },
        onError: notification.showError,
        retry: 0,
    });

    const convertDjangoChoices = (djangoChoices) => {
        let inputChoiceList = {};
        for (const [field, choices] of Object.entries(djangoChoices)) {
            inputChoiceList[field] = choices.map((choiceTuple) => choiceTuple[0]);
        }
        return inputChoiceList;
    };
    const convertModelForeignKeys = (djangoModelObjects) => {
        const inputChoiceObject = {
            library: djangoModelObjects.map((object) => ({
                label: object.name,
                value: object.id.toString(),
            })),
        };
        return inputChoiceObject;
    };

    const getFormChoices = () => {
        const fields = listToObject(filedsWithChoices, "");
        postCheckField.mutate({
            body: {
                User: fields,
            },
        });
    };

    useEffect(() => {
        getFormChoices();
    }, []);

    useEffect(() => {
        if (librariesStatus === "success") {
            const inputChoiceObject = convertModelForeignKeys(libraries);
            setFieldChoices(inputChoiceObject);
        }
    }, [librariesStatus]);

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

            library: "",
            academic_degree: "",
            education_level: "",
            passport: "",
            address: "",
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
        // Exclude empty
        const cleanedFields = Object.fromEntries(
            Object.entries(fields).filter(([_, v]) => v !== "")
        );
        delete cleanedFields["confirmPassword"];

        if (cleanedFields?.library) {
            cleanedFields.library = parseInt(cleanedFields.library);
            console.log("cleanedFields!", cleanedFields);
        }

        if (!isLoggedIn && !isUserMutating) {
            postUsers.mutate({
                body: {
                    User: cleanedFields,
                },
            });
        }
    };

    const nextStep = () => {
        if (form.validate().hasErrors || currentStepStatus === "checking") return;

        const doesStepRequiresChecking = fieldsToCheckAtStep[step].length !== 0;
        if (currentStepStatus === "unchecked" && doesStepRequiresChecking) {
            const fieldsToCheck = Object.fromEntries(
                Object.entries(form.values).filter(
                    ([key, value]) => fieldsToCheckAtStep[step].includes(key) && value !== ""
                )
            );

            const areFieldValuesNonEmpty = fieldsToCheck.length !== 0;
            if (areFieldValuesNonEmpty) {
                toggleCurrentStepStatus(() => "checking");

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
            nextStep();
        }
    }, [currentStepStatus]);

    const prevStep = () =>
        setStep((current) => {
            toggleCurrentStepStatus("unchecked");
            return current > 0 ? current - 1 : current;
        });

    const conditionalLoader = currentStepStatus === "checking" ? <Loader size="xs" /> : null;
    return (
        <>
            <Stepper mx="xl" active={step} breakpoint="sm">
                <Stepper.Step
                    label="First step"
                    description="Account information"
                    loading={step === 0 && currentStepStatus === "checking"}
                >
                    <InputGroup nonFieldErrors={nonFieldErrors}>
                        <TextInput
                            label="Username"
                            placeholder="Username"
                            {...form.getInputProps("username")}
                            withAsterisk
                            rightSection={conditionalLoader}
                        />
                        <TextInput
                            mt="sm"
                            label="Email"
                            placeholder="Email"
                            {...form.getInputProps("email")}
                            withAsterisk
                            rightSection={conditionalLoader}
                        />
                        <PasswordInput
                            mt="md"
                            label="Password"
                            placeholder="Password"
                            {...form.getInputProps("password")}
                            withAsterisk
                        />
                        <PasswordInput
                            mt="sm"
                            label="Confirm password"
                            placeholder="Confirm password"
                            {...form.getInputProps("confirmPassword")}
                            withAsterisk
                        />
                    </InputGroup>
                </Stepper.Step>

                <Stepper.Step
                    label="Second step"
                    description="Personal information"
                    loading={step === 1 && currentStepStatus === "checking"}
                >
                    <InputGroup nonFieldErrors={nonFieldErrors}>
                        <TextInput
                            label="Last name"
                            placeholder="Last name"
                            {...form.getInputProps("last_name")}
                            withAsterisk
                        />
                        <TextInput
                            mt="sm"
                            label="First name"
                            placeholder="First name"
                            {...form.getInputProps("first_name")}
                            withAsterisk
                        />
                        <TextInput
                            mt="sm"
                            label="Middle name"
                            placeholder="Middle name"
                            {...form.getInputProps("middle_name")}
                        />
                        <DateInput
                            mt="md"
                            label="Date of birth"
                            placeholder="30.12.1990"
                            valueFormat="DD.MM.YYYY"
                            {...form.getInputProps("date_of_birth")}
                            rightSection={conditionalLoader}
                        />
                        <TextInput
                            mt="sm"
                            label="Phone number"
                            placeholder="+7 (900) 111 22-33"
                            {...form.getInputProps("phone_number")}
                            rightSection={conditionalLoader}
                        />
                    </InputGroup>
                </Stepper.Step>

                <Stepper.Step
                    label="Final step"
                    description="Additional information"
                    loading={step === 2 && currentStepStatus === "checking"}
                >
                    <InputGroup nonFieldErrors={nonFieldErrors}>
                        <Select
                            mt="sm"
                            label="Library"
                            placeholder="Library"
                            {...form.getInputProps("library")}
                            data={fieldChoices.library ?? []}
                        />
                        <NativeSelect
                            mt="md"
                            label="Academic degree"
                            placeholder="Academic degree"
                            {...form.getInputProps("academic_degree")}
                            data={fieldChoices?.academic_degree ?? []}
                        />
                        <TextInput
                            mt="sm"
                            label="Education level"
                            placeholder="Education level"
                            {...form.getInputProps("education_level")}
                        />

                        <TextInput
                            mt="md"
                            label="Passport"
                            placeholder="Passport"
                            {...form.getInputProps("passport")}
                        />
                        <TextInput
                            mt="sm"
                            label="Address"
                            placeholder="Address"
                            {...form.getInputProps("address")}
                        />
                    </InputGroup>
                </Stepper.Step>
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
