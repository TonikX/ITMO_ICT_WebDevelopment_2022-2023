import "vite/modulepreload-polyfill";
import React from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const root = createRoot(document.getElementById("root"));
root.render(
    <p>what</p>
    // <React.StrictMode>
    //     <App />
    // </React.StrictMode>
);

alert("App loaded!");
