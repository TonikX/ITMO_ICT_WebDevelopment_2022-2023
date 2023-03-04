import React from "react";
import { useQuery } from "@tanstack/react-query";

import backendApi from "~/utils/BackendApi";

const User = () => {
    const { data, status } = useQuery(["users"], backendApi.fetchUsers);
    console.log("data, status", data, status);
    if (status === "loading") {
        return <>Loading users...</>;
    }
    if (status === "error") {
        return <>Error</>;
    }
    return JSON.stringify(data["User"]);
    // <ul>
    //     {data["User"].map((user) => (
    //         <li key={user.id}>{user.username}</li>
    //     ))}
    // </ul>
};

export default User;
