<script setup lang="ts">
import Logo from './Logo.vue'
import ItemMenu from './ItemMenu.vue'
</script>

<template>
    <div class="menu">
        <Logo />
        <nav>
            <ul>
                <ItemMenu title="Calculadora de Viagem" />
            </ul>
        </nav>
    </div>
</template>

<style scoped>
.menu {
    @apply p-8 h-screen flex bg-slate-600 w-1/5 flex-col items-start gap-6;
}
</style>