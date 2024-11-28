import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000 // 或其他未被占用的端口
  }
})

export const API_URL = 'http://localhost:5000'