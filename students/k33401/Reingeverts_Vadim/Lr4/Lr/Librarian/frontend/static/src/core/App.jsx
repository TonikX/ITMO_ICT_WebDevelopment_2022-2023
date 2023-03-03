import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import Library from "../components/Library";
import User from "../components/User";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Library />,
    },
    {
        path: "user",
        element: <User />,
    },
]);

const App = () => {
    return (
        <>
            <RouterProvider router={router} />
        </>
    );
};

export default App;
