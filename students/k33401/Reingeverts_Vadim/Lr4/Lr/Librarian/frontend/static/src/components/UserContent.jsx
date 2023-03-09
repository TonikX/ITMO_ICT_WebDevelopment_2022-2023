import React from "react";

import ContentPane from "~/components/ContentPane";
import { useGetUserData } from "~/hooks";

const UserContent = ({ right }) => {
    const { data: user, status } = useGetUserData();
    const isLoaded = status === "success";

    let name;
    if (isLoaded) {
        name = [user?.first_name, user?.last_name].join(" ");
        name = name === " " ? "Anonymous User" : name;
    }
    console.log("user", user);
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
