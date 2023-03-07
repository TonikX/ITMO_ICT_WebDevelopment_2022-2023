import React from "react";

import { useQuery } from "@tanstack/react-query";
import ContentPane from "~/components/ContentPane";
import backendApi from "~/utils/BackendApi";

const useGetUserData = () => {
    return useQuery(["user"], backendApi.fetchLogin, {
        retry: 0,
    });
};

const UserContent = ({ right }) => {
    const { data, status } = useGetUserData();
    const isLoaded = status === "success";

    let user, name;
    if (isLoaded) {
        user = data.json["User"];
        name = [user?.first_name, user?.last_name].join(" ");
        name = name === " " ? "Anonymous User" : name;
    }

    return (
        <>
            <ContentPane
                primaryText={isLoaded ? name : "Loading..."}
                secondaryText={isLoaded ? user?.username : "Loading..."}
                loading={!isLoaded}
                imgSrc="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=255&q=80"
                right={right}
            />
        </>
    );
};

export default UserContent;
