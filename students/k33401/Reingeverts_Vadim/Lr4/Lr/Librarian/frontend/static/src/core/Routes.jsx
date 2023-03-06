import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Library from "~/components/Library";
import User from "~/components/UserOld";
import Error from "~/pages/Error";
import Login from "~/pages/Login";

const Routes = ({ queryClient }) => {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <Library />,
        },
        {
            path: "user",
            element: <User queryClient={queryClient} />,
            errorElement: <Error />,
        },
        {
            path: "login",
            element: <Login queryClient={queryClient} />,
            errorElement: <Error />,
        },
    ]);
    return (
        <>
            <RouterProvider router={router} />
        </>
    );
};

export default Routes;
