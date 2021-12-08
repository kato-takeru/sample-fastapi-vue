import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;

const app = createApp(App).use(router).mount('#app')
app.config.globalProperties.$axios = axios
