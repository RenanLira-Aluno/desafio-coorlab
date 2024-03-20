import { createRouter, createMemoryHistory, RouteRecordRaw } from "vue-router";

import HomeView from "./View/HomeView.vue";

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: HomeView
    }
]

export const router = createRouter({
    history: createMemoryHistory(),
    routes: routes
})