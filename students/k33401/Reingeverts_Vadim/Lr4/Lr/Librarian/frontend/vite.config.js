import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

const backend_port = process.env.backend_port ?? 8000;

// https://vitejs.dev/config/
// https://github.com/MrBin99/django-vite-example/blob/master/vite.config.js
export default defineConfig({
    plugins: [react()],
    root: resolve("./static"),
    base: "/static/",
    server: {
        host: "localhost",
        strictPort: true,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
        origin: `http://localhost:${backend_port}`,
    },
    resolve: {
        extensions: [".js", ".jsx", ".json"],
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
});
