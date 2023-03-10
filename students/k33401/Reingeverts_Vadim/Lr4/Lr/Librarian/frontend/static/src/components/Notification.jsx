import { notifications } from "@mantine/notifications";
// https://tabler-icons.io/
import { IconX, IconCheck, IconExclamationMark } from "@tabler/icons-react";

const showError = (error) => {
    const message = error?.statusText ?? error?.message ?? error?.detail ?? JSON.stringify(error);

    notifications.show({
        title: "Oops, it seems that something went wrong",
        message,
        color: "red",
        icon: <IconX />,
    });
};
const showAlert = (message) => {
    notifications.show({
        title: "Note that",
        message,
        color: "orange",
        icon: <IconExclamationMark />,
    });
};

const showSuccess = (message) => {
    notifications.show({
        title: "Success",
        message,
        color: "teal",
        icon: <IconCheck />,
    });
};

const notification = {
    showError,
    showAlert,
    showSuccess,
};

export default notification;
