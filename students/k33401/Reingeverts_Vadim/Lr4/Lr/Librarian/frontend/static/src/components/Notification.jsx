import { notifications } from "@mantine/notifications";
// https://tabler-icons.io/
import { IconX, IconCheck } from "@tabler/icons-react";

const showError = (error) => {
    const message = error?.statusText ?? error?.message ?? error?.detail ?? JSON.stringify(error);

    notifications.show({
        title: "Oops, it seems that something went wrong",
        message,
        color: "red",
        icon: <IconX />,
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
    showSuccess,
};

export default notification;
