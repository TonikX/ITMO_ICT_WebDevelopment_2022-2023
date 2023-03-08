import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Library from "~/pages/Library";

const Routes = ({ queryClient, isCompactViewActive }) => {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <Library isCompactViewActive={isCompactViewActive} />,
        },
    ]);
    return (
        <>
            <RouterProvider router={router} />
        </>
    );
};

export default Routes;
