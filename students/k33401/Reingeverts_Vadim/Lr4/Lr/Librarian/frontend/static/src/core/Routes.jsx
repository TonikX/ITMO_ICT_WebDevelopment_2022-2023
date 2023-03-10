import React from "react";
import { useRoutes } from "react-router-dom";

import BookCollection from "~/pages/BookCollection";
import ProfileBookCollection from "~/pages/ProfileBookCollection";
import Error from "~/pages/Error";

const Routes = ({ queryClient, isCompactViewActive, libraries, librariesStatus }) => {
    const router = useRoutes([
        {
            path: "/",
            element: <h1>empty so far</h1>,
            errorElement: <Error />,
        },
        {
            path: "/:id",
            element: (
                <BookCollection
                    queryClient={queryClient}
                    isCompactViewActive={isCompactViewActive}
                    libraries={libraries}
                    librariesStatus={librariesStatus}
                />
            ),
            errorElement: <Error />,
        },
        {
            path: "/profile",
            element: <ProfileBookCollection isCompactViewActive={isCompactViewActive} />,
            errorElement: <Error />,
        },
    ]);
    return <>{router}</>;
};

export default Routes;
