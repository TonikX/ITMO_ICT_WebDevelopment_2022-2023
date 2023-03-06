import React from "react";
import { useQuery, useMutation } from "@tanstack/react-query";

import notification from "~/components/Notification";
import backendApi from "~/utils/BackendApi";

const User = ({ queryClient }) => {
    const { data, status } = useQuery(["users"], () => backendApi.fetchUsers(), {
        onError: notification.showError,
    });

    const postUsers = useMutation(backendApi.postUsers, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: notification.showError,
        retry: 0,
    });
    const patchUserDetails = useMutation(backendApi.patchUserDetails, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: notification.showError,
        retry: 0,
    });
    const deleteUserDetails = useMutation(backendApi.deleteUserDetails, {
        onSuccess: (res) => {
            console.log(res);
            console.log("Users are invalidated");
            queryClient.invalidateQueries("users");
        },
        onError: notification.showError,
        retry: 0,
    });

    if (status === "loading") {
        return <>Loading users...</>;
    }
    return (
        <>
            <ul>
                {data?.["User"] &&
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
                        userId: 7,
                    })
                }
            >
                Delete user 2
            </button>
        </>
    );
};

export default User;
