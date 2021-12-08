import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/trends',
        name: 'trends',
        component: () => import(/* webpackChunkName: "about" */ '../views/Trends.vue')
    },
    {
        path: '/trends/:id',
        name: 'trend',
        component: () => import(/* webpackChunkName: "about" */ '../views/Trend.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
