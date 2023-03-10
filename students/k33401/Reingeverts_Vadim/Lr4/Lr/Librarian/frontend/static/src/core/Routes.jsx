import React from "react";
import { useRoutes } from "react-router-dom";

import Home from "~/pages/Home";
import BookCollection from "~/pages/BookCollection";
import ProfileBookCollection from "~/pages/ProfileBookCollection";
import Error from "~/pages/Error";

const Routes = ({ queryClient, isCompactViewActive }) => {
    const router = useRoutes([
        {
            path: "/",
            element: <Home title="Home" isCompactViewActive={isCompactViewActive} />,
            errorElement: <Error />,
        },
        {
            path: "/:id",
            element: (
                <BookCollection
                    queryClient={queryClient}
                    isCompactViewActive={isCompactViewActive}
                />
            ),
            errorElement: <Error />,
        },
        {
            path: "/profile",
            element: (
                <ProfileBookCollection
                    queryClient={queryClient}
                    isCompactViewActive={isCompactViewActive}
                />
            ),
            errorElement: <Error />,
        },
    ]);
    return <>{router}</>;
};

export default Routes;
