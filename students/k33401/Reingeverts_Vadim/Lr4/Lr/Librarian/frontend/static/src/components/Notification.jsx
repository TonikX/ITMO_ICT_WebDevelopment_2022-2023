import { notifications } from "@mantine/notifications";
import { IconX } from "@tabler/icons-react";

const showError = (error) => {
    notifications.show({
        title: "Oops, it seems that something went wrong",
        message: error.statusText || error.message,
        color: "red",
        icon: <IconX />,
    });
};

const notification = {
    showError,
};

export default notification;
