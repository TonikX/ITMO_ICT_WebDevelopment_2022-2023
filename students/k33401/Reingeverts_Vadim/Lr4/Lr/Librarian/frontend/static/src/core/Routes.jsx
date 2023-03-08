import React from "react";
import { useRoutes } from "react-router-dom";

import Library from "~/pages/Library";
import Profile from "~/pages/Profile";
import Error from "~/pages/Error";

const Routes = ({ queryClient, isCompactViewActive }) => {
    const router = useRoutes([
        {
            path: "/",
            element: <Library isCompactViewActive={isCompactViewActive} />,
            errorElement: <Error />,
        },
        {
            path: "/profile",
            element: <Profile isCompactViewActive={isCompactViewActive} />,
            errorElement: <Error />,
        },
    ]);
    return <>{router}</>;
};

export default Routes;
