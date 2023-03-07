import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Library from "~/pages/Library";

const Routes = ({ queryClient }) => {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <Library />,
        },
    ]);
    return (
        <>
            <RouterProvider router={router} />
        </>
    );
};

export default Routes;
