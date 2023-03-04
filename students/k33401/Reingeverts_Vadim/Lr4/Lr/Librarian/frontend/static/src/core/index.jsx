import "vite/modulepreload-polyfill";
import React from "react";
import { createRoot } from "react-dom/client";
import { MantineProvider } from "@mantine/core";

import App from "./App";

const root = createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <MantineProvider theme={{ colorScheme: "dark" }} withGlobalStyles withNormalizeCSS>
            <App />
        </MantineProvider>
    </React.StrictMode>
);
