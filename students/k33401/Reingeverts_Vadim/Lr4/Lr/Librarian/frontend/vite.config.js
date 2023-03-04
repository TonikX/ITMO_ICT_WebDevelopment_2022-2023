import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

export const backendPort = process.env.backend_port ?? 8000;
const host = process.env.host ?? "localhost";

// https://vitejs.dev/config/
// https://github.com/MrBin99/django-vite-example/blob/master/vite.config.js
export default defineConfig({
    plugins: [react()],
    root: resolve("./static"),
    base: "/static/",
    server: {
        strictPort: true,
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
        origin: `http://${host}:${backendPort}`,
    },
    resolve: {
        extensions: [".js", ".jsx", ".json"],
        alias: {
            "~": resolve("./static/src"),
        },
    },
    build: {
        outDir: resolve("./static/dist"),
        assetsDir: "",
        manifest: true,
        emptyOutDir: true,
        target: "es2015",
        rollupOptions: {
            input: {
                main: resolve("./static/src/core/index.js"),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
    define: {
        backendPort: JSON.stringify(backendPort),
    },
});
