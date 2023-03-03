import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vitejs.dev/config/
// https://github.com/MrBin99/django-vite-example/blob/master/vite.config.js
export default defineConfig({
    plugins: [react()],
    root: resolve("./static/src"),
    base: "/static/",
    server: {
        host: "localhost",
        port: 3000,
        strictPort: true,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
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
