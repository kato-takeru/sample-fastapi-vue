import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { store } from "./store";
import axios from 'axios'
import './index.css'

axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;

const app = createApp(App)
    .use(store)
    .use(router)
    .mount('#app')

app.config.globalProperties.$axios = axios
