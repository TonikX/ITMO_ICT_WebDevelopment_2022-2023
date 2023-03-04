import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Library from "~/components/Library";
import User from "~/components/User";
import Error from "~/components/Error";

const App = ({ queryClient }) => {
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
    ]);
    return (
        <>
            <RouterProvider router={router} />
        </>
    );
};

export default App;
