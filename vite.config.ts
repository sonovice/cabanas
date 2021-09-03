import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import WindiCSS from 'vite-plugin-windicss'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    WindiCSS.default(),
    svelte()
  ],
  build: {
    outDir: 'docs'
  },
  base: "docs/"
})
