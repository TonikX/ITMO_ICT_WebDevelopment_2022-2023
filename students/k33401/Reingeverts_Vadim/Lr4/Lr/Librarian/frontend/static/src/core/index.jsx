import "vite/modulepreload-polyfill";
import React from "react";
import { createRoot } from "react-dom/client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

import App from "~/core/App";

const queryClient = new QueryClient();

const root = createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <QueryClientProvider client={queryClient}>
            <App queryClient={queryClient} />
            <ReactQueryDevtools position="bottom-right" />
        </QueryClientProvider>
    </React.StrictMode>
);
