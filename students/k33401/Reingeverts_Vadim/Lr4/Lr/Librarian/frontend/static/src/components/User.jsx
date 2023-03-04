import React from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { notifications } from "@mantine/notifications";
import { IconX } from "@tabler/icons-react";

import backendApi from "~/utils/BackendApi";

const token = "4ed1fe7242281538e75beeaa9d139e2cd9f3c1b4";

const User = ({ queryClient }) => {
    const { data, status } = useQuery(["users"], () => backendApi.fetchUsers({ token }), {
        onError: (error) =>
            notifications.show({
                title: "Oops, it seems that something went wrong",
                message: error.statusText || error.message,
                color: "red",
                icon: <IconX />,
            }),
    });

    const postUsers = useMutation(backendApi.postUsers, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: (error) => {
            notifications.show({
                title: "Oops, it seems that something went wrong",
                message: error.statusText || error.message,
                color: "red",
                icon: <IconX />,
            });
        },
    });
    const patchUserDetails = useMutation(backendApi.patchUserDetails, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: (error) =>
            notifications.show({
                title: "Oops, it seems that something went wrong",
                message: error.statusText || error.message,
                color: "red",
                icon: <IconX />,
            }),
    });
    const deleteUserDetails = useMutation(backendApi.deleteUserDetails, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: (error) =>
            notifications.show({
                title: "Oops, it seems that something went wrong",
                message: error.statusText || error.message,
                color: "red",
                icon: <IconX />,
            }),
    });

    if (status === "loading") {
        return <>Loading users...</>;
    }
    return (
        <>
            <ul>
                {data["User"] &&
                    data["User"].map((user) => (
                        <li key={user.id}>
                            <p>User</p>
                            <ul>
                                <li>id: {user.id}</li>
                                <li>username: {user.username}</li>
                                <li>first_name: {user.first_name}</li>
                                <li>serial_number: {user.serial_number}</li>
                                <li>password: {user.password}</li>
                            </ul>
                        </li>
                    ))}
            </ul>

            <button
                onClick={() =>
                    postUsers.mutate({
                        token,
                        body: {
                            User: { username: "MRA", password: "cool as well" },
                        },
                    })
                }
            >
                Add user
            </button>
            <button
                onClick={() =>
                    patchUserDetails.mutate({
                        userId: 5,
                        token,
                        body: {
                            User: { first_name: "brand new name" },
                        },
                    })
                }
            >
                Update user 2 name
            </button>
            <button
                onClick={() =>
                    deleteUserDetails.mutate({
                        userId: 5,
                        token,
                    })
                }
            >
                Delete user 2
            </button>
        </>
    );
};

export default User;
