// @ts-check
import { defineConfig } from "astro/config";

import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    preview: {
      allowedHosts: ["*", "foodie-fe.avei.ovh"],
    },
    server: {
      host: "0.0.0.0",
    },
  },
});
