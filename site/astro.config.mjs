import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://kinhluan.github.io",
  base: "/skills",
  output: "static",
  trailingSlash: "always",
  build: {
    format: "directory"
  }
});
