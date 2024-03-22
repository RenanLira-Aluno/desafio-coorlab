import { createRouter, RouteRecordRaw, createWebHistory } from "vue-router";

import HomeView from "./views/HomeView.vue";
import CalculadoraView from "./views/CalculatorView.vue";

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: HomeView
    },
    {
        path: '/calculadora',
        component: CalculadoraView
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes: routes
})