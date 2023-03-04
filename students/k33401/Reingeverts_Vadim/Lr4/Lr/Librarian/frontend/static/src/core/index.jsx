import "vite/modulepreload-polyfill";
import React from "react";
import { createRoot } from "react-dom/client";
import { MantineProvider } from "@mantine/core";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { Notifications } from "@mantine/notifications";

import App from "~/core/App";

const queryClient = new QueryClient();

const root = createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <QueryClientProvider client={queryClient}>
            <MantineProvider theme={{ colorScheme: "dark" }} withGlobalStyles withNormalizeCSS>
                <Notifications />
                <App queryClient={queryClient} />
            </MantineProvider>
            <ReactQueryDevtools />
        </QueryClientProvider>
    </React.StrictMode>
);
